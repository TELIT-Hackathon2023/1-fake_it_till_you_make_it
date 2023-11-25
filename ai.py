from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import numpy as np
import cv2
import pyautogui
import base64
import requests
import mouse


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


chrome_options = Options()

driver = webdriver.Chrome(options=chrome_options)

driver.execute_script("return window.performance.timing.loadEventEnd")
driver.maximize_window()
start_time = time.time()
driver.get("https://www.browserstack.com/guide/ideal-screen-sizes-for-responsive-design")

load_time = time.time() - start_time
print(f"Page Load Time: {load_time:.8f} seconds")

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
cv2.imwrite("image1.png", image)

time.sleep(5)

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

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

        reply = response['choices'][0]['text']
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})

driver.close()

