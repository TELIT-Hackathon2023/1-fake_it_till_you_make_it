import os

import numpy as np
import cv2
import pyautogui
import base64
import requests
import mouse
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import base64


class web_controller:

    def __init__(self):
        self.chrome_options = Options()

        self.driver = webdriver.Chrome(options=self.chrome_options)

        self.driver.execute_script("return window.performance.timing.loadEventEnd")
        self.driver.maximize_window()
        self.y = 0

    def open_web(self, page):
        start_time = time.time()
        self.driver.get(page)

        load_time = time.time() - start_time
        print(f"Page Load Time: {load_time:.8f} seconds")

    def close_web(self):
        self.driver.close()

    def scroll_down(self):
        height = self.driver.execute_script("return document.body.scrollHeight")
        self.y += 1000
        if self.y > height:
            self.y = height
        self.driver.execute_script(f"window.scrollTo(0, {self.y});")

    def scroll_up(self):
        self.y -= 500
        if self.y < 0:
            self.y = 0
        self.driver.execute_script(f"window.scrollTo(0, {self.y});")

    def screenshot(self, counter:int):
        self.driver.save_screenshot("image"+str(counter)+".png")

