import spacy
from spacy import displacy


nlp = spacy.load("en_core_web_sm")


def visualize_entities(text: str):
    """
    Visualize Named Entities.
    """

    doc = nlp(text)

    displacy.serve(
        doc,
        style="ent"
    )