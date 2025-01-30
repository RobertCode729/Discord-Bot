import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def password(pas):
    fig = '+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    print('ddd ', pas)
    passw0rd = ''
    for i in range (int(pas.message.content[len("!password "):])):
        x = random.randint(0,72)
        passw0rd += fig[x]
    await pas.send(passw0rd)
   
# @bot.event()
# async def on_ready():
#     print(f'Zalogowaliśmy się jako {bot.user}')
# import random 
# jokes = ['What time is it when the clock strikes 13?', 'How are false teeth like stars?', 'Why does a seagull fly over the sea?', 'When you look for something, why is it always in the last place you look?', 'Why do some couples go to the gym?', 'Did you know?', 'What kind of music do chiropractors like?', ' I was going to tell a time-traveling joke']
# answer =['Time to get a new clock.', 'They come out at night.', 'Because if it flew over the bay, it would be a baygull.', 'Because when you find it, you stop looking.', 'Because they want their relationship to work out.', '5/4 of people admit they are bad at fractions.', 'Hip pop', 'but you did not like it.']
# facts = ['Tic Tacs got their name from the sound they make when they are tossed around in their container.', 'Mercury and Venus are the only two planets in our solar system that do not have any moons.', 'Lettuce is a member of the sunflower family.', 'The color red does not really make bulls angry; they are color-blind.', 'There is a company that sells mirrors that make people look 10 pounds thinner.', 'Violin bows are commonly made from horse hair.', 'The voice actors of SpongeBob and Karen, Plankton’s computer wife, have been married since 1995.', 'A single strand of Spaghetti is called a “Spaghetto.”']
# @bot.event
# async def on_message(message):
    

bot.run("YOUR SECRET TOKEN!!!")
