import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of Cats")

col1, col2 = st.columns(2)
with col1:
  st.subheader("Son Goku")
  st.image("./goku.jpg", caption="Son Goku", width=300,use_column_width=True)
  st.write("kamehameha")
with col2:
  st.subheader("Yuta Okkotsu")
  st.image("./Yuta_Okkotsu.png", caption="Yuta Okkotsu", width=300,use_column_width=True)
  st.write("GOOD ONE")
