# 🧠 AI Journalist Agent

> 🚀 An AI-powered journalist that researches, writes, and edits high-quality articles automatically.

---

## 📸 Demo Screenshot

![App Screenshot](assets/screenshot.png)

---

## ✨ Features

* 🔍 Real-time web search using DuckDuckGo
* 🌐 Automatic content extraction from articles
* ✍️ AI-generated high-quality articles
* 📰 Professional editing and refinement
* 🧠 Catchy headline generation
* 🔗 Source transparency

---

## 🏗️ Architecture

This project follows a **multi-agent pipeline**:

1. **Searcher Agent** → Finds relevant links
2. **Scraper Tool** → Extracts content from web pages
3. **Writer Agent** → Generates article using AI
4. **Editor Agent** → Refines and improves article
5. **Headline Generator** → Creates engaging titles

---

## ⚙️ Tech Stack

* 🐍 Python
* 🖥️ Streamlit
* 🤖 Cohere API
* 🔍 DuckDuckGo Search
* 🌐 BeautifulSoup

---

## 📁 Project Structure

```
ai_journalist_agent/
│
├── app/
│   ├── main.py
│   ├── config.py
│   │
│   ├── agents/
│   │   ├── searcher.py
│   │   ├── writer.py
│   │   ├── editor.py
│   │
│   ├── tools/
│   │   ├── scraper.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/AI-Journalist-Agent.git
cd AI-Journalist-Agent/app
```

### 2️⃣ Install Dependencies

```bash
pip install -r ../requirements.txt
```

### 3️⃣ Add API Key

Create `.env` file:

```env
COHERE_API_KEY=your_api_key_here
```

### 4️⃣ Run the App

```bash
streamlit run main.py
```

---

## 🧪 Example Topic

```
Impact of Artificial Intelligence on Healthcare
```

---

## ⚠️ Important Notes

* Never commit `.env` file
* API keys must be kept secure
* Some websites may block scraping

---

## 🔥 Future Improvements

* 🧠 Fact-checking agent
* 📊 SEO optimization
* 🌍 Deployment (Streamlit Cloud)
* 📚 Memory with vector DB (FAISS)

---

## 💼 Use Cases

* Blog writing automation
* News article generation
* Content creation tools
* AI writing assistants

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

## 👩‍💻 Author

**Swati Keshri**

---

💡 *Built with AI + curiosity*
