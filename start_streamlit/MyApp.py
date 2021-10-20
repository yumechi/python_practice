import streamlit as st
import pandas as pd
import numpy as np

st.write("""
# なぞぐらふ
なぞぐらふです
""")


df = pd.read_csv("my_data.csv")
# df = pd.DataFrame(
#      np.random.randn(12, 3),
#      columns=['a', 'b', 'c'])

st.line_chart(df)
