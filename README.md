## Random Quote Engine

A sleek, web-based Python application that fetches real-time wisdom from the internet and dispalys on the UI
Built with **Streamlit** and powered by the **ZenQuotes API**.

## Features
* **Instant Generation:** Get a new, hand-picked quote with a single click.
* **Dynamic UI:** Clean, responsive web interface.
* **External API Integration:** Connects live to `zenquotes.io` for an endless supply of inspiration.
* **Custom Styling:** Enhanced with CSS for a modern dark look and feel.

## Getting Started

### Prerequisites
Make sure you have **Python 3.8+** installed on your machine.

### Installation
1. **Clone or download** this repository to your local machine.
2. Open your terminal in the project folder and install the necessary libraries:

   ```bash
   pip install streamlit requests 

   Bash
   
streamlit run app.py

The app will automatically open in your default browser at http://localhost:8501.

🛠️ Built With
Python - The core programming language.

Streamlit - The framework used for the web interface.

Requests - For handling HTTP calls to the API.

ZenQuotes API - The source of the random quotes.

📝 How it Works
When the "Generate" button is clicked, a GET request is sent to the ZenQuotes API.

The script parses the returned JSON data.

The UI is updated instantly via Streamlit's reactive rerender logic to display the new content and author.
