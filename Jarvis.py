import streamlit as st

from page.auth.login import login
from page.auth.signup import signup
from page.main import main
from page.dashboard import dashboard

st.set_option("client.showSidebarNavigation", True)

if __name__ == '__main__':
    data = []
    menu = ["Dashboard", "Login", "SignUp"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == 'Dashboard':
        dashboard()
    elif choice == 'Login':
        data = login()
    elif choice == 'SignUp':
        signup()
        
    if data != []:
        main(data)
