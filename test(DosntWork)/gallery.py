import streamlit as st
from test1.headfooter import render_header, render_footer

st.set_page_config(page_title="Rally City - Gallery")

with open("assets/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

render_header("gallery")

st.markdown("""
<main class="container">
  <h1>Event Gallery</h1>
  <p class="lead">A selection of moments from past rallies — from action shots to community highlights.</p>

  <section class="gallery-grid" aria-live="polite">
    <figure>
      <img src="https://images.unsplash.com/photo-1534081333815-ae5019106622?auto=format&fit=crop&w=400&q=80" alt="Rally car on a turn" loading="lazy">
      <figcaption>Competitor taking a tight corner</figcaption>
    </figure>
    <figure>
      <img src="https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=400&q=80" alt="Crowd watching cars" loading="lazy">
      <figcaption>A competitor drifting</figcaption>
    </figure>
    <figure>
      <img src="https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&q=80" alt="Vintage car on display" loading="lazy">
      <figcaption>Vintage class display</figcaption>
    </figure>
  </section>
</main>
""", unsafe_allow_html=True)

render_footer()
