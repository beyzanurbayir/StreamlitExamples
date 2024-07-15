import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit Projem')   # Uygulamanın başlığını belirler.

num= st.slider('Bir sayı seçin: ',0,50,100)    # Kullanıcının bir sayı seçmesini sağlar.

text=st.text_input('Bir metin girin: ','Streamlit ile çalışıyorum')  # Kullanıcının metin girişi yapmasını sağlar.

st.write('Seçtiğiniz sayı: ',num)    # Kullanıcının seçtiği sayıyı ekrana yazar.
st.write('Seçtiğiniz metin: ',text)  # Kullanıcının girdiği metni ekrana yazar.

data=pd.DataFrame(              # pd.DataFrame(): Rastgele bir veri çerçevesi oluşturur.
    np.random.randn(num,2),     # np.random.randn(num, 2): Seçilen sayıya göre rastgele veriler oluşturur.
    columns=['X','Y'])          

st.line_chart(data)             # # st.line_chart(): Veri çerçevesini çizgi grafiği olarak görselleştirir.

