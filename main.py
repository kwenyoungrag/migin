import streamlit as st
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()


st.title('인공지능시인')

co = st.text_input('시의 주제를 제시해주세요')


if st.button('시작성 요청하기'):
    with st.spinner('시 작성중...'):
        result = llm.invoke(co + "에 대한 시를 써줘")
        st.write(result)


