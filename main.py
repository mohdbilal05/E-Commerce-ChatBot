import streamlit as st
from router import router
from faq import ingest_faq_data, faq_chain
from pathlib import Path
from sql import sql_chain

faqs_path = Path(__file__).parent / "resources" / "faq_data.csv"
ingest_faq_data(faqs_path)


def ask(query):
    route = router(query).name
    if route == 'faq':
        return faq_chain(query)
    elif route == 'sql':
        return sql_chain(query)
    else:
        return f"Route {route} not implemented yet"


st.set_page_config(page_title="E-Commerce Bot", page_icon="🛍️")
st.title("🛍️ E-Commerce ChatBot")
st.caption("Ask me about products, pricing, or store policies!")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Welcome screen when no messages yet
if not st.session_state.messages:
    st.markdown("### 👋 How can I help you today?")
    st.markdown("Here are some things you can ask me:")

    col1, col2 = st.columns(2)
    with col1:
        st.info("🏷️ **Product Queries**\n\nNike shoes with 50% discount\n\nPuma shoes under Rs. 3000\n\nFormal shoes in size 9")
    with col2:
        st.info("📋 **Store Policies**\n\nWhat is your return policy?\n\nAccepted payment methods\n\nHow to use a promo code")

    st.divider()

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

query = st.chat_input("Write your query here...")

if query:
    with st.chat_message("user"):
        st.markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})

    with st.spinner("Thinking..."):
        response = ask(query)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})