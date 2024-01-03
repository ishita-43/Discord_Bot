# app _id:  1191371401173684364
# public _key : KEYfbc021c233f1e108a8ca4e26a2e2932d8008976c80275383fe49f3581c951c38
# MTE5MTM3MTQwMTE3MzY4NDM2NA.G2UtkQ.ejwd2NzD2AycqGOCEuQaxEK-Nz0GPtU5dMd9LM

import os

import discord

import openai

from openai import OpenAI

with open("chat.txt","r") as f:
  chat =f.read()

openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.getenv("SECRET_KEY")


class MyClient(discord.Client):

  async def on_ready(self):
    print('Logged on as', self.user)

  async def on_message(self, message):
    # don't respond to ourselves
    global chat
    chat += f"{message.author}:{message.content}\n."
    print(f'Message from  {message.author}:  {message.content}')
    print(message.mentions)
    if self.user != message.author:
      if self.user in message.mentions:
          print(chat)
          channel = message.channel
          client = OpenAI()
    
          completion = client.completions.create(
              model="text-davinci-003",
              prompt= f"{chat}\nDis.BOT: ",
              temperature=1,
              max_tokens=256,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0)
          messageToSend = completion.choices[0].text
          # await channel.send('Hello I am a bot ')
          await channel.send(messageToSend)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)
