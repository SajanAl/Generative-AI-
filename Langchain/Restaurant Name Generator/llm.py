
import streamlit as st
import langchain_helper

# App title
st.title("Restaurant Name and Menu Generator")

# Sidebar to select cuisine type
cuisine = st.sidebar.selectbox(
    "Select Cuisine Type",
    ('Pakistani', 'Indian', 'Italian', 'Chinese', 'Mexican', 'American')
)

# Generate and display the restaurant name and menu
if cuisine:

    response = langchain_helper.generate_restaurant_name_and_items(cuisine)


    restaurant_name = response['restaurant_name'].strip()

    # Display the concise restaurant name
    st.header(f"🍴 Welcome to {restaurant_name} 🍴")

    # Display the menu items
    menu_items = response['menu_item'].strip().split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write(f"- {item}")









