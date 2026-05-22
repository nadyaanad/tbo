import streamlit as st
from FSM import ChatbotFSM

# =========================
# CONFIG PAGE
# =========================
st.set_page_config(
    page_title="Chatbot Pemesanan",
    page_icon="🤖",
    layout="wide"
)

# =========================
# CSS STYLE
# =========================
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }

    .stChatMessage {
        border-radius: 10px;
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# =========================
# INISIALISASI SESSION
# =========================
if "chatbot" not in st.session_state:
    st.session_state.chatbot = ChatbotFSM()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "cart" not in st.session_state:
    st.session_state.cart = []

# =========================
# HEADER
# =========================
st.title("🤖 Chatbot Pemesanan Makanan")
st.markdown("Silakan pesan makanan melalui chatbot.")

# =========================
# TAB MENU
# =========================
tab1, tab2 = st.tabs(["Pemesanan", "Daftar Menu"])

# =========================
# TAB PEMESANAN
# =========================
with tab1:

    col1, col2 = st.columns([1, 2])

    # =====================
    # KERANJANG BELANJA
    # =====================
    with col1:
        st.subheader("🛒 Keranjang")

        if len(st.session_state.cart) == 0:
            st.write("Keranjang kosong")
        else:
            for item in st.session_state.cart:
                st.write(f"- {item}")

    # =====================
    # CHATBOT
    # =====================
    with col2:
        st.subheader("💬 Chatbot")

        # tampilkan chat sebelumnya
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # input user
        user_input = st.chat_input("Ketik pesanan Anda...")

        if user_input:

            # tampilkan pesan user
            st.session_state.messages.append({
                "role": "user",
                "content": user_input
            })

            with st.chat_message("user"):
                st.markdown(user_input)

            # proses chatbot
            response = st.session_state.chatbot.process(user_input)

            # simpan ke keranjang jika ada keyword pesan
            if "pesan" in user_input.lower():
                st.session_state.cart.append(user_input)

            # tampilkan balasan bot
            st.session_state.messages.append({
                "role": "assistant",
                "content": response
            })

            with st.chat_message("assistant"):
                st.markdown(response)

# =========================
# TAB DAFTAR MENU
# =========================
with tab2:

    st.subheader("📋 Daftar Menu")

    menu = [
        {"nama": "Nasi Goreng", "harga": 15000},
        {"nama": "Mie Ayam", "harga": 12000},
        {"nama": "Bakso", "harga": 13000},
        {"nama": "Es Teh", "harga": 5000},
    ]

    for item in menu:
        st.write(f"🍴 {item['nama']} - Rp {item['harga']}")