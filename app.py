"""
# My first app
"""

import streamlit as st

"""
---
"""

st.title('Welcome To Streamlit Quickstart!')

st.divider()

st.subheader('1. Text')
st.write('Hello, World!')
code = '''st.write('Hello, World!')'''
st.code(code, language='python')

st.divider()

st.subheader('2. Text With Italics')
st.write('Hello, *World!*')
code = '''st.write('Hello, *World!*')'''
st.code(code, language='python')

st.divider()

st.subheader('3. Text With Emojis')
st.write('Hello, *World!* :sunglasses:')
code = '''st.write('Hello, *World!* :sunglasses:')'''
st.code(code, language='python')

st.divider()

st.subheader('4. Text With Bolding')
st.markdown('Streamlit is **_really_ cool**.')
code = '''st.markdown('Streamlit is **_really_ cool**.')'''
st.code(code, language='python')

st.divider()

st.subheader('5. Text With Color')
st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
code = '''st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")'''
st.code(code, language='python')

st.divider()

st.subheader('6. Text With Equations')
st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")
code = '''st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")'''
st.code(code, language='python')

st.divider()
st.divider()
