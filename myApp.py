import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of Cats")

col1, col2 = st.columns(2)
with col1:
  st.subheader("Persian Pilli")
  st.image("./persionPilli.jpg", caption="Persian Cat", width=300,use_column_width=True)
  st.write("I sow it on Little stuart")
with col2:
  st.subheader("Normal Pilli")
  st.image("./normalPilli.jpeg", caption="Ragdoll Cat", width=300,use_column_width=True)
  st.write("Just Normal Pilli")
