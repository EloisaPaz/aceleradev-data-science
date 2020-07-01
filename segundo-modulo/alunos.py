import streamlit as st

def main():
    st.title('Hello world')
    st.header('This is a header')
    st.subheader('This is a subheader')
    st.text('This is a text')
    st.subheader('Imagem:')
    st.image('logo.png')
    st.subheader('Vídeo:')
    st.video('https://www.youtube.com/watch?v=_Zak427WNwY')

if __name__ == "__main__":
    main()