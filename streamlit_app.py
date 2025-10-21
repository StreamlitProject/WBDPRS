import streamlit as st
import heart as h
import multidisease as m
import pneumonia as p
import skin as s

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="WBDPRS",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- Sidebar --------------------
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Medical_icon.svg/512px-Medical_icon.svg.png", width=100)
    st.title("WBDPRS")
    st.markdown("### Web-based Disease Prediction System")
    st.markdown("---")
    st.markdown("**Info:**")
    st.info("""
    - Predict **Heart Disease**, **Pneumonia**, **Skin Cancer**, or **Multidisease**.
    - Approximate results, for educational purposes only.
    - Use healthy habits & consult a doctor for any concern.
    """)

    # Dark/light toggle
    theme_choice = st.radio("Theme:", ["Light", "Dark"])
    if theme_choice == "Dark":
        st.markdown("""
        <style>
        .stApp { background-color: #262730; color: #fafafa; }
        </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <style>
        .stApp { background-color: #fafafa; color: #262730; }
        </style>
        """, unsafe_allow_html=True)

# -------------------- Custom CSS --------------------
st.markdown("""
<style>
h1, h2 {
    text-align: center; 
    color: #0a9396;
    text-shadow: 1px 1px 2px #fff;
}
.stTabs [role="tab"] {
    font-weight: bold;
    font-size: 16px;
    color: #262730;
}
.stTabs [role="tab"][aria-selected="true"] {
    color: white;
    background-color: #0a9396;
    border-radius: 10px;
}
.stButton>button {
    border-radius: 10px;
    font-weight: bold;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #6cdacf;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -------------------- App Title --------------------
st.title("🤖 Web-based Disease Prediction System")
st.markdown("---")

# -------------------- Dashboard Cards --------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🩺 Skin Cancer"):
        st.session_state['page'] = 'Skin Cancer'

with col2:
    if st.button("🫁 Pneumonia"):
        st.session_state['page'] = 'Pneumonia'

with col3:
    if st.button("💊 Multidisease"):
        st.session_state['page'] = 'Multidisease'

with col4:
    if st.button("❤️ Heart Disease"):
        st.session_state['page'] = 'Heart Disease'

# -------------------- Load Selected Page --------------------
page = st.session_state.get('page', 'Skin Cancer')

st.markdown(f"<h2 style='text-align:center'><u>{page}</u></h2>", unsafe_allow_html=True)

if page == "Skin Cancer":
    s.skin()
elif page == "Pneumonia":
    p.pneumonia()
elif page == "Multidisease":
    m.multidisease()
elif page == "Heart Disease":
    h.heart()
