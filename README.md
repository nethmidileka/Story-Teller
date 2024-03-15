# Story-Teller

# LangChain

LangChain is a project that utilizes language models to generate short stories from images.


## Installation

Before running the code, make sure you have Python installed on your system. You can install the required packages using pip:

```bash
pip install langchain
pip install transformers
```

## Usage

To convert an image into a story, you can use the provided functions in the langchain module. Here's a basic example:
```bash
from langchain import img2text, generate_story, text2speech

# Path to your image file
img_file = "example.jpg"

# Convert image to text
scenario = img2text(img_file)

# Generate story based on the image scenario
story = generate_story(scenario, llm)

# Convert story to speech
audio_bytes = text2speech(story)
````
Make sure to replace "example.jpg" with the path to your actual image file.

## Dependencies
  langchain
  transformers
  matplotlib (if using image processing)

## Example
You can find a basic example of how to use LangChain in the example.py file in this repository.

## Credits
LangChain is powered by Hugging Face's transformers library and other open-source technologies.

## More refer:
 ````bash
https://youtu.be/rTeeWq-jNh8?si=CO8gbLK3g90KRi1Q
````


