from Custom import Custom
from Custom2 import Custom2
import streamlit as st
import os

# 실행: streamlit run chatting.py

def chat_page(name, set, line, situation, sit_line):
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": sit_line}]
    
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    
    custom = Custom2(name=name, set=set, line=line, situation=situation)
    
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            assistant_response = custom.receive_chat(prompt)

            message_placeholder.write(assistant_response)
        
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})


def main():
    os.environ["OPENAI_API_KEY"] = st.secrets["openai_key"]
    
    st.subheader("캐릭터를 생성해서 대화해 보세요!")
    
    st.sidebar.title("캐릭터 세팅")
    
    name = st.sidebar.text_input("캐릭터 이름")
    set = st.sidebar.text_input("캐릭터 설정(예: 똑똑함 / 고등학생임 / 공부를 잘함)")
    line = st.sidebar.text_input("캐릭터 말투 예시(예: 안녕 / 난 누구야 / 어쩌고)")
    situation = st.sidebar.text_input("캐릭터와 대화할 상황(예: 00이 00인 나와 대화하는 상황)")
    sit_line = st.sidebar.text_input("캐릭터의 첫 마디(챗봇이 말할 첫 마디 지정)")
    
    if name and set and line and situation and sit_line:
        chat_page(name=name, set=set, line=line, situation=situation, sit_line=sit_line)
    

if __name__ == "__main__":
    main()
            
        
    
    
        