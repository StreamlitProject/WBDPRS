import streamlit as st

st.set_page_config(
    page_title="HealthPulse",
    page_icon="assets/favicon.svg",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    :root {
        --accent: #0f9b8e;
        --accent-light: #6cdacf;
        --accent-dark: #0a7a6e;
        --bg-primary: #0e1117;
        --bg-secondary: #1a1d24;
        --bg-card: #1e2129;
        --text-primary: #fafafa;
        --text-secondary: #a3a8b4;
        --border: #2e3239;
        --danger: #ff4b4b;
        --success: #21c354;
        --warning: #ffaa00;
    }

    /* --- Global --- */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    div[data-testid="stToolbar"] {visibility: hidden; height: 0; position: fixed;}
    div[data-testid="stDecoration"] {visibility: hidden; height: 0; position: fixed;}
    div[data-testid="stStatusWidget"] {visibility: hidden; height: 0; position: fixed;}
    #MainMenu {visibility: hidden; height: 0;}
    header {visibility: hidden; height: 0;}
    footer {visibility: hidden; height: 0;}

    .stApp {
        background: linear-gradient(135deg, #0e1117 0%, #1a1d24 50%, #0e1117 100%);
    }

    /* --- Headings --- */
    h1 { color: var(--accent-light) !important; font-weight: 700 !important; }
    h2 { color: var(--text-primary) !important; font-weight: 600 !important; }
    h3 { color: var(--text-primary) !important; font-weight: 600 !important; }

    /* --- Page header --- */
    .page-header {
        text-align: center;
        padding: 0.5rem 0 1.2rem 0;
    }
    .page-header h2 {
        margin: 0;
        font-size: 1.8rem;
        background: linear-gradient(90deg, var(--accent-light), var(--accent));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .page-header p {
        color: var(--text-secondary);
        font-size: 0.95rem;
        margin-top: 0.3rem;
    }

    /* --- Feature cards --- */
    .feature-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 1.4rem;
        margin-bottom: 0.8rem;
        transition: border-color 0.2s ease, box-shadow 0.2s ease, transform 0.15s ease;
    }
    .feature-card:hover {
        border-color: var(--accent);
        box-shadow: 0 0 24px rgba(15, 155, 142, 0.12);
        transform: translateY(-2px);
    }
    .feature-card h3 {
        margin-top: 0 !important;
        font-size: 1.1rem !important;
    }
    .feature-card-icon {
        font-size: 1.8rem;
        margin-bottom: 0.4rem;
    }

    /* --- Result cards --- */
    .result-card {
        background: var(--bg-card);
        border-radius: 12px;
        padding: 1.5rem 2rem;
        margin: 0.8rem 0;
        text-align: center;
        border: 1px solid var(--border);
    }
    .result-card.positive { border-left: 4px solid var(--danger); }
    .result-card.negative { border-left: 4px solid var(--success); }
    .result-card .result-label {
        color: var(--text-secondary);
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-bottom: 0.25rem;
    }
    .result-card .result-value {
        font-size: 1.5rem;
        font-weight: 700;
    }
    .result-card .result-value.danger { color: var(--danger); }
    .result-card .result-value.success { color: var(--success); }

    /* --- History items --- */
    .history-item {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 8px;
        padding: 0.7rem 1rem;
        margin-bottom: 0.4rem;
        transition: border-color 0.15s ease;
    }
    .history-item:hover {
        border-color: var(--accent);
    }
    .history-badge {
        display: inline-block;
        padding: 0.15rem 0.5rem;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .history-badge.danger {
        background: rgba(255, 75, 75, 0.15);
        color: var(--danger);
    }
    .history-badge.success {
        background: rgba(33, 195, 84, 0.15);
        color: var(--success);
    }
    .history-badge.warning {
        background: rgba(255, 170, 0, 0.15);
        color: var(--warning);
    }

    /* --- Info box --- */
    .info-box {
        background: rgba(15, 155, 142, 0.08);
        border: 1px solid rgba(15, 155, 142, 0.25);
        border-radius: 8px;
        padding: 0.8rem 1rem;
        color: var(--text-secondary);
        font-size: 0.88rem;
        margin-bottom: 1rem;
    }

    /* --- Disclaimer --- */
    .disclaimer {
        background: rgba(255, 170, 0, 0.06);
        border: 1px solid rgba(255, 170, 0, 0.2);
        border-radius: 8px;
        padding: 0.8rem 1rem;
        color: var(--warning);
        font-size: 0.82rem;
    }

    /* --- Sidebar --- */
    section[data-testid="stSidebar"] {
        background-color: var(--bg-secondary);
    }
    section[data-testid="stSidebar"] .stMarkdown p {
        color: var(--text-secondary);
        font-size: 0.85rem;
    }

    /* --- Divider --- */
    hr {
        border-color: var(--border) !important;
        opacity: 0.5;
    }

    /* --- Tabs --- */
    .stTabs [data-baseweb="tab-list"] { gap: 0; }
    .stTabs [data-baseweb="tab"] {
        padding: 0.6rem 1.5rem;
        font-weight: 500;
    }

    /* --- Form submit button --- */
    .stFormSubmitButton > button {
        background: linear-gradient(90deg, var(--accent), var(--accent-dark));
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: opacity 0.2s ease, transform 0.1s ease;
    }
    .stFormSubmitButton > button:hover {
        opacity: 0.9;
    }
    .stFormSubmitButton > button:active {
        transform: scale(0.98);
    }

    /* --- Regular buttons --- */
    .stButton > button {
        border-radius: 8px;
        font-weight: 500;
        transition: opacity 0.2s ease, transform 0.1s ease;
    }
    .stButton > button:hover {
        opacity: 0.9;
    }
    .stButton > button:active {
        transform: scale(0.98);
    }

    /* --- Selectbox / Radio labels --- */
    .stRadio label, .stSelectbox label {
        font-weight: 500;
    }

    /* --- Expander --- */
    .streamlit-expanderHeader {
        font-weight: 600;
    }

    /* --- Progress bar text --- */
    .stProgress [data-testid="stMarkdownContainer"] {
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    sc1, sc2, sc3 = st.columns([1, 2, 1])
    with sc2:
        st.image("assets/logo.svg", width=72)
    st.markdown("### HealthPulse")
    st.caption("AI-Powered Health Screening")
    st.divider()

    if st.session_state.get("history"):
        count = len(st.session_state.history)
        st.markdown(f"**{count}** prediction{'s' if count != 1 else ''} this session")

    st.divider()
    st.caption("For educational purposes only. Not a medical device.")
    st.caption("Built with Streamlit | v3.1")

pages = {
    "": [
        st.Page("pages/home.py", title="Home", icon="🏠", default=True),
    ],
    "Predictions": [
        st.Page("pages/heart.py", title="Heart Disease", icon="🫀"),
        st.Page("pages/pneumonia.py", title="Pneumonia", icon="🔬"),
        st.Page("pages/skin.py", title="Skin Cancer", icon="🩺"),
        st.Page("pages/multidisease.py", title="Multidisease", icon="📋"),
    ],
}

pg = st.navigation(pages, position="top")
pg.run()
