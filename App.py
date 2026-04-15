import streamlit as st
from groq import Groq

st.set_page_config("PragyanAI Content Generator", layout="wide")
st.title("PragyanAI – Content Generator")
st.image("")
#Get GROQ API KEY
client = Groq(api_key=st.secrets("GROQ_API_KEY"))
# Get Product Name and Audience for that product
product = st.text_input("product")
au

        
