import streamlit as st

# Title of the app
st.title('Sample Streamlit App')

# Header
st.header('Welcome to my Streamlit app!')

# Text
st.write('This is a simple example of a Streamlit app.')

# Input text box
user_input = st.text_input('Enter some text:')

# Display user input
st.write('You entered:', user_input)

# Slider
slider_value = st.slider('Select a value', 0, 100, 50)

# Display slider value
st.write('Slider value:', slider_value)

# Button
if st.button('Click me'):
    st.write('Button clicked!')

# Checkbox
if st.checkbox('Check me'):
    st.write('Checkbox checked!')

# Selectbox
option = st.selectbox('Select an option:', ['Option 1', 'Option 2', 'Option 3'])

# Display selected option
st.write('You selected:', option)