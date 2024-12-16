import streamlit as st

def app():
    st.title('Welcome to :violet[Air Quality Index]')

    # Initialize session state for login if not already initialized
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if 'username' not in st.session_state:
        st.session_state.username = ""

    def authenticate(username, password):
        """Simple authentication logic."""
        # Replace this with your own authentication logic
        return username == "admin" and password == "password"

    def login(username):
        """Login function."""
        st.session_state.logged_in = True
        st.session_state.username = username

    def logout():
        """Logout function."""
        st.session_state.logged_in = False
        st.session_state.username = ""

    def dashboard():
        """Dashboard content."""
        st.title(f"Dashboard - Welcome, {st.session_state.username}!")
        st.write("This is the dashboard page where the main content is displayed.")
        st.components.v1.iframe(
            "https://app.powerbi.com/view?r=eyJrIjoiY2RjNTY2MGYtZTYxNC00ZmM4LWI5ZTAtYmIwYWUxNTVjMzA5IiwidCI6IjlhNDNhMzAxLTk5OWMtNDljYy1iMTA1LWExMjYxODVlNjVlYiJ9&pageName=ab0cd5de87d79c73d219",
            width=600,
            height=373.5,
        )
        if st.button("Logout"):
            logout()
            st.success("You have been logged out.")

    # UI for login
    if not st.session_state.logged_in:
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if authenticate(username, password):
                login(username)
                st.success("Logged in successfully!")
            else:
                st.error("Invalid username or password")
    else:
        dashboard()

if __name__ == "__main__":
    app()

