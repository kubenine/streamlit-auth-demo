import streamlit as st
import streamlit_authenticator as stauth
import yaml 

from yaml.loader import SafeLoader

with open('credentials.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['key'],
    config['cookie']['name'],
    config['cookie']['expiry_days'],
)

name, authentication_status, username = authenticator.login(location="main")

if authentication_status:
    st.write(f'Welcome *{name}*')