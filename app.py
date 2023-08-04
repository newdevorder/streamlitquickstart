"""
# My first app
"""

import streamlit as st
from langchain.llms import OpenAI
from PIL import Image
"""
---
"""


st.title('Welcome To Streamlit Quickstart!')

image = Image.open('streamlit_logo.png')
st.image(image, caption='streamlit logo')
code = '''image = Image.open('streamlit_logo.png')
st.image(image, caption='streamlit logo')'''
st.code(code, language='python')

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

st.subheader('7. Text with LaTex')
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.divider()

st.subheader('8. Slider')
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')
code = '''age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')'''
st.code(code, language='python')

st.divider()

st.subheader('9. Text Input')
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)
code = '''title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)'''
st.code(code, language='python')

st.divider()

st.subheader('10. Camera Input')
picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)
code = '''picture = st.camera_input("Take a picture")
if picture:
    st.image(picture)'''
st.code(code, language='python')

st.divider()

st.subheader('BONUS: CHATGPT CHATBOT')

st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  llm = OpenAI(temperature=0.1, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)



code = '''st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  llm = OpenAI(temperature=0.1, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key ', icon='⚠', ' by clicking the arrow in the top left-hand corner of the screen')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)'''
st.code(code, language='python')
