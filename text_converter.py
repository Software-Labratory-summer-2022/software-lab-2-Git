import emoji


def dictinary_replacing(string, replace):
    for key, value in replace.items():
        string = string.replace(key, value)
    return string


def replace_emoji(message):
    char_emojis = {
        ':)': ':smiling_face_with_smiling_eyes:',
        ':(': ':disappointed_face:',
        ';)': ':winking_face:',
        ':D': ':grinning_face_with_big_eyes:',
        ':-/': ':confused_face:',
        '">': ':grinning_face_with_sweat:',
        'P': ':face_with_tongue:'
    }
    # This replace replacing pattern that defined in char_emojis
    message = dictinary_replacing(message, char_emojis)
    return emoji.emojize(message)
