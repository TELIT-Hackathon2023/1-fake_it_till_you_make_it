import base64

import openai

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

openai.api_key = ''  # Replace with your actual API key


image_path = "C:/Users/Vasyl/Pictures/Screenshots/Знімок екрана 2023-04-11 183302.png"
base64_image = encode_image(image_path)
# Getting the base64 string
messages = []

while True:
    message = input("User: ")
    if message and message != "ano":
        messages.append({"role": "user", "content": message})
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the appropriate engine for your needs
            prompt=" ".join([m['content'] for m in messages]),
            max_tokens=150
        )

        reply = response['choices'][0]['text']
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})
    else:
        message = base64_image
        messages.append({"role": "user", "content": message})
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the appropriate engine for your needs
            prompt=" ".join([m['content'] for m in messages]),
            max_tokens=150
        )

        reply = response['choices'][0]['text']
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})

