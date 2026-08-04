import re


def to_lowercase(text: str) -> str:
    """
    Convert all characters in the text to lowercase.
    """
    return text.lower()


def remove_emails(text: str) -> str:
    """
    Remove email addresses from the text.
    """
    pattern = r"\S+@\S+"
    return re.sub(pattern, "", text)


def remove_html(text: str) -> str:
    """
    Remove HTML tags from the text.
    """
    pattern = r"<.*?>"
    return re.sub(pattern, "", text)


def remove_emojis(text: str) -> str:
    """
    Remove emojis and special unicode characters.
    """
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"
        "\U0001F300-\U0001F5FF"
        "\U0001F680-\U0001F6FF"
        "\U0001F700-\U0001F77F"
        "\U0001F900-\U0001F9FF"
        "]+",
        flags=re.UNICODE
    )

    return emoji_pattern.sub(r"", text)


def remove_punctuation(text: str) -> str:
    """
    Remove punctuation marks from the text.
    """
    return re.sub(r"[^\w\s]", "", text)


def remove_numbers(text: str) -> str:
    """
    Remove numeric characters from the text.
    """
    return re.sub(r"\d+", "", text)


def remove_extra_spaces(text: str) -> str:
    """
    Remove unnecessary spaces from the text.
    """
    return re.sub(r"\s+", " ", text).strip()


def preprocess_text(text: str) -> str:
    """
    Apply complete text preprocessing pipeline.
    """

    text = to_lowercase(text)

    text = remove_emails(text)

    text = remove_html(text)

    text = remove_emojis(text)

    text = remove_punctuation(text)

    text = remove_numbers(text)

    text = remove_extra_spaces(text)

    return text