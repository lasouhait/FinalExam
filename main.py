# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
#import statsmodels.api as sm

st.set_page_config(page_title="期末考頁面")
st.title("109年度第二學期期末考")
#st.write("All information is for personal use, and is not aimed to provide suggestion.")
#page_nav = st.sidebar.radio("請選取頁面",["營運概況","人力資訊","董監酬勞揭露","股價資訊","金融統計"])

path="國二下"
answer = pd.read_csv("./"+path+"/正解.csv")

st.write(answer)

st.image("./"+path+"/1.jpg")
Q1 = st.radio("1.",('A','B','C','D'))

st.image("./"+path+"/2.jpg")
Q2 = st.radio("2.",('A','B','C','D'))

st.image("./"+path+"/3.jpg")
Q3 = st.radio("3.",('A','B','C','D'))

st.image("./"+path+"/4.jpg")
Q4 = st.radio("4.",('A','B','C','D'))

st.image("./"+path+"/5.jpg")
Q5 = st.radio("5.",('A','B','C','D'))

st.image("./"+path+"/67.jpg")
Q6 = st.radio("6.",('A','B','C','D'))
Q7 = st.radio("7.",('A','B','C','D'))

st.image("./"+path+"/8.jpg")
Q8 = st.radio("8.",('A','B','C','D'))

st.image("./"+path+"/9.jpg")
Q9 = st.radio("9.",('A','B','C','D'))

st.image("./"+path+"/1011.jpg")
Q10 = st.radio("10.",('A','B','C','D'))
Q11 = st.radio("11.",('A','B','C','D'))

submit = pd.DataFrame(columns=['題號','答案'])
submit = submit.append({'題號':1,'答案':Q1},ignore_index=True)
submit = submit.append({'題號':2,'答案':Q2},ignore_index=True)
submit = submit.append({'題號':3,'答案':Q3},ignore_index=True)
submit = submit.append({'題號':4,'答案':Q4},ignore_index=True)
submit = submit.append({'題號':5,'答案':Q5},ignore_index=True)
submit = submit.append({'題號':6,'答案':Q6},ignore_index=True)
submit = submit.append({'題號':7,'答案':Q7},ignore_index=True)
submit = submit.append({'題號':8,'答案':Q8},ignore_index=True)
submit = submit.append({'題號':9,'答案':Q9},ignore_index=True)
submit = submit.append({'題號':10,'答案':Q10},ignore_index=True)
submit = submit.append({'題號':11,'答案':Q11},ignore_index=True)

st.write(submit)
submit.to_csv("./"+path+"0901.csv",encoding="utf-8")
