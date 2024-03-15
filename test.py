pip install langchain
pip install transformers

from transformers import pipeline
from langchain import LLMChain, PromptTemplate
from langchain import HuggingFaceHub
import matplotlib.pyplot as plt

#convert an image to text using an image captioning model
def img2text(url):
  pipe =pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
  text =pipe(url)[0]["generated_text"]
  return text

print(img2text("bird.jpg"))

repo_id ="tiiuae/falcon-7b-instruct"

hf_token="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"
llm = HuggingFaceHub(huggingfacehub_api_token=hf_token,
                     repo_id=repo_id,
                     verbose=False,
                     model_kwargs={"temperature":0.1, "max_new_tokens":1500})

def generate_story(scenario, llm):
  template= """You are a story teller.
               You get a scenario as an input text, and generates a short story out of it.
               Context: {scenario}
               Story:
               """
  prompt =PromptTemplate(template=template, input_variables=["scenario"])

  #let's create our LLM chain now.
  chain = LLMChain(prompt=prompt, llm=llm)
  story = chain.predict(scenario=scenario)
  return story

scenario = "A man is walking in a dark street."
print(generate_story(scenario, llm))

import requests
def text2speech(text):
    API_URL = "https://api-inference.huggingface.co/models/facebook/mms-tts-eng"
    headers = {"Authorization": "Bearer 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"}
    payload ={"inputs": text}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content



img_file="child.jpg"
img = plt.imread(img_file)
plt.imshow(img)

scenario = img2text(img_file)
print(scenario)
story = generate_story(scenario, llm)
print(story)
audio_bytes = text2speech(story)

# You can access the audio with IPython.display for example
from IPython.display import Audio
Audio(audio_bytes)