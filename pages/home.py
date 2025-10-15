import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Rally City - Community Car Rally", layout="centered")

# Header with navigation
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
    .btn {
        background-color: #0073e6;
        color: white;
        padding: 0.5rem 1rem;
        margin-right: 1rem;
        border-radius: 4px;
        text-decoration: none;
        font-weight: 600;
    }
    .btn-outline {
        background-color: transparent;
        border: 2px solid #0073e6;
        color: #0073e6;
        padding: 0.5rem 1rem;
        border-radius: 4px;
        text-decoration: none;
        font-weight: 600;
    }
    .container {
        max-width: 900px;
        margin: auto;
        padding: 0 1rem;
    }
    .hero {
        background-color: #e6f0ff;
        padding: 2rem 0;
        margin-bottom: 2rem;
        border-radius: 6px;
        text-align: center;
    }
    h1, h2, h3 {
        margin-bottom: 0.5rem;
    }
    p.lead {
        font-size: 1.25rem;
        margin-bottom: 1.5rem;
    }
    .grid {
        display: flex;
        gap: 2rem;
        margin-top: 1rem;
        margin-bottom: 2rem;
        flex-wrap: wrap;
    }
    .grid article {
        flex: 1 1 28%;
        min-width: 250px;
        background-color: #f9f9f9;
        padding: 1rem;
        border-radius: 6px;
        box-shadow: 0 0 8px rgb(0 0 0 / 0.1);
    }
    ul.highlights-list {
        list-style-type: disc;
        padding-left: 1.25rem;
    }
    footer {
        margin-top: 3rem;
        padding: 1rem 0;
        text-align: center;
        font-size: 0.9rem;
        color: #666;
        border-top: 1px solid #ccc;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header and Navigation
st.markdown(
    """
    <div class="container">
      <div class="header">Rally City</div>
      <nav class="nav">
        <a href="home.html" class="current">Home</a>
        <a href="gallery.html">Gallery</a>
        <a href="apply.html">Apply</a>
      </nav>
    </div>
    """,
    unsafe_allow_html=True,
)

# Hero section
st.markdown(
    """
    <section class="hero">
      <div class="container">
        <h1>Rally City Community Rally</h1>
        <p class="lead">Join us for a weekend of speed, skill, and community fun. Open to cars, bikes, and vintage vehicles.</p>
        <p>
          <a class="btn" href="apply.html">Apply to Participate</a>
          <a class="btn btn-outline" href="gallery.html">View Gallery</a>
        </p>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# About the Rally section
st.markdown(
    """
    <section class="about container">
      <h2>About the Rally</h2>
      <p>The Rally City event brings together drivers of all skill levels for a friendly timed rally through scenic routes. There will be categories for novices, experienced competitors, and a vintage class. Families are welcome — activities and food vendors will be on site.</p>

      <div class="grid">
        <article>
          <h3>When & Where</h3>
          <p>June 21-22, Rally Park and surrounding roads. Check-in starts at 7:00 AM on Saturday.</p>
        </article>
        <article>
          <h3>What to Expect</h3>
          <p>Timed stages, safety briefings, demonstrations, and a community car show. This event emphasizes safety and sportsmanship.</p>
        </article>
        <article>
          <h3>How to Join</h3>
          <p>Complete the application form with vehicle details and emergency contact information. Submissions are reviewed and confirmed by email.</p>
        </article>
      </div>
    </section>
    """,
    unsafe_allow_html=True,
)

# Event Highlights
st.markdown(
    """
    <section class="highlights container">
      <h2>Event Highlights</h2>
      <ul class="highlights-list">
        <li>Professional marshals & safety teams</li>
        <li>Prizes for category winners</li>
        <li>Food trucks and live music</li>
      </ul>
    </section>
    """,
    unsafe_allow_html=True,
)

# Footer with current year
current_year = datetime.now().year
st.markdown(
    f"""
    <footer>
      <div class="container footer-inner">
        &copy; {current_year} Rally City. All rights reserved.
      </div>
    </footer>
    """,
    unsafe_allow_html=True,
)
