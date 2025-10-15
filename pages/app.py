import re
import csv
from pathlib import Path
import streamlit as st

DATA_FILE = Path('submissions.csv')

st.set_page_config(page_title='Rally City - Apply', layout='centered')
st.title('Participant Application — Rally City')
st.write('Fill out the form to apply to participate. Fields marked with * are required.')


def valid_phone(p: str) -> bool:
    """Return True for empty or valid phone pattern."""
    return not p or re.match(r'^\+?[0-9\-\s]{7,20}$', p) is not None


with st.form('application_form'):
    full_name = st.text_input('Full name *')
    email = st.text_input('Email *')
    phone = st.text_input('Phone')

    vehicle = st.text_input('Vehicle make & model *')
    category = st.selectbox('Category *', ('', 'Novice', 'Experienced', 'Vintage'))

    emergency_name = st.text_input('Emergency contact name *')
    emergency_phone = st.text_input('Emergency contact phone *')

    submitted = st.form_submit_button('Submit application')


if submitted:
    errors = []
    if not full_name or len(full_name.strip()) < 2:
        errors.append('Full name must be at least 2 characters.')
    if not email or '@' not in email:
        errors.append('A valid email is required.')
    if not vehicle:
        errors.append('Vehicle make & model is required.')
    if not category:
        errors.append('Please choose a category.')
    if not emergency_name:
        errors.append('Emergency contact name is required.')
    if not valid_phone(emergency_phone):
        errors.append('A valid emergency contact phone is required.')
    if phone and not valid_phone(phone):
        errors.append('Phone number format is invalid.')

    if errors:
        for err in errors:
            st.error(err)
    else:
        st.success('Thank you! Your application has been submitted (simulated).')
        st.info('A confirmation would be sent by email in a real system.')

        # Append to CSV (simple simulated persistence)
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        header = ['full_name', 'email', 'phone', 'vehicle', 'category', 'emergency_name', 'emergency_phone']
        write_header = not DATA_FILE.exists()
        with DATA_FILE.open('a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if write_header:
                writer.writerow(header)
            writer.writerow([full_name, email, phone, vehicle, category, emergency_name, emergency_phone])

        st.session_state['last_submission'] = {
            'full_name': full_name,
            'email': email,
            'vehicle': vehicle,
            'category': category,
        }


if 'last_submission' in st.session_state:
    with st.expander('Last submission (simulated)'):
        st.json(st.session_state['last_submission'])
