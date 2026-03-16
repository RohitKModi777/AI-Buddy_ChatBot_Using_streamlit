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

### Deploying on Vercel
*Note: Streamlit apps require a running server. For Vercel, you may need a wrapper or specialized configuration.*

---
**Made with ❤️ as a student project.**
