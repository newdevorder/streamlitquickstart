"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st

st.write('Hello, World!')
code = '''st.write('Hello, World!')'''
st.code(code, language='python')


st.write('Hello, *World!*')
code = '''st.write('Hello, *World!*')'''
st.code(code, language='python')


st.write('Hello, *World!* :sunglasses:')
code = '''st.write('Hello, *World!* :sunglasses:')'''
st.code(code, language='python')

st.markdown('Streamlit is **_really_ cool**.')
code = '''st.markdown('Streamlit is **_really_ cool**.')'''
st.code(code, language='python')


st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")
code = '''st.markdown("This text is :red[colored red], and this is **:blue[colored]** and bold.")'''
st.code(code, language='python')

st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")
code = '''st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :pencil:")'''
st.code(code, language='python')










