import streamlit as st

from src.pipeline import TextInsightPipeline


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="TextInsight",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# Custom CSS
# =========================================================

st.markdown(
    """
    <style>

    /* =========================
       Global
       ========================= */

    .stApp {
        background: #0b1020;
        color: #ffffff !important;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }


    /* =========================
       Header
       ========================= */

    .main-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 0;
        color: #ffffff !important;
        letter-spacing: -1px;
    }

    .subtitle {
        color: #ffffff !important;
        font-size: 16px;
        margin-top: 4px;
        margin-bottom: 25px;
    }


    /* =========================
       Cards
       ========================= */

    .card {
        background: #151c2f;
        border: 1px solid #283149;
        border-radius: 18px;
        padding: 22px;
        margin-bottom: 18px;
        color: #ffffff !important;
    }

    .card-title {
        font-size: 18px;
        font-weight: 700;
        color: #ffffff !important;
        margin-bottom: 6px;
    }

    .card-description {
        color: #ffffff !important;
        font-size: 13px;
        margin-bottom: 15px;
    }


    /* =========================
       Section Labels
       ========================= */

    .section-title {
        font-size: 24px;
        font-weight: 750;
        color: #ffffff !important;
        margin-top: 20px;
        margin-bottom: 12px;
    }


    /* =========================
       Metrics
       ========================= */

    [data-testid="stMetric"] {
        background: #151c2f;
        border: 1px solid #283149;
        border-radius: 15px;
        padding: 15px;
    }

    [data-testid="stMetricLabel"] {
        color: #ffffff !important;
    }

    [data-testid="stMetricValue"] {
        color: #ffffff !important;
    }


    /* =========================
       Text Area
       ========================= */

    textarea {
        background-color: #151c2f !important;
        color: #ffffff !important;
        border: 1px solid #34405a !important;
        border-radius: 16px !important;
        font-size: 15px !important;
    }


    /* =========================
       Buttons
       ========================= */

    .stButton > button {
        border-radius: 12px;
        border: 1px solid #34405a;
        background: #151c2f;
        color: #ffffff !important;
        font-weight: 600;
        min-height: 44px;
        transition: 0.2s;
    }

    .stButton > button:hover {
        border-color: #4f8cff;
        color: #ffffff !important;
    }


    /* Analyze Button */

    .analyze-button button {
        background: #1f8f8a !important;
        border: none !important;
        color: #ffffff !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        min-height: 52px !important;
    }


    /* =========================
       Tabs
       ========================= */

    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: transparent;
    }

    .stTabs [data-baseweb="tab"] {
        background: #151c2f;
        border-radius: 12px;
        padding: 10px 18px;
        border: 1px solid #283149;
        color: #ffffff !important;
    }

    .stTabs [aria-selected="true"] {
        background: #1f8f8a;
        color: #ffffff !important;
    }


    /* =========================
       Expanders
       ========================= */

    .streamlit-expanderHeader {
        background: #151c2f;
        border-radius: 12px;
        color: #ffffff !important;
    }


    /* =========================
       Result Box
       ========================= */

    .result-box {
        background: #101729;
        border: 1px solid #283149;
        border-radius: 14px;
        padding: 18px;
        color: #ffffff !important;
        line-height: 1.7;
        word-wrap: break-word;
    }


    /* =========================
       Token Pills
       ========================= */

    .token-container {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }

    .token {
        background: #202a42;
        border: 1px solid #35415d;
        color: #ffffff !important;
        padding: 6px 10px;
        border-radius: 9px;
        font-size: 13px;
    }


    /* =========================
       Entity Pills
       ========================= */

    .entity {
        display: inline-block;
        background: #242c4b;
        border: 1px solid #485477;
        color: #ffffff !important;
        padding: 7px 12px;
        border-radius: 10px;
        margin: 4px;
        font-size: 13px;
    }


    /* =========================
       Footer
       ========================= */

    .footer {
        text-align: center;
        color: #ffffff !important;
        font-size: 12px;
        padding-top: 30px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# Pipeline
# =========================================================

analyzer = TextInsightPipeline()


# =========================================================
# Header
# =========================================================

st.markdown(
    '<div class="main-title">🧠 TextInsight</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Professional Natural Language Processing & Text Analysis Platform
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# Input Card
# =========================================================

st.markdown(
    """
    <div class="card">
        <div class="card-title">Text Analysis</div>
        <div class="card-description">
            Type or paste text to analyze it using the TextInsight NLP pipeline.
        </div>
    """,
    unsafe_allow_html=True
)

text = st.text_area(
    "Input",
    height=170,
    label_visibility="collapsed",
    placeholder=(
        "Example: Google announced a new artificial intelligence "
        "project in New York on March 15, 2026..."
    )
)

st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# Analysis Options
# =========================================================

st.markdown(
    '<div class="section-title">Analysis Modules</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    show_preprocessing = st.toggle(
        "Preprocessing",
        value=True
    )

with col2:
    show_linguistic = st.toggle(
        "Linguistic Analysis",
        value=True
    )

with col3:
    show_entities = st.toggle(
        "Entity Analysis",
        value=True
    )

with col4:
    show_statistics = st.toggle(
        "Statistics",
        value=True
    )


# =========================================================
# Analyze Button
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    '<div class="analyze-button">',
    unsafe_allow_html=True
)

analyze_clicked = st.button(
    "Analyze Text",
    use_container_width=True
)

st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# Analysis
# =========================================================

if analyze_clicked:

    if not text.strip():

        st.warning("Please enter some text before starting the analysis.")

    else:

        with st.spinner("Running NLP pipeline..."):

            results = analyzer.analyze(text)

        st.success("Analysis completed successfully.")


        # =================================================
        # Overview Metrics
        # =================================================

        statistics = results["statistics"]

        st.markdown(
            '<div class="section-title">Overview</div>',
            unsafe_allow_html=True
        )

        metric1, metric2, metric3, metric4 = st.columns(4)

        with metric1:
            st.metric(
                "Characters",
                statistics.get("characters", 0)
            )

        with metric2:
            st.metric(
                "Words",
                statistics.get("words", 0)
            )

        with metric3:
            st.metric(
                "Unique Words",
                statistics.get("unique_words", 0)
            )

        with metric4:
            st.metric(
                "Tokens",
                len(results["tokens"])
            )


        # =================================================
        # Result Tabs
        # =================================================

        tab_preprocessing, tab_linguistic, tab_entities, tab_statistics = st.tabs(
            [
                "Preprocessing",
                "Linguistic Analysis",
                "Entity Analysis",
                "Statistics"
            ]
        )


        # =================================================
        # Preprocessing Tab
        # =================================================

        with tab_preprocessing:

            if show_preprocessing:

                st.markdown(
                    '<div class="section-title">Preprocessing</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    """
                    <div class="card">
                        <div class="card-title">Clean Text</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(
                    f"""
                    <div class="result-box">
                        {results["clean_text"]}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown("<br>", unsafe_allow_html=True)

                st.markdown(
                    "Tokens",
                    help="Tokens generated by the spaCy tokenizer."
                )

                token_html = "".join(
                    f'<span class="token">{token}</span>'
                    for token in results["tokens"]
                )

                st.markdown(
                    f'<div class="token-container">{token_html}</div>',
                    unsafe_allow_html=True
                )

                st.markdown("<br>", unsafe_allow_html=True)

                with st.expander("After Stop Words Removal"):

                    filtered_html = "".join(
                        f'<span class="token">{token}</span>'
                        for token in results["filtered_tokens"]
                    )

                    st.markdown(
                        f'<div class="token-container">{filtered_html}</div>',
                        unsafe_allow_html=True
                    )

                with st.expander("Lemmatization"):

                    lemma_html = "".join(
                        f'<span class="token">{lemma}</span>'
                        for lemma in results["lemmas"]
                    )

                    st.markdown(
                        f'<div class="token-container">{lemma_html}</div>',
                        unsafe_allow_html=True
                    )

            else:

                st.info(
                    "Preprocessing module is currently disabled."
                )


        # =================================================
        # Linguistic Analysis Tab
        # =================================================

        with tab_linguistic:

            if show_linguistic:

                st.markdown(
                    '<div class="section-title">Linguistic Analysis</div>',
                    unsafe_allow_html=True
                )

                with st.expander(
                    "POS Tagging",
                    expanded=True
                ):

                    for item in results["pos"]:

                        token = item.get("token", "")
                        pos = item.get("pos", "")
                        description = item.get("description", "")

                        st.markdown(
                            f"""
                            <div class="card">
                                <strong>{token}</strong>
                                <br>
                                <span style="color:#ffffff;">
                                    {pos}
                                </span>
                                <span style="color:#ffffff;">
                                    — {description}
                                </span>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )


                with st.expander(
                    "Dependency Parsing"
                ):

                    for item in results["dependencies"]:

                        token = item.get("token", "")
                        dependency = item.get("dependency", "")
                        head = item.get("head", "")
                        head_pos = item.get("head_pos", "")

                        st.markdown(
                            f"""
                            <div class="card">
                                <strong>{token}</strong>
                                <span style="color:#ffffff;">
                                    → {dependency} →
                                </span>
                                <strong>{head}</strong>
                                <span style="color:#ffffff;">
                                    ({head_pos})
                                </span>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

            else:

                st.info(
                    "Linguistic analysis module is currently disabled."
                )


        # =================================================
        # Entity Analysis Tab
        # =================================================

        with tab_entities:

            if show_entities:

                st.markdown(
                    '<div class="section-title">Named Entities</div>',
                    unsafe_allow_html=True
                )

                entities = results["entities"]

                if entities:

                    for entity in entities:

                        entity_text = entity.get(
                            "text",
                            ""
                        )

                        label = entity.get(
                            "label",
                            ""
                        )

                        description = entity.get(
                            "description",
                            ""
                        )

                        st.markdown(
                            f"""
                            <div class="card">
                                <div class="card-title">
                                    {entity_text}
                                </div>

                                <span class="entity">
                                    {label}
                                </span>

                                <div class="card-description">
                                    {description}
                                </div>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                else:

                    st.info(
                        "No named entities were detected."
                    )

            else:

                st.info(
                    "Entity analysis module is currently disabled."
                )


        # =================================================
        # Statistics Tab
        # =================================================

        with tab_statistics:

            if show_statistics:

                st.markdown(
                    '<div class="section-title">Text Statistics</div>',
                    unsafe_allow_html=True
                )

                statistics = results["statistics"]

                stat1, stat2 = st.columns(2)

                with stat1:

                    st.metric(
                        "Characters",
                        statistics.get("characters", 0)
                    )

                    st.metric(
                        "Words",
                        statistics.get("words", 0)
                    )

                with stat2:

                    st.metric(
                        "Unique Words",
                        statistics.get("unique_words", 0)
                    )

                    st.metric(
                        "Average Word Length",
                        statistics.get(
                            "average_word_length",
                            0
                        )
                    )


                st.markdown("<br>", unsafe_allow_html=True)

                st.markdown(
                    "Most Common Words"
                )

                common_words = statistics.get(
                    "most_common_words",
                    []
                )

                if common_words:

                    for word, count in common_words:

                        st.markdown(
                            f"""
                            <div class="card">
                                <strong>{word}</strong>
                                <span style="float:right;">
                                    {count}
                                </span>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

            else:

                st.info(
                    "Statistics module is currently disabled."
                )


# =========================================================
# Footer
# =========================================================

st.markdown(
    """
    <div class="footer">
        TextInsight NLP Analyzer · Python · spaCy · Streamlit
    </div>
    """,
    unsafe_allow_html=True
)