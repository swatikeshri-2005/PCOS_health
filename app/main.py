import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import streamlit as st # type: ignore
from agents.searcher import search_web # type: ignore
from tools.scraper import extract_text # type: ignore
from agents.writer import write_article, generate_headline # type: ignore
from agents.editor import edit_article # type: ignore

st.set_page_config(page_title="AI Journalist Agent", layout="wide")

st.title("🧠 AI Journalist Agent")
st.write("Generate high-quality articles automatically")

topic = st.text_input("Enter article topic:")

if st.button("Generate Article"):
    if topic:
        # Step 1: Search
        with st.spinner("🔍 Searching web..."):
            links = search_web(topic + " news latest")

        # Step 2: Scrape
        with st.spinner("🌐 Extracting content..."):
            all_text = ""
            for link in links:
                text = extract_text(link)
                
                if len(text) > 200:
                    all_text += text + "\n\n"

        # Step 3: Write
        with st.spinner("✍️ Writing article..."):
            draft = write_article(topic, all_text)

        # Step 4: Edit
        with st.spinner("📰 Editing article..."):
            final_article = edit_article(draft)

        # Step 5: Headline
        headline = generate_headline(final_article)

        # Output
        st.subheader("📰 Headline")
        st.write(headline)

        st.subheader("📄 Article")
        st.write(final_article)

        st.subheader("🔗 Sources Used")
        for link in links:
            st.write(link)

    else:
        st.warning("Please enter a topic")