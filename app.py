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

st.divider()

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

st.divider()

code = '''prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")'''
st.code(code, language='python')

st.divider()


