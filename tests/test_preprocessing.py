from src.preprocessing import preprocess_text


def test_preprocess_text():

    text = """
    Hello WORLD!!! 
    Contact me at test@gmail.com 😊
    <h1>NLP 2026</h1>
    """

    result = preprocess_text(text)

    expected = "hello world contact me at nlp"

    assert result == expected


if __name__ == "__main__":
    test_preprocess_text()
    print("Test passed successfully!")