from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import numpy as np
import cv2
import pyautogui
import base64
import requests


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


api_key = ""  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

messages = []


# message = ("find cartoon\"The Road Runner Show\" for this position on the site. ONLY phrases can be used: "
#           "scroll down scroll up found (ONLY ONE PHRASE and without dots and comas!!!)")
# image_path = "oleh.png"
def analyze(counter):
    for i in range(counter):
        message = ("Write me your opinion as a professional UI/UX designer about this page in general in bulletpoints "
                   "(ONLY important things). What is good? What can be better?")  # input("User: ")
        image_path = "image" + str(i+1) + ".png"
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
