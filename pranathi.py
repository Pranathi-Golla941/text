import streamlit as st
import re
from collections import Counter
import pandas as pd

st.title("Word Frequency from uploaded text file")
uploaded = st.file_uploader("Upload a .txt file", type=["txt"])
if uploaded:
    content = uploaded.read().decode("utf-8")
    words = re.findall(r"\b\w+\b", content.lower())
    df = pd.DataFrame(Counter(words).items(), columns=["Word","Count"]).sort_values("Count", ascending=False).reset_index(drop=True)
    st.dataframe(df)
