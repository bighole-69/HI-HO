import streamlit as st
st.title('웹 만들기')
name=st.text_input('이름')
menu=st.selectbox('좋아하는 음식은 뭔가요',['고기','채소'])
if st.button('인사말'):
  st.info(name+'안녕하신가')
  st.warning(menu+'를 좋아하나보군요, 저도 좋아합니다')
