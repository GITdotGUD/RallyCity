import streamlit as st
import re
from datetime import datetime

st.set_page_config(page_title="Apply - Rally City", layout="centered")

# Header
st.markdown(
    """
    <style>
    .header {
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .nav {
        margin-bottom: 2rem;
    }
    .nav a {
        margin-right: 1.5rem;
        text-decoration: none;
        color: #0073e6;
        font-weight: 600;
    }
    .nav a.current {
        font-weight: bold;
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="header">Rally City</div>
    <nav class="nav">
        <a href="home.html">Home</a>
        <a href="gallery.html">Gallery</a>
        <a href="apply.html" class="current">Apply</a>
    </nav>
    """,
    unsafe_allow_html=True,
)

st.title("Participant Application")
st.write("Fill out the form below to apply to participate. Fields marked with * are required.")

with st.form("application_form"):
    st.subheader("Personal details")
    full_name = st.text_input("Full name *", placeholder="Jane Doe")
    email = st.text_input("Email *", placeholder="name@example.com")
    phone = st.text_input("Phone", placeholder="+1 555-555-5555")

    st.subheader("Vehicle & category")
    vehicle = st.text_input("Vehicle make & model *", placeholder="Ford Fiesta")
    category = st.selectbox(
        "Category *",
        options=["", "Novice", "Experienced", "Vintage"],
        index=0,
    )

    st.subheader("Emergency contact")
    emergency_name = st.text_input("Contact name *")
    emergency_phone = st.text_input("Contact phone *")

    submitted = st.form_submit_button("Submit application")
    reset = st.form_submit_button("Reset")

    if reset:
        st.experimental_rerun()

    if submitted:
        errors = []

        if not full_name or len(full_name) < 2:
            errors.append("Full name is required and must be at least 2 characters.")
        if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Valid email is required.")
        if phone and not re.match(r"^\+?[0-9\-\s]{7,20}$", phone):
            errors.append("Phone number format is invalid.")
        if not vehicle:
            errors.append("Vehicle make & model is required.")
        if not category:
            errors.append("Category is required.")
        if not emergency_name:
            errors.append("Emergency contact name is required.")
        if not emergency_phone or not re.match(r"^\+?[0-9\-\s]{7,20}$", emergency_phone):
            errors.append("Valid emergency contact phone is required.")

        if errors:
            for err in errors:
                st.error(err)
        else:
            st.success("Application submitted successfully!")
            st.write("### Submitted details:")
            st.write(f"**Full name:** {full_name}")
            st.write(f"**Email:** {email}")
            st.write(f"**Phone:** {phone or 'N/A'}")
            st.write(f"**Vehicle:** {vehicle}")
            st.write(f"**Category:** {category}")
            st.write(f"**Emergency contact name:** {emergency_name}")
            st.write(f"**Emergency contact phone:** {emergency_phone}")

# Footer with current year
current_year = datetime.now().year
st.markdown(f"<footer style='margin-top:3rem; text-align:center;'>© {current_year} Rally City.</footer>", unsafe_allow_html=True)
