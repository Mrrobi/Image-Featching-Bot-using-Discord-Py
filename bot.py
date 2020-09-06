import discord
import random
from discord.ext import commands
import requests
import urllib.request
import io
import aiohttp
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

client = commands.Bot(command_prefix="?")
team_member = []
member_list = []
team_one = []
team_two = []

@client.event
async def on_ready():
    print("bot ready.")

@client.command()
async def h(ctx):
    # if ctx.message.author.permissions_in(ctx.message.channel):
    await ctx.send(f"1. ?insta <insta photo link>\n2. ?dlink <direct photolink (Any)>\n<@{ctx.message.author.id}>")

@client.command()
async def dlink(ctx,arg):
    async with aiohttp.ClientSession() as session:
        async with session.get(str(arg)) as resp:
            if resp.status != 200:
                return await ctx.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await ctx.send(file=discord.File(data, 'cool_image.png'))

@client.command()
async def insta(ctx,arg):
    # if ctx.message.author.administrator:
    DRIVER_PATH = '.\chrome_driver\chromedriver.exe'
    options = Options()
    options.headless = True
    #options.add_argument("--window-size=1920,1200")
    driver = webdriver.Chrome(options=options,executable_path=DRIVER_PATH)
    driver.get("https://bloodlink.mrrobi.tech/Welcome/?url="+arg)
    driver.execute_script("document.getElementsByClassName('ibutton')[0].click()")
    driver.implicitly_wait(45)
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
        # print(elem.get_attribute("href"))
        async with aiohttp.ClientSession() as session:
            async with session.get(elem.get_attribute("href")) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await ctx.send(file=discord.File(data, 'cool_image.png'))
    # await ctx.send(f"# i am undergoing construction <@{751134170499252244}>"+arg)

client.run("YOUR BOT TOKEN")