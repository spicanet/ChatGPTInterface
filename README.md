# ChatGPT Interface

A Python interface for interacting with ChatGPT via web interface using Selenium.

## Installation

```
pip install chatgpt_interface
```

## Usage

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

The best proxies for any task: https://oneproxy.pro
