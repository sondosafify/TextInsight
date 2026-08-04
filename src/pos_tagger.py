import spacy


nlp = spacy.load("en_core_web_sm")


def pos_tag_text(text: str) -> list:
    """
    Perform POS tagging using spaCy.
    """

    doc = nlp(text)

    pos_tags = []

    for token in doc:
        pos_tags.append(
            {
                "token": token.text,
                "pos": token.pos_,
                "description": token.tag_
            }
        )

    return pos_tags