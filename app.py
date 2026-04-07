import streamlit as st
import requests

# --- CONFIGURATION ---
API_URL = "https://api.quotable.io/random"

# --- LOGIC: FETCHING DATA ---
# def fetch_quote():
#     """Fetches a random quote from the API."""
#     try:
#         # We use a timeout so the app doesn't hang forever if the internet is slow
#         response = requests.get(API_URL, timeout=5, verify=False)
#         response.raise_for_status() # Check if the request was successful
#         return response.json()
#     except requests.exceptions.RequestException as e:
#         st.error(f"Connection Error: {e}")
#         return None

def fetch_quote():
    """Fetches a random quote from the ZenQuotes API."""
    try:
        # ZenQuotes is a very reliable alternative
        response = requests.get("https://zenquotes.io/api/random", timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # ZenQuotes returns a list, so we take the first item [0]
        return {
            'content': data[0]['q'],
            'author': data[0]['a']
        }
    except Exception as e:
        st.error(f"Could not connect to the quote server. Error: {e}")
        return None

# --- INTERFACE: STREAMLIT UI ---
# def main():
#     # Set the page title and icon
#     st.set_page_config(page_title="Quote Gen", page_icon="📜")

#     # Header section
#     st.title("🌟 Random Quote Engine")
#     st.write("Need inspiration? Click the button below to pull a quote from the web.")

#     # Container for the quote to keep the layout clean
#     quote_container = st.container()

#     # The Button - This is the "Trigger"
#     if st.button('✨ Generate New Quote', use_container_width=True):
#         with st.spinner('Fetching wisdom...'):
#             data = fetch_quote()
            
#             if data:
#                 with quote_container:
#                     st.markdown("---")
#                     st.subheader(f"\"{data['content']}\"")
#                     st.write(f"**— {data['author']}**")
#                     st.caption(f"Tags: {', '.join(data['tags'])}")
#                     st.markdown("---")
#             else:
#                 st.warning("We couldn't grab a quote. Check your internet connection!")

def main():
    st.set_page_config(page_title="Quote Gen", page_icon="📜")

    st.title("🌟 Random Quote Engine")
    st.write("Need inspiration? Click the button below.")

    quote_container = st.container()

    if st.button('✨ Generate New Quote', use_container_width=True):
        with st.spinner('Fetching wisdom...'):
            data = fetch_quote()
            
            if data:
                with quote_container:
                    st.markdown("---")
                    # data['content'] and data['author'] exist in our new fetch function
                    st.subheader(f"\"{data['content']}\"")
                    st.write(f"**— {data['author']}**")
                    # REMOVED the Tags line because ZenQuotes doesn't provide them
                    st.markdown("---")
            else:
                st.warning("We couldn't grab a quote. Check your internet connection!")

# Run the app
if __name__ == "__main__":
    main()