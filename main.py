import streamlit as st
import mymodel as m

st.title("Sales Model")
st.write("Below are our sales predictions for this customer.")

window_value = st.slider("Select Window Size", min_value=1, max_value=50, value=15)

result = m.run(Window=window_value)
st.write(result)
