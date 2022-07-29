import text_converter


def get_response(message):
    message = text_converter.replace_emoji(message)
    yield message
