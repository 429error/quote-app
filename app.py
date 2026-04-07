import streamlit as st
import requests

# --- CONFIGURATION ---
API_URL = "https://api.quotable.io/random"

# --- LOGIC: FETCHING DATA ---

def fetch_quote():
    """Fetches a random quote from the ZenQuotes API."""
    try:
        # ZenQuotes API
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

def main():
    st.set_page_config(page_title="Quote Gen", page_icon="📜")

    st.title(" Random Quote Engine ")
    st.write("Need inspiration? Click the button below.")

    quote_container = st.container()

    if st.button('Generate New Quote', use_container_width=True):
        with st.spinner('Fetching wisdom...'):
            data = fetch_quote()
            
            if data:
                with quote_container:
                    st.markdown("---")
                    st.subheader(f"\"{data['content']}\"")
                    st.write(f"**— {data['author']}**")
                    st.markdown("---")
            else:
                st.warning("We couldn't grab a quote. Check your internet connection!")

# Run the app
if __name__ == "__main__":
    main()