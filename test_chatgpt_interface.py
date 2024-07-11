from chatgpt_interface import ChatGPTInterface

if __name__ == "__main__":
    profile_path = "/var/www/spicanet/data/dev/Chrome/Default"
    chat_url = "https://chat.openai.com/"
    prompts = ["Write article\nabout\nChocolate", "Write FAQ\nfor this article", "Write meta description for this article"]
    output_file = "responses.txt"

    chatgpt = ChatGPTInterface(profile_path, chat_url, prompts)
    chatgpt.open_chat()
    responses = chatgpt.process_prompts()
    chatgpt.save_profile()

    with open(output_file, 'w', encoding='utf-8') as file:
        for prompt, response in responses:
            file.write(f"Prompt: {prompt}\nResponse: {response}\n\n")
