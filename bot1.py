import discord
from discord.ext import commands
import asyncio
import sys
import random
import operator
from Upload_bot.bot_token import *
import os
import json
import pickledb
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

db = pickledb.load('discord.db', True)


@client.event
async def on_ready():
    print("Evil Romeo online.")
    print("------------------")


@client.command()
async def balance(ctx):
    author = str(ctx.author)
    if not db.exists(author): #if username is not in database
        db.set(author, 500)
        await ctx.reply(f'`Account made! your current balance is {db.get(author)}$`')
    else:
        await ctx.reply(f'`Your current balance is {db.get(author)}$`')

@client.command()
async def slots(ctx):
    author = str(ctx.author)
    if db.get(author) < 30:
        await ctx.reply(f'`you dont have enough money! your balance is {db.get(author)}$`')
    else:
        db.append(author, -30)
        

#picks random options
        author = str(ctx.author) #sets user as author of message
        slot_options = ["<:cat_sunglasses:1209765973247402038>",
                        "<:Cat_OO:1209765972504870982>",
                        "<:cat_milk:1209765971162824734>",
                        "<:Cat_Mewing:1209765969916993576>",
                        "<:cat_drank:1209765968478470197>",
                        "<:Cat_Bleh:1209765967048081448>",
                        "<:Cat_Apple:1209765965953372210>"]

        Pos1 = random.choice(slot_options)
        Pos2 = random.choice(slot_options)
        Pos3 = random.choice(slot_options)


#places three randomized variables in order

        slot_results = [Pos1,Pos2,Pos3]

#sends edited sequence

        message1 = await ctx.send("  [  "+":black_large_square:" +"  |  "+":black_large_square:"+"  |  "":black_large_square:""  ]  ")
        await asyncio.sleep(.5)
        await message1.edit(content="  [  "+Pos1+"  |  :black_large_square:  |  :black_large_square:  ]  ")
        await asyncio.sleep(.5)
        await message1.edit(content="  [  "+Pos1 +"  |  "+Pos2 +"  |  :black_large_square:  ]  ")
        await asyncio.sleep(.5)
        await message1.edit(content="  [  "+Pos1 +"  |  "+Pos2 +"  |  "+Pos3+"  ]  ")


#convert this to sending a discord message
   
        print (slot_results,"edited")


        ##############
        if operator.countOf(slot_results, "<:cat_milk:1209765971162824734>") == 3:
            await ctx.send("Three cats falling in milk, they are all so clumsy!")
            db.append(author, 110) #adds to users count
            await ctx.reply(f'`you won 110$ your new balance is {db.get(author)}$`')

        if operator.countOf(slot_results, "<:cat_milk:1209765971162824734>") == 2:
            await ctx.send("Two cats in milk!")
            db.append(author, 50) #adds to users count
            await ctx.reply(f'`you won 50$ your new balance is {db.get(author)}$`')
            ##############
        if operator.countOf(slot_results, "<:cat_drank:1209765968478470197>") == 3:
            await ctx.send("drank.")
            db.append(author, 150) #adds to users count
            await ctx.reply(f'`you won 150$ your new balance is {db.get(author)}$ tralalala`')

        if operator.countOf(slot_results, "<:cat_drank:1209765968478470197>") == 2:
            await ctx.send("two dranks :3")
            db.append(author, 60) #adds to users count
            await ctx.reply(f'`you won 60$ your new balance is {db.get(author)}$`')
            ###############
        if operator.countOf(slot_results, "<:Cat_OO:1209765972504870982>") == 3:
            await ctx.send("O-O")
            db.append(author, 200) #adds to users count
            await ctx.reply(f'`you won 200$ your new balance is {db.get(author)}$`')

        if operator.countOf(slot_results, "<:Cat_OO:1209765972504870982>") == 2:
            await ctx.send("two jinx cats...")
            db.append(author, 70) #adds to users count
            await ctx.reply(f'`you won 70$ your new balance is {db.get(author)}$`')
            ##############
        if operator.countOf(slot_results, "<:Cat_Mewing:1209765969916993576>") == 3:
            await ctx.send("The ratchetest")
            db.append(author, 300) #adds to users count
            await ctx.reply(f'`you won 300$ your new balance is {db.get(author)}$`')

        if operator.countOf(slot_results, "<:Cat_Mewing:1209765969916993576>") == 2:
            await ctx.send("a little ratchet")
            db.append(author, 80) #adds to users count
            await ctx.reply(f'`you won 80$ your new balance is {db.get(author)}$`')
            ##############
        if operator.countOf(slot_results, "<:Cat_Bleh:1209765967048081448>") == 3:
            await ctx.send(":P :P :P")
            db.append(author, 400) #adds to users count
            await ctx.reply(f'`you won 400$ your new balance is {db.get(author)}$`')

        if operator.countOf(slot_results, "<:Cat_Bleh:1209765967048081448>") == 2:
            await ctx.send(":P :P")
            db.append(author, 90) #adds to users count
            await ctx.reply(f'`you won 90$ your new balance is {db.get(author)}$`')
            ###############
        if operator.countOf(slot_results, "<:cat_sunglasses:1209765973247402038>") == 3:
            await ctx.send("RAHHHHHHHH")
            db.append(author, 500) #adds to users count
            await ctx.reply(f'`you won 500 bands :3 new balance is {db.get(author)}$`')

        if operator.countOf(slot_results, "<:cat_sunglasses:1209765973247402038>") == 2:
            await ctx.send("Two Cool <:cat_sunglasses:1209765973247402038> ")
            db.append(author, 100) #adds to users count
            await ctx.reply(f'`you won 100$ your new balance is {db.get(author)}$`')
            ###############
        if operator.countOf(slot_results, "<:Cat_Apple:1209765965953372210>") == 3:
            await ctx.send("Your greed is immeasurable.")
            db.append(author, 1000) #adds to users count
            await ctx.reply(f'`you won gambling  +$1000 your new balance is {db.get(author)}$`')

        if operator.countOf(slot_results, "<:Cat_Apple:1209765965953372210>") == 2:
            await ctx.send("Be careful of your greed.")
            db.append(author, 150) #adds to users count
            await ctx.reply(f'`you won 150 your new balance is {db.get(author)}$, but tame your gluttony.`')

    #detects if there are no matches

        set_slot_results = set(slot_results)

        if len(set_slot_results) == len(slot_results):
            await ctx.send(f'`no matches! Your new balance is {db.get(author)}$`')
            print ("no matches!")


client.run(TOKEN)

