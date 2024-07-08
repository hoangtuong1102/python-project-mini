# import the following modules
import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact(_):
    """Fetch and display a fun fact from the API"""
    # Clear the screen
    clear()

    # Display the heading with an icon
    put_html("""
        <p align="left">
            <h2>
                <img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%">
                Fun Fact Generator
            </h2>
        </p>
    """)

    # URL to fetch the data
    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    # Use GET request to fetch data
    response = requests.get(url)

    # Load the response as JSON
    data = json.loads(response.text)

    # Extract the 'text' field from the JSON data
    useless_fact = data['text']

    # Display the fact in blue color with large font size
    style(put_text(useless_fact), 'color:blue; font-size: 30px')

    # Display the "Click me" button to fetch another fact
    put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )

# Driver function
if __name__ == '__main__':
    # Display the initial heading with an icon
    put_html("""
        <p align="left">
            <h2>
                <img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%">
                Fun Fact Generator
            </h2>
        </p>
    """)

    # Display the initial "Click me" button to start fetching facts
    put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )

    # Hold the session for a long time
    hold()
