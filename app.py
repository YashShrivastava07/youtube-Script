import streamlit as st
from utils import  get_info

st.markdown("""
<style>
div.stButton > button:first-child{
            background-color: #0099ff;
            color: #ffffff
}
div.stButton > button:hover{
            background-color: #00ff00;
            color: #ffffff
}
</style>""",unsafe_allow_html=True)


if 'API_KEY' not in st.session_state:
    st.session_state['API_KEY']=''

st.title("❤️Youtube Script Writing Tool❤️")

st.sidebar.title("🔑🔑")
st.session_state['API_KEY']=st.sidebar.text_input("What's your API Key",type="password")
st.sidebar.image('YouTube.png',width=300,use_column_width=True)

prompt=st.text_input("Please provide the topic of your video",key='prompt')
video_length=st.text_input('Expected Video length (in minutes)',key='video_length')
creativity=st.slider('Creativity',0.0,1.0,0.1,step=0.1)

submit=st.button("Generate Script for me")

if submit:

    if st.session_state['API_KEY']:
        title,script,DuckDuckGoSearch=get_info(prompt=prompt,video_length=video_length,creativity=creativity,api_key=st.session_state['API_KEY'])
        st.success('Hope you like the Script')

        st.subheader('Title:🔥'+title)

        st.subheader('Your Video Script: 📜'+script)

        st.subheader('Check out - DuckDuckGo Search Data:🔍')
        with st.expander('Show me: 👀'):
            st.info('Search Data: '+DuckDuckGoSearch)

    else:
        st.error('Please provide valid API key Bro')