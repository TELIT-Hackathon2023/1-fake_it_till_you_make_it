from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import numpy as np
import cv2
import pyautogui
import base64
import requests
from AI import web_controller


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


api_key = "" #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

wb = web_controller()
wb.open_web("https://www.browserstack.com/guide/ideal-screen-sizes-for-responsive-design")

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
cv2.imwrite("image1.png", image)


messages = []

while True:
    message = input("User: ")
    image_path = input("")

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

