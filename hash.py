import streamlit_authenticator as stauth

hashed_password = stauth.Hasher(['password123']).generate()
print(hashed_password)
