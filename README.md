# ChatGPT Interface

**A Python interface for interacting with ChatGPT via web interface using Selenium.**

This tool allows you to automate interactions with the ChatGPT web interface using Selenium, providing an efficient way to send prompts and receive responses programmatically.

---

## Installation

Before using this interface, ensure you have Python and pip installed. Install the required package with the following command:

```bash
pip install chatgpt_interface
```

---

## Usage

Here's an example of how to use the ChatGPT interface.

```python
from chatgpt_interface import ChatGPTInterface

# Path to the Chrome profile
profile_path = "D:/Projects/SpicaNet/Dev/Chrome/profiles/Profile1"

# URL of the ChatGPT web interface
chat_url = "https://chatgpt.com/"

# List of prompts for the ChatGPT model
prompts = ["Write article about Chocolate", "Write FAQ for this article", "Write meta description for this article"]

# Output file to save the responses
output_file = "responses.txt"

# Create an instance of the ChatGPTInterface
chatgpt = ChatGPTInterface(profile_path, chat_url, prompts)

# Open the chat interface
chatgpt.open_chat()

# Process the prompts and get the responses
responses = chatgpt.process_prompts()

# Save the Chrome profile
chatgpt.save_profile()

# Write the responses to the output file
with open(output_file, 'w', encoding='utf-8') as file:
    for prompt, response in responses:
        file.write(f"Prompt: {prompt}\nResponse: {response}\n\n")
```

---

## Parameters

-   **`profile_path`**: The path to your Chrome profile. This allows the script to reuse your Chrome profile settings, including your logged-in session to the ChatGPT web interface.
-   **`chat_url`**: The URL of the ChatGPT web interface.
-   **`prompts`**: A list of prompts/questions that you want to send to ChatGPT.
-   **`output_file`**: The file where the responses will be saved.

---

## Main Functions

-   **`ChatGPTInterface(profile_path, chat_url, prompts)`**: Initializes the ChatGPT interface with the Chrome profile, the ChatGPT URL, and a list of prompts.
-   **`open_chat()`**: Opens the ChatGPT web interface using Selenium.
-   **`process_prompts()`**: Sends the prompts one by one to the ChatGPT web interface and retrieves the responses.
-   **`save_profile()`**: Saves the current Chrome profile to preserve login and session data.

---

## Saving Responses

The responses from ChatGPT are saved in the `responses.txt` file, where each prompt and its corresponding response are written in the following format:

The best proxies for any task: https://oneproxy.pro
