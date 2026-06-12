import streamlit as st

st.title("Affiliate Content Generator")

produk = st.text_input("Nama Produk")

if st.button("Generate"):
    st.write("Produk:", produk)
    st.write("Hook:")
    st.write(f"{produk} yang lagi viral ternyata sebagus ini!")
