# 🛍 AI Product Catalog & Recommender

An interactive **e-commerce product catalog** built with **Streamlit** that uses **AI-powered recommendations** via **spaCy** for natural language search.  
Users can browse, filter, and search products using both structured filters (category, price) and natural language queries like:

> `"Show me running shoes under $100 with good reviews"`

---

## 🚀 How to Run the App

1. **Clone the repository**:
   ```bash
   git clone https://github.com/adeelafzal01/Recommendation-System.git
   cd Product Recommendations
2. **Install dependencies**:
   Make sure you have Python 3.8+ installed, then run:
   ```bash
   pip install -r requirements.txt
3. **Download the spaCy model**:
   ```bash
   python -m spacy download en_core_web_lg
4. **Run the app**:
   ```bash
   streamlit run app.py
3. **Open your browser at**:
   ```bash
   http://localhost:

🧠 AI Feature Used
- Recommendation System with Natural Language Search
- Uses spaCy's large English model (en_core_web_lg) to compute semantic similarity between the user's query and product metadata.
- Matches product names, categories, prices, and reviews against the user's intent.
- Displays the top N recommended products that best match the query.

🛠 Tools / Libraries Used
- Streamlit – For building the interactive web UI.
- spaCy – For natural language processing and similarity scoring.
- pandas – For managing and filtering product data.
- Python Standard Library – json, os.

📌 Notable Assumptions
- Product data is loaded from a static products.json file containing:
  - name, category, price, description, reviews.
- The AI recommendation system is local (no API calls to external AI services) for speed and offline capability.
- The price field is assumed to be a number in USD.
- The reviews field is an average rating between 1.0 and 5.0.
- Filters are applied after AI recommendations to refine results.
- No authentication or cart functionality is implemented — the focus is on catalog browsing & AI-powered search.

📂 Project Structure
   ```bash
  📦 product-recommender
 ┣ 📜 app.py              # Main Streamlit app
 ┣ 📜 products.json       # Product catalog (static data)
 ┣ 📜 requirements.txt    # Dependencies
 ┗ 📜 README.md           # Documentation
```

💡 Possible Enhancements
- Add OpenAI API for more context-aware product recommendations.
- Implement dynamic pricing or personalized suggestions based on user history.
- Integrate with blockchain for token-gated pricing or on-chain loyalty rewards.

If integrating blockchain:
- Store user preferences on-chain (categories, budget, past purchases) so they’re portable across stores.
- Use token-gated discounts (NFT holders get special prices).
- Maintain a loyalty program with smart contracts where purchases automatically add reward tokens to the user’s wallet.


    





   
   
