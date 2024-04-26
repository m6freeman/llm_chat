import time
import requests
import json
from result import Result, Ok, Err


def main():
    initial_prompt = (
        "Let's talk about solving all the worlds problems."
        " Humans have kinda fucked things up."
        " How should we do things differently?"
        " Reply in 50 words or less."
    )
    url = "http://localhost:11434/api/generate"
    data = {"model": "llama3", "prompt": initial_prompt}
    try:
        print(initial_prompt)
        print("###########################################")
        response = requests.post(
            url,
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        response.raise_for_status()
        json_response = response.text
        initial_response = parse_message(json_response).unwrap_or_raise(Exception)
        print("llama3:")
        print(initial_response)
        print("###########################################")
    except requests.exceptions.RequestException as e:
        return f"Failed to send initial request: {e}"
    except ParseException as e:
        return f"Failed to parse initial message: {e}"
    reply = initial_response
    model_toggle = True
    while True:
        try:
            reply, model_toggle = talk(reply, model_toggle)
            time.sleep(10)
        except Exception as e:
            return str(e)


class ParseException(Exception):
    pass


def talk(reply: str, model_toggle: bool) -> tuple[str, bool]:
    model_names: dict[bool, str] = {
        True: "mistral",
        False: "llama3",
    }
    try:
        prompt = reply + (
            " Skip the positive affirmations."
            " Reply in a conversational manner that concicely responds to"
            " the question, but maintain a reasonable level of skepticism."
            " Attempt to provoke a response from me about the topic."
            " Reply in 50 words or less."
        )
        url = "http://localhost:11434/api/generate"
        data = {"model": model_names[model_toggle], "prompt": prompt}
        response = requests.post(
            url,
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
        )
        response.raise_for_status()
        json_response = response.text
        return_response = (
            parse_message(json_response).unwrap_or_raise(Exception),
            not model_toggle,
        )
        print(model_names[model_toggle], ":")
        print(return_response[0])
        print("###########################################")
        return return_response
    except Exception as e:
        raise e


def parse_message(json_response) -> Result[str, Exception]:
    messages = []
    for line in json_response.splitlines():
        try:
            obj = json.loads(line)
            if not obj["done"]:
                messages.append(obj["response"])
        except Exception as e:
            return Err(e)
    reconstructed_message: str = "".join(messages)
    return Ok(reconstructed_message)


if __name__ == "__main__":
    main()
