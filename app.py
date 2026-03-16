from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

import os

# 1. Load API Key
api_key = os.getenv("GOOGLE_API_KEY")

# 2. Check if API Key exists
if not api_key:
    st.error("⚠️ GOOGLE_API_KEY is missing! Please add it to your Streamlit Secrets or .env file.")
    st.stop()

# 3. Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

st.title("🤖 AskBuddy - AI qnA Bot")
st.markdown("My QnA Bot with Langchain and Google Gemini !")

# session_state is a backend memory of stremalit

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state.messages:
    role =message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)


query = st.chat_input()
if query:
    st.session_state.messages.append({"role":"user","content":query})
    st.chat_message("user").markdown(query)
    try:
        res = llm.invoke(query)
        st.chat_message("assistant").markdown(res.content)
        st.session_state.messages.append({"role":"assistant","content":res.content})
    except Exception as e:
        st.error(f"❌ AI Error: {str(e)}")
        st.info("Check if your API Key is valid and if you have exceeded your quota on Google AI Studio.")

