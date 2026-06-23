import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Happy Birthday Brother 🎂",
    page_icon="🎂",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.big-title {
    text-align: center;
    color: #ff4b4b;
    font-size: 50px;
    font-weight: bold;
}

.message {
    text-align: center;
    font-size: 22px;
    line-height: 1.8;
    padding: 20px;
}

.footer {
    text-align: center;
    padding-top: 30px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# Balloons
st.balloons()

# Title
st.markdown(
    '<p class="big-title">🎉 Happy Birthday Brother! 🎉</p>',
    unsafe_allow_html=True
)

# Birthday Message
st.markdown("""
<div class="message">
Wishing you a day filled with happiness, success, and unforgettable memories. ❤️<br><br>

You have always been my biggest supporter, guide, and inspiration.<br><br>

So today, I wanted to give you something special that I built with love. 🎁
</div>
""", unsafe_allow_html=True)

st.divider()

# Gift Section
st.subheader("🎁 Your Special Birthday Gift")

st.success("A surprise gift is waiting for you!")

# Portfolio Button
st.link_button(
    "🎁 Open Your Gift",
    "https://balam-lovaraju-portfolio.onrender.com"
)

st.divider()

st.markdown(
    """
    <div class="footer">
        <h3>Made with ❤️ by Your Loving Sister</h3>
    </div>
    """,
    unsafe_allow_html=True
)
