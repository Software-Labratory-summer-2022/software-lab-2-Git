import text_converter

DEFINED_SCRIPTES = {
    "سلام": "علیک سلام",
    "چطوری؟": "خوبم تو چطوری؟"
}
NOT_FOUND_MESSAGE = "وات؟"


def is_script(message):
    return message.startswith("+ ")


def get_response(message):
    message = text_converter.replace_emoji(message)
    message = text_converter.change_digits_to_english(message)
    if is_script(message):
        script = message[2:]
        if script in DEFINED_SCRIPTES:
            yield DEFINED_SCRIPTES[script]
        elif script.startswith("بشمار"):
            number = int(script[5:])
            for i in range(number):
                yield text_converter.change_digits_to_persian(str(i + 1))
        else:
            yield NOT_FOUND_MESSAGE
    else:
        message = text_converter.change_digits_to_persian(message)
        yield message
