# Python program to take
# screenshots 


import numpy as np
import cv2
import pyautogui
import base64
import requests

image = pyautogui.screenshot()


image = cv2.cvtColor(np.array(image),
                     cv2.COLOR_RGB2BGR)
cv2.imwrite("image1.png", image)

# writing it to the disk using opencv 
#cv2.imwrite("image1.png", image)

api_key  =

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "image1.png"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "what do you see in this image?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())

