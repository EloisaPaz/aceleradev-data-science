import streamlit as st

def main():
    st.title('Hello world')
    st.header('This is a header')
    st.subheader('This is a subheader')
    st.text('This is a text')
    st.subheader('Image:')
    st.image('logo.png')
    st.subheader('Video:')
    st.video('https://www.youtube.com/watch?v=_Zak427WNwY')
    st.markdown('Button')
    botao = st.button('Button')
    
    if botao:
        st.markdown('Clicked')

    st.markdown('Checkbox')
    check = st.checkbox('Checkbox')
    if check:
        st.markdown('Clicked')

    st.markdown('Radio Button') 
    radio = st.radio('Choose options', ('Option 1','Option 2', 'K'))
    if radio == 'Option 1':
        st.markdown('Option 1')
    if radio == 'Option 2':
        st.markdown('Option 2')

    st.markdown('Select Box')
    select = st.selectbox('Choose options', ('Option 1','Option 2'))
    if select == 'Option 1':
        st.markdown('Option 1')
    if select == 'Option 2':
        st.markdown('Option 2')

    st.markdown('Multi Select')
    multi = st.multiselect('Choose:', ('Option 1','Option 2'))
    if multi == 'Option 1':
        st.markdown('Option 1')
    if multi == 'Option 2':
        st.markdown('Option 2')

    st.markdown('File Uploader')
    file = st.file_uploader('Choose your file', type = 'csv')
    if file is not None:
        st.markdown('Not empty')



if __name__ == "__main__":
    main()