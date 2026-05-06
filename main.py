
import streamlit as st
from llm import get_chain



st.title("🔬 Graph RAG Chat")

if "chain" not in st.session_state:
    st.session_state.chain = get_chain()

if "messages" not in st.session_state:
    st.session_state.messages = []

# display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# input
if question := st.chat_input("Ask about the database..."):
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = st.session_state.chain.invoke({"query": question})
            answer = result["result"]
        st.write(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})