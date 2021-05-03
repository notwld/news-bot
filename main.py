import requests  
from newsapi import NewsApiClient
from random import choice,sample
import discord
from discord.ext import tasks,commands


def news_tech():

      query_params = {"source": "the-verge",
            "sortBy": "top",
            "apiKey": "INSERT UR API KEY" #goto newsapi website for more info
      }
      main_url = " https://newsapi.org/v1/articles"
      
      
      res = requests.get(main_url, params=query_params)
      open_page = res.json()
      
      # getting all articles in a string article
      article = open_page["articles"]
      
      # empty list which will
      # contain all trending news
      results = []
      tech_news=[]
      for ar in article:
            results.append('__By: '+str(ar['author'])+'__'+'\n'+'**'+str(ar["title"])+'**'+'\n'+'_'+str(ar['description'])+'_'+'\n'+str(ar['url']))
            
      for i in range(len(results)):
            tech_news.append(results[i])

      return choice(tech_news)

def news_bbc():

      query_params = {"source": "bbc-news",
            "sortBy": "top",
            "apiKey": "INSERT UR API KEY"
      }
      main_url = " https://newsapi.org/v1/articles"
      
      
      res = requests.get(main_url, params=query_params)
      open_page = res.json()
      
      # getting all articles in a string article
      article = open_page["articles"]
      
      # empty list which will
      # contain all trending news
      results = []
      bbc_news=[]
      for ar in article:
            results.append('__By: '+str(ar['author'])+'__'+'\n'+'**'+str(ar["title"])+'**'+'\n'+'_'+str(ar['description'])+'_'+'\n'+str(ar['url']))
            
      for i in range(len(results)):
            bbc_news.append(results[i])

      return choice(bbc_news)


def news_ign():

      query_params = {"source": "ign",
            "sortBy": "top",
            "apiKey": "INSERT UR API KEY"
      }
      main_url = " https://newsapi.org/v1/articles"
      
      
      res = requests.get(main_url, params=query_params)
      open_page = res.json()
      
      # getting all articles in a string article
      article = open_page["articles"]
      
      # empty list which will
      # contain all trending news
      results = []
      an_news=[]
      for ar in article:
            results.append('__By: '+str(ar['author'])+'__'+'\n'+'**'+str(ar["title"])+'**'+'\n'+'_'+str(ar['description'])+'_'+'\n'+str(ar['url']))
            
      for i in range(len(results)):
            an_news.append(results[i])

      return choice(an_news)



client=discord.Client()

@client.event
async def on_ready():
  print('Loaded')
  activity = discord.Game(name="@news-bot", type=3)
  await client.change_presence(status=discord.Status.idle, activity=activity)


key1=r'\news-tech'
key2=r'\news-bbc'
key3=r'\news-ign'

@client.event
async def on_message(message):
        if message.content==key1:
              await message.channel.send(news_tech())
        if message.content==key2:
              await message.channel.send(news_bbc())
        if message.content==key3:
              await message.channel.send(news_ign())
        if client.user.mentioned_in(message):
            a=r'\news-tech'
            b=r'\news-bbc'
            c=r'\news-ign'
            embedVar = discord.Embed(title=f"Thanks for using News-Bot\n--------------------------------\nThis Bot is currently under-development.\nBot Commands: \n{a}\n{b}\n{c}", color=0x00ff00)
            embedVar.set_footer(text='Please Support us.')
            await message.channel.send(embed=embedVar)




client.run(ADD YOUR DISCORD BOT TOKEN HERE) #goto discord dev applications to initialize a bot
