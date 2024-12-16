import pandas as pd
import streamlit as st

def app():
    # Corrected file path
    df = pd.read_csv(r"C:\Users\Alameen\OneDrive\Desktop\AQI\AQI2020-2022.csv")

    # Displaying the dataframe in Streamlit
    st.dataframe(df)

# Run the app function
if __name__ == "__main__":
    app()
