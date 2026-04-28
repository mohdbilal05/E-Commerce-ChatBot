# 🛍️ E-Commerce Assistant Chatbot

An AI-powered e-commerce chatbot that intelligently routes customer queries using **Semantic Router** — answering policy and FAQ questions via RAG (ChromaDB + Groq LLM), and product queries via natural language to SQL.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://e-commerce-assistant-bot.streamlit.app/)

---

## 🚀 Live Demo

👉 **[https://e-commerce-assistant-bot.streamlit.app/](https://e-commerce-assistant-bot.streamlit.app/)**

---

## ✨ Features

- **Semantic Routing** — automatically classifies user queries into FAQ or product search
- **RAG-based FAQ** — retrieves relevant answers from a CSV knowledge base using ChromaDB vector search
- **Natural Language to SQL** — converts product queries into SQL and fetches results from a database
- **Groq LLM** — fast inference using `llama-3.3-70b-versatile` for answer generation
- **Streamlit UI** — clean, interactive chat interface with example prompts

---

## 🧠 How It Works

```
User Query
    │
    ▼
Semantic Router (sentence-transformers)
    │
    ├── FAQ Route ──► ChromaDB Vector Search ──► Groq LLM ──► Answer
    │
    └── SQL Route ──► NL-to-SQL ──► Database Query ──► Answer
```

1. The user submits a query via the chat interface
2. **Semantic Router** classifies the query as either `faq` or `sql`
3. **FAQ queries** are matched against a ChromaDB collection of questions/answers, and the top results are passed to Groq to generate a grounded response
4. **SQL queries** are converted to database queries to search products by price, brand, size, discount, etc.

---

## 🗂️ Project Structure

```
e-commerce-chatbot/
├── app/
│   ├── main.py          # Streamlit UI entry point
│   ├── router.py        # Semantic Router setup with FAQ & SQL routes
│   ├── faq.py           # ChromaDB ingestion + RAG chain
│   ├── sql.py           # Natural language to SQL chain
│   └── resources/
│       └── faq_data.csv # FAQ knowledge base
├── requirements.txt
├── .python-version
└── .env                 # Local secrets (not committed)
```

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| UI | Streamlit |
| Semantic Routing | semantic-router |
| Embeddings | sentence-transformers (`all-MiniLM-L6-v2`) |
| Vector Store | ChromaDB |
| LLM | Groq (`llama-3.3-70b-versatile`) |
| Data | pandas |

---

## ⚙️ Local Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/e-commerce-chatbot.git
cd e-commerce-chatbot
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

Get your free Groq API key at [console.groq.com](https://console.groq.com)

### 5. Run the app
```bash
streamlit run app/main.py
```

---

## 💬 Example Queries

**FAQ / Policy questions:**
- *"What is your return policy?"*
- *"What payment methods are accepted?"*
- *"How do I use a promo code?"*

**Product search:**
- *"Nike shoes with 50% discount"*
- *"Formal shoes in size 9 under Rs. 3000"*
- *"Are there any Puma shoes on sale?"*

---

## ☁️ Deploying to Streamlit Cloud

1. Push your code to a public GitHub repository
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo
3. Set **Main file path** to `app/main.py`
4. Add your secrets under **Settings → Secrets**:
```toml
GROQ_API_KEY = "your_groq_api_key_here"
GROQ_MODEL = "llama-3.3-70b-versatile"
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
