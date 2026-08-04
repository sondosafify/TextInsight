import streamlit as st

from src.pipeline import TextInsightPipeline


# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="TextInsight NLP Analyzer",
    page_icon="🧠",
    layout="wide"
)


# =========================
# Header
# =========================

st.title("🧠 TextInsight NLP Analyzer")

st.markdown(
    """
    **Professional NLP Text Analysis Tool**

    Analyze text using:

    - Text Preprocessing
    - Tokenization
    - Lemmatization
    - POS Tagging
    - Dependency Parsing
    - Named Entity Recognition
    - Statistics
    """
)

st.divider()


# =========================
# Pipeline Initialization
# =========================

analyzer = TextInsightPipeline()


# =========================
# User Input
# =========================

text = st.text_area(
    "Enter your text",
    height=180,
    placeholder="Example: Apple announced a new product in Cairo..."
)


# =========================
# Sidebar Options
# =========================

st.sidebar.title("Analysis Options")

st.sidebar.write(
    "Choose the analysis components:"
)


show_clean = st.sidebar.checkbox(
    "Clean Text"
)

show_tokens = st.sidebar.checkbox(
    "Tokens"
)

show_filtered = st.sidebar.checkbox(
    "Stop Words Removal"
)

show_lemmas = st.sidebar.checkbox(
    "Lemmatization"
)

show_pos = st.sidebar.checkbox(
    "POS Tagging"
)

show_dependencies = st.sidebar.checkbox(
    "Dependency Parsing"
)

show_entities = st.sidebar.checkbox(
    "Named Entities"
)

show_statistics = st.sidebar.checkbox(
    "Statistics"
)


st.sidebar.divider()


select_all = st.sidebar.checkbox(
    "Select All"
)


if select_all:

    show_clean = True
    show_tokens = True
    show_filtered = True
    show_lemmas = True
    show_pos = True
    show_dependencies = True
    show_entities = True
    show_statistics = True



# =========================
# Analyze Button
# =========================

if st.button(
    "Analyze Text",
    use_container_width=True
):

    if not text.strip():

        st.warning(
            "Please enter text first."
        )


    else:

        with st.spinner(
            "Analyzing text..."
        ):

            results = analyzer.analyze(text)


        st.success(
            "Analysis Completed Successfully"
        )


        # =========================
        # Results
        # =========================


        if show_clean:

            st.subheader(
                "Clean Text"
            )

            st.info(
                results["clean_text"]
            )


        if show_tokens:

            st.subheader(
                "Tokens"
            )

            st.code(
                "\n".join(results["tokens"])
            )

            st.caption(
                f"Total Tokens: {len(results['tokens'])}"
            )


        if show_filtered:

            st.subheader(
                "After Stop Words Removal"
            )

            st.code(
                "\n".join(results["filtered_tokens"])
            )


        if show_lemmas:

            st.subheader(
                "Lemmatization"
            )

            st.code(
                "\n".join(results["lemmas"])
            )


        if show_pos:

            st.subheader(
                "POS Tagging"
            )

            st.code(
                str(results["pos"])
            )


        if show_dependencies:

            st.subheader(
                "Dependency Parsing"
            )

            st.code(
                str(results["dependencies"])
            )


        if show_entities:

            st.subheader(
                "Named Entities"
            )

            if results["entities"]:

                st.code(
                    str(results["entities"])
                )

            else:

                st.info(
                    "No entities detected."
                )


        if show_statistics:

            st.subheader(
                "Statistics"
            )

            for key, value in results["statistics"].items():

                st.write(
                    f"**{key.replace('_', ' ').title()}:** {value}"
                )



# =========================
# Footer
# =========================

st.divider()

st.caption(
    "Built with Python • spaCy • Streamlit | TextInsight NLP Analyzer"
)