import spacy


# Load spaCy model
nlp = spacy.load("en_core_web_sm")


def tokenize_text(text: str) -> list:
    """
    Tokenize text using spaCy tokenizer.
    """

    doc = nlp(text)

    tokens = [token.text for token in doc]

    return tokens

# Remove stop words
def remove_stopwords(tokens: list) -> list:
    """
    Remove stop words from token list.
    """

    filtered_tokens = []

    for token in tokens:
        if not nlp.vocab[token].is_stop:
            filtered_tokens.append(token)

    return filtered_tokens


# lemmatize tokens
def lemmatize_tokens(tokens: list) -> list:
    """
    Convert tokens into their base forms using spaCy.
    """

    doc = nlp(" ".join(tokens))

    lemmas = [token.lemma_ for token in doc]

    return lemmas