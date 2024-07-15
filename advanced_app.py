import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Streamlit Projem')

uploaded_file= st.file_uploader('Bir CSV dosyası yükleyin',type=['csv'])

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write('Yüklenen veri: ')
    st.write(df.head())

    st.write('Verinin temel istatistikleri: ')
    st.write(df.describe())

    st.write('Veri görselleştirme: ')

    cols=df.columns.tolist()
    x_axis=st.selectbox('X ekseni için bir sütun seçiniz: ',cols)
    y_axis=st.selectbox('Y ekseni için bir sütun seçiniz: ',cols)

     
    if x_axis and y_axis:
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f'{x_axis} ve {y_axis} Scatter Plot')
        st.pyplot(fig)
    
    hist_col=st.selectbox('Histogram için bir sütun seçiniz: ',cols)

    if hist_col:
        fig,ax=plt.subplots()
        sns.histplot(df[hist_col],kde=True,ax=ax)
        ax.set_xlabel(hist_col)
        ax.set_ylabel('Frekans')
        ax.set_title(f'{hist_col} Histogram')
        st.pyplot(fig)

else:
    st.write('Lütfen bir csv dosyası yükleyiniz')


