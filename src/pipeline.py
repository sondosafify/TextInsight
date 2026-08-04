from src.preprocessing import preprocess_text

from src.tokenizer import (
    tokenize_text,
    remove_stopwords,
    lemmatize_tokens
)

from src.pos_tagger import pos_tag_text

from src.dependency_parser import dependency_parse_text

from src.ner import extract_entities

from src.statistics import text_statistics



class TextInsightPipeline:
    """
    Complete NLP pipeline for TextInsight.
    """


    def analyze(self, text: str) -> dict:
        """
        Run complete NLP analysis.
        """


        results = {}


        # Preprocessing
        cleaned_text = preprocess_text(text)

        results["clean_text"] = cleaned_text


        # Tokenization
        tokens = tokenize_text(cleaned_text)

        results["tokens"] = tokens


        # Stop Words Removal
        filtered_tokens = remove_stopwords(tokens)

        results["filtered_tokens"] = filtered_tokens


        # Lemmatization
        lemmas = lemmatize_tokens(filtered_tokens)

        results["lemmas"] = lemmas


        # POS Tagging
        pos_results = pos_tag_text(cleaned_text)

        results["pos"] = pos_results


        # Dependency Parsing
        dependencies = dependency_parse_text(cleaned_text)

        results["dependencies"] = dependencies


        # NER
        entities = extract_entities(cleaned_text)

        results["entities"] = entities


        # Statistics
        stats = text_statistics(
            cleaned_text,
            tokens
        )

        results["statistics"] = stats


        return results