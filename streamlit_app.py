import streamlit as st
import skin as s
import pneumonia as p
import multidisease as m
import heart as h

st.set_page_config(page_title="WBDPRS", page_icon="🤖", layout="wide")

st.markdown("<h1 style='text-align:center;color:#004d40;'>Web-based Disease Prediction System</h1>", unsafe_allow_html=True)
st.write("---")

tab1, tab2, tab3, tab4 = st.tabs(["Skin Cancer", "Pneumonia", "Multidisease", "Heart Disease"])

with tab1:
    s.skin()

with tab2:
    p.pneumonia()

with tab3:
    m.multidisease()

with tab4:
    h.heart()
