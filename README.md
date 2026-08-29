# ☕ Coffee Barista AI Agent

An intelligent, conversational Coffee Barista AI Agent built using **Streamlit**, **Python**, **Google Cloud Run**, and the **Gemini API**. This application serves as an interactive beverage ordering assistant that helps users explore the menu, customize their drink orders, and receive real-time recommendations.

---

## 🌟 Key Features

* **Interactive Menu Exploration**: Browse through available coffee, tea, and bakery options.
* **Smart Drink Customization**: Order beverages with specific options (milk preference, sweetness level, size, toppings).
* **AI-Powered Recommendations**: Real-time natural language responses powered by Gemini API.
* **Cloud Native Deployment**: Fully containerized using Docker and hosted on Google Cloud Run for scalability.

---

## 🛠️ Tech Stack

* **Frontend / UI**: Streamlit
* **Language**: Python 3.10+
* **AI Model / LLM**: Gemini API
* **Containerization**: Docker
* **Cloud Platform**: Google Cloud Run

---

## 🚀 Live Demo

Check out the live running application here:  
🔗 **[Coffee Barista AI Agent Live Demo](https://coffee-barista-717984413079.us-central1.run.app)**

---

## 📂 Repository Structure

```text
├── agent.py            # AI Barista logic and Gemini integration
├── app.py              # Streamlit Web Application interface
├── menu.json           # Coffee shop menu and pricing data
├── Dockerfile          # Container configuration for Google Cloud Run
├── Procfile            # Deployment execution rules
└── requirements.txt    # Python dependencies
