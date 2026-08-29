import json
import os
import streamlit as st
from google import genai

st.set_page_config(
    page_title="Barista AI | Premium Coffee Assistant",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .stApp { background-color: #0F172A; color: #F8FAFC; }
    [data-testid="stSidebar"] { background-color: #1E293B; border-right: 1px solid #334155; }
    .menu-card { background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 12px; padding: 14px; margin-bottom: 12px; }
    .tag-badge { background: #334155; color: #38BDF8; padding: 2px 8px; border-radius: 6px; font-size: 11px; font-weight: 600; margin-right: 4px; }
    .allergen-badge { background: #451A03; color: #F97316; padding: 2px 8px; border-radius: 6px; font-size: 11px; font-weight: 600; }
    .main-header { background: linear-gradient(135deg, #0284C7 0%, #0F172A 100%); padding: 24px; border-radius: 16px; border: 1px solid #0369A1; margin-bottom: 24px; }
    
    /* Text color fixes for clear visibility */
    [data-testid="stChatMessage"] p, [data-testid="stChatMessage"] li, [data-testid="stChatMessage"] div {
        color: #FFFFFF !important;
        font-size: 15px !important;
    }
    [data-testid="stChatMessage"][data-testimonial-user="true"] p {
        color: #0F172A !important;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1 style="margin:0; color:#FFFFFF;">☕ Coffee Barista AI Agent</h1>
    <p style="margin:4px 0 0 0; color:#94A3B8; font-size:14px;">Powered by Gemini 2.5 Flash & Google Cloud</p>
</div>
""", unsafe_allow_html=True)

def get_menu_data():
    try:
        with open("menu.json", "r") as f:
            return json.load(f)
    except Exception:
        return []

menu_data = get_menu_data()

with st.sidebar:
    st.markdown("<h2 style='color:#F8FAFC; margin-bottom:16px;'>📜 Live Menu Catalog</h2>", unsafe_allow_html=True)
    if menu_data:
        for item in menu_data:
            tags_html = "".join([f'<span class="tag-badge">{tag}</span>' for tag in item.get('tags', [])])
            allergens_html = "".join([f'<span class="allergen-badge">⚠️ {alg}</span>' for alg in item.get('allergens', [])])
            st.markdown(f"""
            <div class="menu-card">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <span style="font-weight:bold; font-size:16px; color:#F8FAFC;">{item['name']}</span>
                    <span style="color:#38BDF8; font-weight:bold; font-size:15px;">${item['price']:.2f}</span>
                </div>
                <p style="font-size:12px; color:#94A3B8; margin:6px 0 10px 0;">{item['description']}</p>
                <div>{tags_html} {allergens_html}</div>
            </div>
            """, unsafe_allow_html=True)

project_id = os.environ.get("GOOGLE_CLOUD_PROJECT", "gen-lang-client-0019210947")
location = os.environ.get("GOOGLE_CLOUD_REGION", "us-central1")
client = genai.Client(vertexai=True, project=project_id, location=location)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to our AI Coffee Bar! How can I assist you with our menu today?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Type your order or ask a menu question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        system_instruction = f"You are a barista assistant. Use menu: {json.dumps(menu_data)}. Recommend items from this menu only."
        
        try:
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt,
                config={'system_instruction': system_instruction}
            )
            final_response = response.text if response.text else "I couldn't process that request."
            response_placeholder.markdown(final_response)
            st.session_state.messages.append({"role": "assistant", "content": final_response})
        except Exception as e:
            err_msg = f"Error: {str(e)}"
            response_placeholder.error(err_msg)
            st.session_state.messages.append({"role": "assistant", "content": err_msg})
