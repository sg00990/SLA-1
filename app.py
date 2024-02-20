import streamlit as st
import datetime
import json

st.set_page_config(
    page_title="Tier 1 SLA Questionnaire",
    page_icon="💻",
    layout="wide"
)

conn = st.connection("snowflake")

st.markdown('<p style="font-family:sans-serif; color:#324a62; font-size: 28px; font-weight: bold">Tier 1 SLA Questionnaire</p>', unsafe_allow_html=True)
st.write("###")

st.markdown('<p style="font-family:sans-serif; color:#87c440; font-size: 20px; font-weight: bold">SLA 1</p>', unsafe_allow_html=True)

st.write("**Availability of Help Desk**")
help_desk = st.text_area("help_desk", label_visibility="collapsed")
help_desk = help_desk.replace("\n", "  ").replace("'", "''").replace('"', r'\"')
st.write("**Did your team experience an outage this past week?**")
experienced_outage = st.radio("experienced_outage", options=["No", "Yes"], label_visibility="collapsed")

outage_start_datetime = None
outage_end_datetime = None
reason = None

if experienced_outage == "Yes":

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

    outage_start_datetime = datetime.datetime.combine(outage_start, outage_start_time)
    outage_end_datetime = datetime.datetime.combine(outage_end, outage_end_time)

    st.write("**Outage Reason**")
    reason = st.text_area("reason", label_visibility="collapsed")
    reason = reason.replace("\n", "  ").replace("'", "''").replace('"', r'\"')


col1, col2, col3 = st.columns(3)

with col3:
    if st.button("Submit", use_container_width=True):
        data = {
            "sla_1_helpdesk_availability": help_desk,
            "sla_1_experienced_outage": experienced_outage,
            "sla_1_outage_start": outage_start_datetime,
            "sla_1_outage_end": outage_end_datetime,
            "sla_1_outage_reason": reason
        }

        json_data = json.dumps(data, indent=4, sort_keys=True, default=str)

        date_submitted = datetime.datetime.now()

        try:
            conn.query(f""" INSERT INTO sla_tier_1_questionnaire (type, date_submitted, json_data) SELECT 'SLA 1', '{date_submitted}', (parse_json('{json_data}'))""")
        except:
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


