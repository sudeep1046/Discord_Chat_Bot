import discord
import requests
from discord.ext import commands
import os
from keep_alive import keep_alive
import random
import openai


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}, I am your loyal bot!')

@bot.command()
async def motivate(ctx):
    quotes = [
        "Push yourself, because no one else is going to do it for you.",
        "Great things never come from comfort zones.",
        "Do something today that your future self will thank you for.",
        "Success doesn’t just find you. You have to go out and get it.",
        "Dream it. Wish it. Do it."
    ]
    await ctx.send(random.choice(quotes))

import random  # Add this at the top of your file if not already

@bot.command()
async def joke(ctx):
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the programmer quit his job? Because he didn't get arrays.",
        "Why did the computer show up at work late? It had a hard drive!",
        "Why was the robot angry? Because someone kept pushing its buttons!"
    ]
    await ctx.send(random.choice(jokes))



@bot.command()
async def weather(ctx, *, city: str):
    api_key = "YOUR_API_KEY"  # ← Replace with your real API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()

    if data["cod"] != 200:
        await ctx.send(f"❌ Could not find weather for **{city}**.")
        return

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"].capitalize()
    await ctx.send(f"🌤️ Weather in **{city}**: {desc}, {temp}°C")





# Keep the bot alive
keep_alive()

# Run the bot
bot.run("PASTE YOUR TOKEN")
