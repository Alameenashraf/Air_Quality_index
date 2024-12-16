import streamlit as st

def app():
    # Title and Description
    st.title("Air Quality Power BI Dashboard")
   

    # Embed the Power BI dashboard
    power_bi_embed_url = "https://app.powerbi.com/view?r=eyJrIjoiY2RjNTY2MGYtZTYxNC00ZmM4LWI5ZTAtYmIwYWUxNTVjMzA5IiwidCI6IjlhNDNhMzAxLTk5OWMtNDljYy1iMTA1LWExMjYxODVlNjVlYiJ9&pageName=ab0cd5de87d79c73d219"  # Replace with your URL

    # Use an iframe to embed the dashboard
    st.components.v1.html(
        f"""
        <iframe 
            src="{power_bi_embed_url}" 
            width="100%" 
            height="600" 
            frameborder="0" 
            allowFullScreen="true">
        </iframe>
        """,
        height=600,
    )



# Call the app function to run the Streamlit app
if __name__ == "__main__":
    app()
