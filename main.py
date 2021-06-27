# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
#import statsmodels.api as sm

st.set_page_config(page_title="期末考頁面")
st.title("109年度第二學期期末考")
#st.write("All information is for personal use, and is not aimed to provide suggestion.")
#page_nav = st.sidebar.radio("請選取頁面",["營運概況","人力資訊","董監酬勞揭露","股價資訊","金融統計"])

path="/國二下/"
answer = pd.read_csv(path+"正解.csv")

st.write(answer)
