

import openai


promt = input("search anything: ")



openai.api_key = "access token here"

output = openai.ChatComletion.create(
  model = "gpt-3.5-turbo",
  message=[{"role":"user",
  "content":promt}]

) 

print(output)