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

    /* --- Section header on pages --- */
    .page-header {
        text-align: center;
        padding: 0.5rem 0 1.5rem 0;
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

    /* --- Cards --- */
    .feature-card {
        background: var(--bg-card);
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: border-color 0.2s, box-shadow 0.2s;
    }
    .feature-card:hover {
        border-color: var(--accent);
        box-shadow: 0 0 20px rgba(15, 155, 142, 0.15);
    }
    .feature-card h3 {
        margin-top: 0 !important;
        font-size: 1.15rem !important;
    }
    .feature-card-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }

    /* --- Result cards --- */
    .result-card {
        background: var(--bg-card);
        border-radius: 12px;
        padding: 1.5rem 2rem;
        margin: 1rem 0;
        text-align: center;
        border: 1px solid var(--border);
    }
    .result-card.positive {
        border-left: 4px solid var(--danger);
    }
    .result-card.negative {
        border-left: 4px solid var(--success);
    }
    .result-card .result-label {
        color: var(--text-secondary);
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.25rem;
    }
    .result-card .result-value {
        font-size: 1.6rem;
        font-weight: 700;
    }
    .result-card .result-value.danger { color: var(--danger); }
    .result-card .result-value.success { color: var(--success); }

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

    /* --- Form elements --- */
    .stRadio > div { gap: 0.4rem; }

    /* --- Divider override --- */
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

    /* --- Buttons --- */
    .stFormSubmitButton > button {
        background: linear-gradient(90deg, var(--accent), var(--accent-dark));
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: opacity 0.2s;
    }
    .stFormSubmitButton > button:hover {
        opacity: 0.9;
    }

    /* --- Pills --- */
    .stPills > div > div {
        gap: 0.4rem;
    }
    .stPills button {
        border-radius: 20px !important;
        padding: 0.4rem 1rem !important;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("assets/logo.svg", width=80)
    st.markdown("### HealthPulse")
    st.markdown("AI-Powered Health Screening Platform")
    st.divider()
    st.markdown("**Quick Navigation**")
    st.markdown("- 🏠 Home")
    st.markdown("- 🫀 Heart Disease")
    st.markdown("- 🔬 Pneumonia")
    st.markdown("- 🩺 Skin Cancer")
    st.markdown("- 📋 Multidisease")
    st.divider()
    if st.session_state.get("history"):
        st.markdown(f"**Session:** {len(st.session_state.history)} prediction(s)")
    st.divider()
    st.markdown(
        "<div class='disclaimer'>"
        "**Disclaimer:** This system is for educational purposes only. "
        "It is not a substitute for professional medical advice, diagnosis, or treatment. "
        "Always consult a qualified healthcare provider."
        "</div>",
        unsafe_allow_html=True,
    )
    st.divider()
    st.caption("Built with Streamlit | v3.0")

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

qp = st.query_params
if "feedback" in qp:
    rating = qp["feedback"]
    if "history" in st.session_state and st.session_state.history:
        st.session_state.history[-1]["Rating"] = f"{rating}/3"
        st.toast(f"Thanks for your feedback: {rating}/3", icon="⭐")

pg = st.navigation(pages, position="top")
pg.run()
