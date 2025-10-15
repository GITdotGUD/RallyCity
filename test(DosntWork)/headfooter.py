import streamlit as st
import datetime

def render_header(current_page):
    st.markdown(f"""
    <header class="site-header">
      <div class="container header-inner">
        <a href="/" class="brand">Rally City</a>
        <nav class="main-nav">
          <ul>
            <li><a href="/" {'aria-current="page"' if current_page=='home' else ''}>Home</a></li>
            <li><a href="/Gallery" {'aria-current="page"' if current_page=='gallery' else ''}>Gallery</a></li>
            <li><a href="/Apply" {'aria-current="page"' if current_page=='apply' else ''}>Apply</a></li>
          </ul>
        </nav>
      </div>
    </header>
    """, unsafe_allow_html=True)

def render_footer():
    current_year = datetime.datetime.now().year
    st.markdown(f"""
    <footer class="site-footer">
      <div class="container footer-inner">
        <p>&copy; {current_year} Rally City. All rights reserved.</p>
      </div>
    </footer>
    """, unsafe_allow_html=True)
