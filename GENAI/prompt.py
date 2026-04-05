import streamlit as st
from model import llm
from langchain_core.messages import HumanMessage

st.header('📝 Text Summarizer')

userinput = st.text_area("Enter text to summarize:")

if st.button("Summarize"):
    if userinput.strip() == "":
        st.warning("Please enter some text!")
    else:
        prompt = f"Summarize the following text:\n{userinput}"

        result = llm.invoke([
            HumanMessage(content=prompt)
        ])

        st.subheader("Summary:")
        st.write(result.content)