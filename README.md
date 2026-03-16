# 🤖 AI-Buddy ChatBot (qna-bot)

A simple and interactive AI-powered ChatBot built using **Streamlit**, **Langchain**, and **Google Gemini (AI model)**. This bot allows users to ask questions and get intelligent responses in real-time.

## 🚀 Features
- **Real-time Interaction:** Chat with the AI in a user-friendly interface.
- **Powered by Gemini:** Uses Google's `gemini-1.5-flash` model for fast and accurate answers.
- **Message History:** Keeps track of your conversation within the session.
- **Sleek UI:** Built with Streamlit for a clean and minimalist student project look.

## 🛠️ Tech Stack
- **Frontend:** Streamlit
- **AI Framework:** Langchain
- **LLM:** Google Gemini AI
- **Environment Management:** Dotenv

---

## 🧠 End-to-End Code Explanation (Streamlit Functions)

This project heavily relies on **Streamlit** to create the web interface. Here is a breakdown of the functions used:

### 1. Header & Interface
- **`st.title("🤖 AskBuddy")`**: Sets the main heading of the web page.
- **`st.markdown(...)`**: Used for the subtitle and descriptions. It supports Markdown formatting (bold, links, etc.).

### 2. State Management (Memory)
- **`st.session_state`**: This is critical. Streamlit reruns the entire script every time a user interacts with a widget. We use `st.session_state["messages"]` to store the chat history so that the messages don't disappear when the page reloads.
  - *Code snippet:* `if "messages" not in st.session_state: st.session_state["messages"] = []`

### 3. Displaying the Chat
- **`st.chat_message("role")`**: Creates a visual message box. We loop through the `session_state.messages` and use this to display previous chats.
  - `role="user"`: Shows a user icon.
  - `role="assistant"`: Shows the AI icon.

### 4. Handling Input
- **`st.chat_input()`**: Displays a sleek chat bar at the bottom. It waits for the user to type something and press Enter.
- **The Input Logic**: 
  1. When a `query` is entered, we append it to our "memory" (`session_state`).
  2. We immediately display the user's message using `st.chat_message`.
  3. We call the AI (`llm.invoke`) to get a response.
  4. We display the AI's response and save it to the memory as well.

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/RohitKModi777/AI-Buddy_ChatBot_Using_streamlit.git
cd AI-Buddy_ChatBot_Using_streamlit
```

### 2. Install dependencies
Make sure you have Python installed. Then run:
```bash
pip install -r requirements.txt
```

### 3. Set up your API Key
Create a `.env` file in the root directory and add your Google API Key:
```env
GOOGLE_API_KEY=your_api_key_here
```

### 4. Run the app
```bash
streamlit run app.py
```

## 🌐 Deployment

### Deploying on Streamlit Cloud (Recommended)
1. Push your code to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io/).
3. Connect your repo and deploy!

---
**Made with ❤️ as a student project.**
