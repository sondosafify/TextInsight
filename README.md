# 🧠 TextInsight NLP Analyzer

A professional NLP text analysis application built with Python, spaCy, and Streamlit.

TextInsight analyzes any input text through a complete Natural Language Processing pipeline and presents the results in an interactive interface.

---

## Project Overview

TextInsight is designed to demonstrate a complete NLP workflow starting from raw text preprocessing to advanced linguistic analysis.

The application performs:

- Text Cleaning
- Tokenization
- Stop Words Removal
- Lemmatization
- Part-of-Speech Tagging
- Dependency Parsing
- Named Entity Recognition (NER)
- Text Statistics

---

## Features

### Text Preprocessing

The application cleans raw text by applying:

- Lowercasing
- Removing punctuation
- Removing extra spaces
- Removing emails
- Removing HTML tags
- Removing emojis
- Removing repeated characters


### Tokenization

Splits text into individual tokens using spaCy tokenizer.


### Stop Words Removal

Removes common words that do not add significant meaning to the analysis.


### Lemmatization

Converts words into their base form.

Example:
announced → announce
released → release
celebrated → celebrate

### POS Tagging

Identifies the grammatical role of each word.

Example:
Google → PROPN
announced → VERB
technology → NOUN



### Dependency Parsing

Analyzes relationships between words and identifies sentence structure.


### Named Entity Recognition (NER)

Extracts important entities from text.



### Statistics

Provides:

- Number of characters
- Number of words
- Unique words count
- Average word length
- Most common words

---

# Project Structure
│
├── src/
│ ├── preprocessing.py
│ ├── tokenizer.py
│ ├── pos_tagger.py
│ ├── dependency_parser.py
│ ├── ner.py
│ ├── statistics.py
│ ├── pipeline.py
│ └── main.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
