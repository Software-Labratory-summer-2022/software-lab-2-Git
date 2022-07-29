import text_converter

DEFINED_SCRIPTES = {
    "سلام": "علیک سلام",
    "چطوری؟": "خوبم تو چطوری؟"
}


def is_script(message):
    return message.startswith("+ ")


def get_response(message):
    message = text_converter.replace_emoji(message)
    if is_script(message):
        script = message[2:]
        if script in DEFINED_SCRIPTES:
            yield DEFINED_SCRIPTES[script]
    else:
        yield message
