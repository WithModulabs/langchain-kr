import streamlit as st
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
import os

# API 키를 환경변수로 관리하기 위한 설정 파일
from dotenv import load_dotenv

# API 키 정보 로드
load_dotenv()


def LangGraph_run():
    # Define the state for storing messages
    class State(TypedDict):
        messages: Annotated[list, add_messages]
    graph_builder = StateGraph(State)

    # session_state에 저장된 model_choice를 사용합니다.
    model_choice = st.session_state.get("model_choice", "OpenAI ChatGPT")
    if model_choice == "OpenAI ChatGPT":
        # OpenAI ChatGPT를 사용하는 코드
        llm = ChatOpenAI(
            model="gpt-4o-mini",
        )
    else:
        st.error("지원하지 않는 모델입니다.")
        return

    def chatbot(state: State):
        return {"messages": [llm.invoke(state["messages"])]}
    graph_builder.add_node("chatbot", chatbot)
    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_edge("chatbot", END)
    graph = graph_builder.compile()

    try:
        # Get the mermaid PNG as bytes
        graph_bytes = graph.get_graph().draw_mermaid_png()
        # 바이트를 이미지로 변환하고 Streamlit에 표시합니다.
        st.image(graph_bytes, caption="Chatbot Graph")

    except Exception as e:
        st.error(f"Failed to display graph: {e}")

    if "messages_01" not in st.session_state:
        st.session_state.messages_01 = []

    # 이전 메시지 모두 표시
    for message in st.session_state.messages_01:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    #  새로운 사용자 입력을 받아 처리합니다.    
    if prompt := st.chat_input("무엇을 원하세요?"):
        st.session_state.messages_01.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 모델에 보낼 전체 채팅 기록을 준비합니다.
        full_conversation = [(msg["role"], msg["content"]) for msg in st.session_state.messages_01]

        # 전체 대화 기록이 포함된 모델을 사용하여 응답 생성
        for event in graph.stream({"messages": full_conversation}):
            for value in event.values():
                # AIMessage 객체에서 직접 콘텐츠에 액세스                
                response = value["messages"][-1].content
                st.session_state.messages_01.append({"role": "assistant", "content": response})
                with st.chat_message("assistant"):
                    st.markdown(response)

def main():
    # Sidebar to reset session state
    st.title("LangGraph Chatbot!!")
    # API key가 제출된 경우 챗봇 실행
    LangGraph_run()

if __name__ == "__main__":
    main()