## Simple Streamlit app that displays a 2 column layout with a title and a text

from nameparser import HumanName
import streamlit as st

st.title('My first Streamlit app')
st.write('Here is a simple example of a Streamlit app with a title and some text.')
name = HumanName("Dr. Juan Q. Xavier de la Vega III (Doc Vega)")
name.as_dict()
print(name.last)
st.write(name.last)
