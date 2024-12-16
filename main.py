import streamlit as st

from streamlit_option_menu import option_menu

import login, dashboard, database

st.set_page_config(
        page_title="Air Quality Index",
)

class MultiApp:

    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        
        with st.sidebar:        
            app = option_menu(
                menu_title='Air Quality Index',
                options=['login', 'dashboard', 'database'],
            
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
                
                )

        
        if app == "login":
            login.app()
        if app == "dashboard":
            dashboard.app()   
        if app == "database":
            database.app()   
                      
    run()            
         
