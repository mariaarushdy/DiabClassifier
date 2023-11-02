# -*- coding: utf-8 -*-
"""
Created on Tue May 17 15:58:29 2022

@author: ECC
"""

import streamlit as st
import pandas as pd
import numpy as np
import pickle 
st.title('**Diabetes** :cry:')
st.text('Diabetes is one of the fastest growing chronic life threatening diseases that have \nalready affected 422 million people worldwide according to the report of World Health \nOrganization (WHO), in 2018. Due to the presence of a relatively long asymptomatic \nphase, early detection of diabetes is always desired for a clinically meaningful \noutcome. Around 50% of all people suffering from diabetes are undiagnosed because of \nits long-term asymptomatic phase..')
df = pd.read_csv(r'C:\Users\ECC\Downloads\raw_data.csv')
dia = pd.read_csv(r'C:\Users\ECC\Downloads\diabetes_data.csv' , delimiter= ';')
head = df.head()
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(head)

st.markdown("<h2 style='text-align: center; color: lightblue;'>Diabetes awereness </h2>", unsafe_allow_html=True)

st.video(r'C:\Users\ECC\Downloads\Diabetes Awareness 2019.mp4' , format="video/mp4", start_time=0)

st.sidebar.header('Diabetes symptoms')
st.sidebar.subheader('If you have any of the following diabetes symptoms, see your doctor about getting your blood sugar tested:')
st.sidebar.text("\n  -Urinate (pee) a lot,often at night\n  -Are very thirsty\n  -Lose weight without trying\n  -Are very hungry\n  -Have blurry vision\n  -Have numb or tingling hands or feet\n  -Feel very tired\n  -Have very dry skin\n  -Have sores that heal slowly\n  -Have more infections than usual")

#--------------------------
st.subheader('Ages of Males and Femals having diabetes.')
gende = st.selectbox(
     'select the gender',
     ('Male', 'Female'))

flt= dia[dia['gender'] == gende]
hist_values = np.histogram( flt['age'])[0]
st.bar_chart(hist_values)
#-------------------------
st.subheader('Mab of diabetes around the world')
years_to_filter = st.selectbox(
     'select the year',
     ('2010', '2019'))
years = int(years_to_filter)
filtered_data = df[df['Year'] == years]
st.map(filtered_data)
st.header('Quicck Cheackup')
st.subheader('check if u have diabetes or not by answering the following for you own safety.')

s =[]
option = int(st.text_input('how old are you'))
s.append(option)
#-----------------
option = st.selectbox(
     'Whether the patient experienced excessive urination or not.',
     ('yes', 'no'))
if(option == 'yes'):
    option = 1
else : option = 0
s.append(option)
#-------------------
option = st.selectbox(
     'Whether the patient experienced excessive thirst/excess drinking or not.',
     ('yes', 'no'))
if(option == 'yes'):
    option = 1
else : option = 0
s.append(option)
#------------------
option = st.selectbox(
     'Whether patient had an episode of sudden weight loss or not.',
     ('yes', 'no'))
if(option == 'yes'):
    option = 1
else : option = 0
s.append(option)
#------------------
option = st.selectbox(
     'Whether patient had an episode of feeling weak.',
     ('yes', 'no'))
if(option == 'yes'):
    option = 1
else : option = 0
s.append(option)
#------------------
option = st.selectbox(
     'Whether patient had an episode of excessive/extreme hunger or not.',
     ('yes', 'no'))
if(option == 'yes'):
    option = 1
else : option = 0
s.append(option)
#------------------
option = st.selectbox(
     'Whether patient had a yeast infection or not.',
     ('yes', 'no'))
if(option == 'yes'):
    option = 1
else : option = 0
s.append(option)
#------------------
option = st.selectbox(
     'Whether patient had an episode of blurred vision.',
     ('yes', 'no'))
if(option == 'yes'):
    option = 1
else : option = 0
s.append(option)
#------------------
option = st.selectbox(
     'Whether patient had an episode of itch.',
     ('yes', 'no'))
if(option == 'yes'):
    option = 1
else : option = 0
s.append(option)
#------------------
option = st.selectbox(
     'Whether patient had an episode of irritability.',
     ('yes', 'no'))
if(option == 'yes'):
    option = 1
else : option = 0
s.append(option)
#------------------
option = st.selectbox(
     'Whether patient had an noticed delayed healing when wounded.',
     ('yes', 'no'))
if(option == 'yes'):
    option = 1
else : option = 0
s.append(option)
#------------------
option = st.selectbox(
     'Whether patient had an episode of weakening of a muscle/group of muscles or not.',
     ('yes', 'no'))
if(option == 'yes'):
    option = 1
else : option = 0
s.append(option)
#------------------
option = st.selectbox(
     'Whether patient had an episode of muscle stiffness.',
     ('yes', 'no'))
if(option == 'yes'):
    option = 1
else : option = 0
s.append(option)
#------------------
option = st.selectbox(
     'Whether patient experienced hair loss or not.',
     ('yes', 'no'))
if(option == 'yes'):
    option = 1
else : option = 0
s.append(option)
#------------------
option = st.selectbox(
     'Whether patient can be considered obese or not using his body mass index.',
     ('yes', 'no'))
if(option == 'yes'):
    option = 1
else : option = 0
s.append(option)
#------------------
option = st.selectbox(
     'what is the patient gender is ',
     ('male', 'female'))
if(option == 'male'):
    option = 1
else : option = 0
s.append(option)
#------------------
loadmodel = pickle.load(open('D:/trained_model.sav','rb'))
nparr = np.asanyarray(s)
reshap = nparr.reshape(1,-1)
#stdip = scaler.transform(reshap)
predc = loadmodel.predict(reshap)
if st.button('Result'):
    if(predc == 0) :
        st.markdown("<h2 style='text-align: center; color: lightblue;'>person is non diabetic, congrates </h2>", unsafe_allow_html=True)
        st.subheader(':relieved: :blue_heart:')
        st.balloons()
    else:
        st.markdown("<h2 style='text-align: center; color: red;'>Im sorry, but there is a big chance that you might be diabetic </h2>", unsafe_allow_html=True)
        st.subheader('               hope you get better lvu u take care of urself:cry:	:heart: ')