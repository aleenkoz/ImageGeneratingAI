#install and import all the necessary packages and libraries related to image generating and OpenAI.
pip install Pillow 

import openai
from openai import OpenAI

import os
import json
import base64
import io
import time
import uuid

from IPython.display import Image, display
from PIL import Image as PILImage

from pathlib import Path

#Assign the key and client to enable the use of OpenAI functions.
os.environ["OPENAI_API_KEY"] = 'Your OpenAI key here'
client= OpenAI()

#Image generating is used by calling these methods
response = client.images.generate(
    prompt="A washing machine working in the desert.", #What is it that you want to generate?
    n=4, #How many pictures do you want to generate?
    size="256x256" #In what size would you like to see your generated images in?
)
response #Showing the generated Image in URL.

Image(url=response.data[0].url) #Changing the long useless URL into a useful and easily shown format.


response2 = client.images.generate(
    prompt="A group of monkeys playing volleyball.",
    n=1,
    size="256x256",
    response_format="b64_json" #included to help show the image instantly.
)
response2

image_data = base64.b64decode(response2.data[0].b64_json)
image = PILImage.open(io.BytesIO(image_data))
display(image)

#lets sum it all up into a well written function 
def generating(
    prompt, model="dall-e-3", #dall-e-2 is chosen always by default if not changed.
    n=1, size= "1024x1024", style="vivid", quality="standard"):
        responsing= client.images.generate(
            prompt= prompt,
            model= model,
            n=n,
            size = size,
            style = style,
            quality = quality
        )
        image_urls = [entry.url for entry in responsing.data]
        return image_urls

print("please enter a discription of what you want generated in an image:")
prompt= input()
image_urls = generating(prompt) #The developer is able to choose to change the default parameters, by defining aand initializing them, and then asigning them in the function's parameters.
for url in image_urls:
   display(Image(url=url))
   