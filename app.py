import json
import os
import spacy
import streamlit as st
import pandas as pd

# Load spaCy model
nlp = spacy.load("en_core_web_lg")

# Load products from JSON
with open("products.json", "r") as f:
    products = json.load(f)

df = pd.DataFrame(products)

# Streamlit page setup
st.set_page_config(page_title="🛍️ AI Product Catalog & Recommender", layout="wide")
st.title("🛍 AI Product Catalog & Recommender")

# --- Sidebar Filters ---
st.sidebar.header("Filters")

# Category filter
categories = ["All"] + sorted(df["category"].unique().tolist())
selected_category = st.sidebar.selectbox("Select Category", categories)

# Price filter
min_price, max_price = st.sidebar.slider(
    "Select Price Range",
    min_value=int(df["price"].min()),
    max_value=int(df["price"].max()),
    value=(int(df["price"].min()), int(df["price"].max()))
)

# --- User query ---
st.subheader("🔍 Search with AI")
st.write("Example: *'Show me running shoes under $100 with good reviews'*")
query = st.text_input("Your request:")

# Function: spaCy similarity search
def get_similar_products(user_query, top_n=5):
    query_vec = nlp(user_query)
    scored_products = []
    for product in products:
        product_text = f"{product['name']} category {product['category']} price {product['price']} reviews {product['reviews']}"
        score = query_vec.similarity(nlp(product_text))
        scored_products.append((product, score))
    scored_products.sort(key=lambda x: x[1], reverse=True)
    return [p[0] for p in scored_products[:top_n]]

# --- Apply search & filters ---
if query.strip():
    recommended = get_similar_products(query, top_n=5)
    results_df = pd.DataFrame(recommended)
else:
    results_df = df.copy()

# Apply category filter
if selected_category != "All":
    results_df = results_df[results_df["category"] == selected_category]

# Apply price filter
results_df = results_df[(results_df["price"] >= min_price) & (results_df["price"] <= max_price)]

# --- Display Results ---
st.subheader(f"📦 Showing {len(results_df)} Products")
if not results_df.empty:
    for _, row in results_df.iterrows():
        with st.container():
            st.markdown(f"**{row['name']}** — ${row['price']} — ⭐ {row['reviews']}")
            st.caption(f"Category: {row['category']} — {row['description']}")
            st.markdown("---")
else:
    st.warning("No products match your filters/search.")
