import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Gallery - Rally City", layout="centered")

# Header with navigation links
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
    .gallery-grid {
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
    }
    figure {
        margin: 0;
        width: 30%;
    }
    figcaption {
        text-align: center;
        font-style: italic;
        margin-top: 0.25rem;
    }
    img {
        width: 100%;
        border-radius: 4px;
    }
    footer {
        margin-top: 3rem;
        text-align: center;
        font-size: 0.9rem;
        color: #666;
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
        <a href="gallery.html" class="current">Gallery</a>
        <a href="apply.html">Apply</a>
    </nav>
    """,
    unsafe_allow_html=True,
)

st.title("Event Gallery")
st.write("A selection of moments from past rallies — from action shots to community highlights.")

# Images and captions data
images = [
    {
        "src": "https://images.unsplash.com/photo-1549924231-f129b911e442?auto=format&fit=crop&w=800&q=80",
        "alt": "Rally car on a turn",
        "caption": "Competitor taking a tight corner",
    },
    {
        "src": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=800&q=80",
        "alt": "Crowd watching cars",
        "caption": "A competitor drifting",
    },
    {
        "src": "https://images.unsplash.com/photo-1525609004556-c46c7d6cf023?auto=format&fit=crop&w=800&q=80",
        "alt": "Vintage car on display",
        "caption": "Vintage class display",
    },
]

# Render gallery
cols = st.columns(3)
for idx, img in enumerate(images):
    with cols[idx]:
        st.image(img["src"], caption=img["caption"], use_column_width=True, clamp=True, output_format="JPEG")

# Footer with current year and rights
current_year = datetime.now().year
st.markdown(
    f"""
    <footer>
      &copy; {current_year} Rally City. <br>
      <a href="https://unsplash.com/s/photos/rally-car" target="_blank" rel="noopener noreferrer">All rights reserved.</a>
    </footer>
    """,
    unsafe_allow_html=True,
)
