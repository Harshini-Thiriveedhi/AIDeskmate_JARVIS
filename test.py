import os
import openai

from config import apikey

openai.api_key =apikey


response = openai.Completion.create(
  model="text-davinci-003",
  prompt="write an email to boss for resignation?",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response.choices[0].message.content)


