import spacy


nlp = spacy.load("en_core_web_sm")


def dependency_parse_text(text: str) -> list:
    """
    Perform dependency parsing using spaCy.
    """

    doc = nlp(text)

    dependencies = []

    for token in doc:
        dependencies.append(
            {
                "token": token.text,
                "dependency": token.dep_,
                "head": token.head.text,
                "head_pos": token.head.pos_
            }
        )

    return dependencies