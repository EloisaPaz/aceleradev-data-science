import streamlit as st
import pandas as pd

def main():
    st.image('logo.png')
    st.title('Working with pandas and streamlit')
    file = st.file_uploader('Upload your file', type = 'csv')
    if file is not None:
        slider = st.slider('Values', 1, 20)
        df = pd.read_csv(file)
        st.markdown('Head slider')
        st.dataframe(df.head(slider))
        st.markdown('Table slider')
        st.table(df.head(slider))
        st.markdown('Name of columns')
        st.write(df.columns)
        st.markdown('Mean')
        st.table(df.groupby('species')['petal_width'].mean())

if __name__ == "__main__":
    main()