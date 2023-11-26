
import time

import base64
import requests
from AI import web_controller
import screenAnalizer


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


api_key = ""  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

wb = web_controller()
wb.open_web("https://www.imdb.com/list/ls069641793/")
time.sleep(5)

counter = 1


wb.screenshot(counter)

messages = []

message = input("User: ")
message = (f"{message} for this position on the site. ONLY phrases can be used: "
           "scroll down scroll up found (ONLY ONE PHRASE and without dots and comas!!!)")


while True:
    image_path = f"image{counter}.png"
    if message:
        base64_image = encode_image(image_path)
        content = [
            {
                "type": "text",
                "text": f"{message}"
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            }
        ]
        messages.append({"role": "user", "content": content})

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": messages,
            "max_tokens": 300
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        print(response.json())
        response_json = response.json()
        reply = response_json['choices'][0]['message']['content']
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": [
            {
                "type": "text",
                "text": f"{message}"
            }
        ]})
        if reply.lower() == "scroll down":
            wb.scroll_down()
        elif reply.lower() == "scroll up":
            wb.scroll_up()
        elif reply.lower() == "found":
            screenAnalizer.analyze(counter)
            break
        else:
            break
        time.sleep(1)

        counter += 1
        wb.screenshot(counter)



