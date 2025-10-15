import streamlit as st
from test1.headfooter import render_header, render_footer

st.set_page_config(page_title="Rally City - Apply")

with open("assets/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

render_header("apply")

st.markdown("<main class='container'>", unsafe_allow_html=True)
st.markdown("<h1>Participant Application</h1>", unsafe_allow_html=True)
st.markdown("<p class='lead'>Fill out the form below to apply to participate. Fields marked with * are required.</p>", unsafe_allow_html=True)

with st.form("application_form"):
    full_name = st.text_input("Full name *", help="Enter your full name", max_chars=50)
    email = st.text_input("Email *", help="Enter a valid email address")
    phone = st.text_input("Phone", help="Format: +1 555-555-5555 (optional)")
    vehicle = st.text_input("Vehicle make & model *", max_chars=50)
    category = st.selectbox("Category *", ["", "Novice", "Experienced", "Vintage"])
    emergency_name = st.text_input("Emergency contact name *", max_chars=50)
    emergency_phone = st.text_input("Emergency contact phone *", help="Format: +1 555-555-5555")
    submitted = st.form_submit_button("Submit application")

if submitted:
    # Basic validation
    if not full_name or len(full_name) < 2:
        st.error("Please enter a valid full name (at least 2 characters).")
    elif not email or "@" not in email:
        st.error("Please enter a valid email address.")
    elif not vehicle:
        st.error("Vehicle make & model is required.")
    elif category == "":
        st.error("Please select a category.")
    elif not emergency_name:
        st.error("Emergency contact name is required.")
    elif not emergency_phone:
        st.error("Emergency contact phone is required.")
    else:
        # Here you could save the data or send email, etc.
        st.success("Thank you! Your application has been submitted.")
        # Optionally clear the form or disable inputs after submit

st.markdown("</main>", unsafe_allow_html=True)

render_footer()
