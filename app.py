import streamlit as st
import streamlit.components.v1 as components

# Page Configuration
st.set_page_config(
    page_title="Happy Birthday Brother",
    page_icon="🎂",
    layout="centered"
)

# Custom Styling
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
    padding: 20px;
}
.gift-box {
    text-align: center;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

# Balloons
st.balloons()

# Header
st.markdown('<p class="big-title">🎉 Happy Birthday Brother! 🎉</p>', unsafe_allow_html=True)

# Message
st.markdown("""
<div class="message">
Wishing you a day filled with happiness, success, and lots of unforgettable memories. ❤️<br><br>

You have always been my biggest supporter, guide, and inspiration.<br>
Today, I wanted to give you something special that I built with love. 🎁
</div>
""", unsafe_allow_html=True)

st.divider()

# Gift Section
st.markdown('<div class="gift-box">', unsafe_allow_html=True)

if st.button("🎁 Open Your Birthday Gift"):
    
    st.success("Surprise! I created a special portfolio website just for you.")
    
    portfolio_link = "https://balam-lovaraju-portfolio.onrender.com"
    
    st.markdown(
        f"""
        ### 🎉 Your Gift is Ready!
        
        Click below to explore:
        
        **🔗 [Visit Your Portfolio]({portfolio_link})**
        """
    )

    st.balloons()

st.markdown('</div>', unsafe_allow_html=True)

st.divider()

st.markdown(
    """
    <center>
    <h3>Made with ❤️ by Your Loving Sister</h3>
    </center>
    """,
    unsafe_allow_html=True
)
