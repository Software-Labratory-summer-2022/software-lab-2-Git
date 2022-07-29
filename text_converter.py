import emoji

PERSIAN_DIGITS = "۰۱۲۳۴۵۶۷۸۹"
ENGLISH_DIGITS = "0123456789"
PERSIAN_TO_ENGLISH = dict(zip(PERSIAN_DIGITS, ENGLISH_DIGITS))
ENGLISH_TO_PERSIAN = dict(zip(ENGLISH_DIGITS, PERSIAN_DIGITS))


def dictinary_replacing(string, replace):
    for key, value in replace.items():
        string = string.replace(key, value)
    return string


def change_digits_to_persian(string):
    return dictinary_replacing(string, ENGLISH_TO_PERSIAN)


def change_digits_to_english(string):
    return dictinary_replacing(string, PERSIAN_TO_ENGLISH)


def replace_emoji(message):
    char_emojis = {
        ':)': ':smiling_face_with_smiling_eyes:',
        ':(': ':disappointed_face:',
        ';)': ':winking_face:',
        ':D': ':grinning_face_with_big_eyes:',
    }
    # This replace replacing pattern that defined in char_emojis
    message = dictinary_replacing(message, char_emojis)
    return emoji.emojize(message)
