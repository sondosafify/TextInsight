from preprocessing import preprocess_text
from tokenizer import (
    tokenize_text,
    remove_stopwords,
    lemmatize_tokens
)
from pos_tagger import pos_tag_text
from dependency_parser import dependency_parse_text
from ner import extract_entities
from statistics import text_statistics

def main():
    """
    Main pipeline for TextInsight NLP Analyzer.
    """

    # Get input
    text = input("Enter your text: ")


    print("\n========== Original Text ==========")
    print(text)


    # -------------------------
    # Preprocessing
    # -------------------------

    cleaned_text = preprocess_text(text)

    print("\n========== Clean Text ==========")
    print(cleaned_text)


    # -------------------------
    # Tokenization
    # -------------------------

    tokens = tokenize_text(cleaned_text)

    print("\n========== Tokens ==========")
    print(tokens)


    # -------------------------
    # Stop Words Removal
    # -------------------------

    filtered_tokens = remove_stopwords(tokens)

    print("\n========== After Stop Words Removal ==========")
    print(filtered_tokens)


    # -------------------------
    # Lemmatization
    # -------------------------

    lemmas = lemmatize_tokens(filtered_tokens)

    print("\n========== Lemmatized Tokens ==========")
    print(lemmas)


    # -------------------------
    # POS Tagging
    # -------------------------

    pos_results = pos_tag_text(cleaned_text)

    print("\n========== POS Tagging ==========")

    for item in pos_results:
        print(item)


    # -------------------------
    # Dependency Parsing
    # -------------------------

    dependencies = dependency_parse_text(cleaned_text)

    print("\n========== Dependency Parsing ==========")

    for item in dependencies:
        print(item)


    # -------------------------
    # Named Entity Recognition
    # -------------------------

    entities = extract_entities(cleaned_text)

    print("\n========== Named Entities ==========")

    for entity in entities:
        print(entity)


    # -------------------------
    # Statistics
    # -------------------------

    stats = text_statistics(
        cleaned_text,
        tokens
    )

    print("\n========== Statistics ==========")

    for key, value in stats.items():
        print(f"{key}: {value}")



if __name__ == "__main__":
    main()