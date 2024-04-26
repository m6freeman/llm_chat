from result import Result, Ok


def do_thing() -> Result[str, Exception]:
    return Ok("Hello world!")
