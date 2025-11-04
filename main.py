import streamlit as st
st.title('웹 만들기')
name=st.text_input('이름')
st.selectbox('좋아하는 음식은 뭔가요',['고기','채소'])
if st.button('인사말'):
  st.write(name+'안녕하신가')
