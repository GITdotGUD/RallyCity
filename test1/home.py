# Home.py
import streamlit as st
from test1.headfooter import render_header, render_footer

st.set_page_config(page_title="Rally City - Home")

# Include CSS from assets
with open("assets/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

render_header("home")

st.markdown("""
<main class="container">
  <section class="hero">
    <h1>Rally City Community Rally</h1>
    <p class="lead">Join us for a weekend of speed, skill, and community fun. Open to cars, bikes, and vintage vehicles.</p>
    <p>
      <a href="/Apply" class="btn">Apply to Participate</a>
      <a href="/Gallery" class="btn btn-outline">View Gallery</a>
    </p>
  </section>

  <section class="about">
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

  <section class="highlights">
    <h2>Event Highlights</h2>
    <ul>
      <li>Professional marshals & safety teams</li>
      <li>Prizes for category winners</li>
      <li>Food trucks and live music</li>
    </ul>
  </section>
</main>
""", unsafe_allow_html=True)

render_footer()
