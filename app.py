import streamlit as st
import time

st.set_page_config(
    page_title="Tier 2 SLA Questionnaire",
    page_icon="💻",
    layout="wide"
)

st.markdown('<p style="font-family:sans-serif; color:#324a62; font-size: 28px; font-weight: bold">Tier 2 SLA Questionnaire</p>', unsafe_allow_html=True)
st.write("###")

st.markdown('<p style="font-family:sans-serif; color:#87c440; font-size: 20px; font-weight: bold">SLA 1A/1B</p>', unsafe_allow_html=True)


st.write("**Did your team experience a Planned or Unplanned Outage this past week?**")
experienced_outage = st.radio("experienced_outage", options=["No", "Yes"], label_visibility="collapsed")

if experienced_outage == "Yes":
    st.write("**If yes, please answer the following**")
    workstream = st.selectbox("Workstream", options=["BP", "Impact", "LDAP", "Doc Center"])
    outage_planned = st.radio("Planned?", options=["No", "Yes"])

    col3, col4 = st.columns(2)

    with col3:
        outage_start = st.date_input(
            "Outage Start Date",
            format="MM/DD/YYYY"
        )
    with col4:
        outage_start_time = st.time_input("Outage Start Time", step=60)

    col5, col6 = st.columns(2)

    with col5:
        outage_end = st.date_input(
            "Outage End Date",
            format="MM/DD/YYYY",
        )
    with col6:
        outage_end_time = st.time_input("Outage End Time", step=60)

    outage_desc = st.text_area("Brief Description", key="outage_desc")


st.write("**Date**")
survey_date = st.date_input("survey_date", format="MM/DD/YYYY", label_visibility="collapsed")
st.write("**Additional Comments**")
survey_text = st.text_area("survey_text", label_visibility="collapsed")


col1, col2, col3 = st.columns(3)

with col3:
    if st.button("Submit", use_container_width=True):
        st.success("Thank you for your responses!")


col4, col5, col6 = st.columns([1, .5, 1])

with col4:
    st.write("##")
    st.image("img/blue_bar.png")
    
with col5:
    col17, col18, col19 = st.columns(3)
    with col18:
        st.write("######")
        st.image("img/moser_logo.png")
with col6:
    st.write("##")
    st.image("img/blue_bar.png")


