import streamlit as st
import sqlite3
import hashlib

# Create a SQLite database and users table
def create_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Add user to the database
def add_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hash_password(password)))
    conn.commit()
    conn.close()

# Authenticate user
def authenticate_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hash_password(password)))
    user = c.fetchone()
    conn.close()
    return user

# Delete user from the database
def delete_user(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE username = ?', (username,))
    conn.commit()
    conn.close()

# Main Streamlit app
def main():
    st.title('User Authentication System')

    # Create database and users table
    create_db()

    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.session_state.username = None

    menu = ['Home', 'Sign Up', 'Sign In']
    if st.session_state.authenticated:
        menu.append('Protected Page')
        menu.append('Delete Account')
        menu.append('Logout')
    choice = st.sidebar.selectbox('Menu', menu)

    if choice == 'Home':
        st.subheader('Home Page')
        st.write('Welcome to the Home Page!')

    elif choice == 'Sign Up':
        st.subheader('Create New Account')

        new_user = st.text_input('Username')
        new_password = st.text_input('Password', type='password')

        if st.button('Sign Up'):
            if new_user and new_password:
                try:
                    add_user(new_user, new_password)
                    st.success('Account created successfully!')
                except sqlite3.IntegrityError:
                    st.error('Username already exists. Please choose a different username.')
            else:
                st.error('Please enter a username and password.')

    elif choice == 'Sign In':
        st.subheader('Login to Your Account')

        username = st.text_input('Username')
        password = st.text_input('Password', type='password')

        if st.button('Sign In'):
            user = authenticate_user(username, password)
            if user:
                st.session_state.authenticated = True
                st.session_state.username = username
                st.success(f'Welcome {username}!')
            else:
                st.error('Invalid username or password.')

    elif choice == 'Protected Page':
        if st.session_state.authenticated:
            st.subheader('Protected Page')
            st.write('This page is only accessible to logged-in users.')
        else:
            st.error('You must be logged in to access this page.')

    elif choice == 'Delete Account':
        if st.session_state.authenticated:
            st.subheader('Delete Your Account')

            password = st.text_input('Password', type='password')

            if st.button('Delete Account'):
                user = authenticate_user(st.session_state.username, password)
                if user:
                    delete_user(st.session_state.username)
                    st.session_state.authenticated = False
                    st.session_state.username = None
                    st.success('Account deleted successfully.')
                else:
                    st.error('Invalid password.')
        else:
            st.error('You must be logged in to delete your account.')

    elif choice == 'Logout':
        st.session_state.authenticated = False
        st.session_state.username = None
        st.success('You have been logged out.')

if __name__ == '__main__':
    main()
