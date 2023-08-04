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
