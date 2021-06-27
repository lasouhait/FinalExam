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

name = st.text_input("輸入姓名")
#st.write(answer)

if path=="國二下":
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

  st.image("./"+path+"/1213.jpg")
  Q12 = st.radio("12.",('A','B','C','D'))
  Q13 = st.radio("13.",('A','B','C','D'))

  st.image("./"+path+"/14.jpg")
  Q14 = st.radio("14.",('A','B','C','D'))

  st.image("./"+path+"/15.jpg")
  Q15 = st.radio("15.",('A','B','C','D'))

  st.image("./"+path+"/1617.jpg")
  Q16 = st.radio("16.",('A','B','C','D'))
  Q17 = st.radio("17.",('A','B','C','D'))

  st.image("./"+path+"/1819.jpg")
  Q18 = st.radio("18.",('A','B','C','D'))
  Q19 = st.radio("19.",('A','B','C','D'))

  st.image("./"+path+"/20.jpg")
  Q20 = st.radio("20.",('A','B','C','D'))

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
submit = submit.append({'題號':12,'答案':Q12},ignore_index=True)
submit = submit.append({'題號':13,'答案':Q13},ignore_index=True)
submit = submit.append({'題號':14,'答案':Q14},ignore_index=True)
submit = submit.append({'題號':15,'答案':Q15},ignore_index=True)
submit = submit.append({'題號':16,'答案':Q16},ignore_index=True)
submit = submit.append({'題號':17,'答案':Q17},ignore_index=True)
submit = submit.append({'題號':18,'答案':Q18},ignore_index=True)
submit = submit.append({'題號':19,'答案':Q19},ignore_index=True)
submit = submit.append({'題號':20,'答案':Q20},ignore_index=True)

def csv_downloader(data):
  
  csvfile = data.to_csv(index=False)
  #b64 = base64.b64encode(csvfile.encode()).decode()
  new_filename = "答案_{}_.csv".format(name)
  st.markdown(" #### Download File #### ")
  href = f'<a href="data:file/csv;base64,{csvfile}">Click here</a>'
  st.markdown(href,unsafe_allow_html=True)

if st.button('檢查提交答案'):
  st.table(submit)
  csvfile = submit.to_csv(index=False)
  st.markdown(f'<a href="data:file/csv;base64,{csvfile}">下載答案</a>',unsafe_allow_html=True)
  #csv_downloader(submit)
#st.markdown('<a href="mailto:daniel40307@yahoo.com.tw">Contact us !</a>', unsafe_allow_html=True)
#submit.to_csv("./"+path+"0901.csv",encoding="utf-8")
