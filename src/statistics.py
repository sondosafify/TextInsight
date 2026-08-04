from collections import Counter


def text_statistics(text: str, tokens: list) -> dict:
    """
    Generate text statistics.
    """

    stats = {}

    # Characters count
    stats["characters"] = len(text)

    # Total words
    stats["words"] = len(tokens)

    # Unique words
    stats["unique_words"] = len(set(tokens))

    # Average word length
    if tokens:
        stats["average_word_length"] = (
            sum(len(word) for word in tokens) / len(tokens)
        )
    else:
        stats["average_word_length"] = 0

    # Most common words
    counter = Counter(tokens)

    stats["most_common_words"] = counter.most_common(5)

    return stats