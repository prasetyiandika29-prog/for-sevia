import streamlit as st
import time

# Konfigurasi Halaman Web
st.set_page_config(
    page_title="Special Question for Sevia ❤️",
    page_icon="💖",
    layout="centered"
)

# Kustomisasi CSS untuk Desain Romantis
st.markdown("""
    <style>
    /* Latar belakang nuansa romantis */
    .stApp {
        background: linear-gradient(135deg, #ffe6eb 0%, #ffb6c1 100%);
    }
    
    /* Style Judul */
    .title-text {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        color: #d81b60;
        text-align: center;
        font-size: 38px;
        font-weight: bold;
        margin-top: 50px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Custom tombol */
    div.stButton > button {
        width: 100%;
        border-radius: 20px;
        font-size: 20px;
        font-weight: bold;
        padding: 10px 24px;
        transition: all 0.3s ease;
    }
    </style>
""", unsafe_allow_html=True)

# Judul Utama
st.markdown("<h1 class='title-text'>Sevia, will you be my girlfriend? 🌹✨</h1>", unsafe_allow_html=True)
st.write("")
st.write("")

# Inisialisasi state untuk menyimpan status jawaban
if 'answered' not in st.state_models if hasattr(st, 'state_models') else 'answered' not in st.session_state:
    st.session_state.answered = None

# Tampilan Tombol Opsi
col1, col2 = st.columns(2)

with col1:
    if st.button("💖 YES 💖", key="yes_btn"):
        st.session_state.answered = "YES"

with col2:
    if st.button("💔 NO 💔", key="no_btn"):
        st.session_state.answered = "NO"

# Respon berdasarkan pilihan
if st.session_state.answered == "YES":
    st.balloons()  # Efek balon beterbangan
    st.snow()      # Efek salju/kelopak gugur
    st.markdown("""
        <div style='text-align: center; background-color: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 15px; margin-top: 20px;'>
            <h2 style='color: #e91e63;'>YAY! 🥰❤️</h2>
            <p style='font-size: 20px; color: #333;'>Kamu telah membuat hari ini menjadi hari terindah! Terima kasih sudah menerima aku, Sevia! ✨💍</p>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.answered == "NO":
    st.markdown("""
        <div style='text-align: center; background-color: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 15px; margin-top: 20px;'>
            <h3 style='color: #555;'>Yahhh... 🥺🥺</h3>
            <p style='font-size: 18px; color: #666;'>Gak apa-apa kok, tapi coba pikir-pikir lagi dan tekan tombol YES ya? 😉</p>
        </div>
    """, unsafe_allow_html=True)
