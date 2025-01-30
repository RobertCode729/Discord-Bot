# import random

# fig = '+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
# length = int(input('Podaj prosze dlugosc hasla:'))
# password = ''

# for i in range(length):
#     x = random.randint(0,72)
#     password += fig[x]

# print(password)



#pip install discord, audioop-lts
 
import discord
 
# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej client i przekazanie mu uprawnień
client = discord.Client(intents=intents)
 
@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')
import random 
jokes = ['What time is it when the clock strikes 13?', 'How are false teeth like stars?', 'Why does a seagull fly over the sea?', 'When you look for something, why is it always in the last place you look?', 'Why do some couples go to the gym?', 'Did you know?', 'What kind of music do chiropractors like?', ' I was going to tell a time-traveling joke']
answer =['Time to get a new clock.', 'They come out at night.', 'Because if it flew over the bay, it would be a baygull.', 'Because when you find it, you stop looking.', 'Because they want their relationship to work out.', '5/4 of people admit they are bad at fractions.', 'Hip pop', 'but you did not like it.']
facts = ['Tic Tacs got their name from the sound they make when they are tossed around in their container.', 'Mercury and Venus are the only two planets in our solar system that do not have any moons.', 'Lettuce is a member of the sunflower family.', 'The color red does not really make bulls angry; they are color-blind.', 'There is a company that sells mirrors that make people look 10 pounds thinner.', 'Violin bows are commonly made from horse hair.', 'The voice actors of SpongeBob and Karen, Plankton’s computer wife, have been married since 1995.', 'A single strand of Spaghetti is called a “Spaghetto.”']
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("hi"):
        await message.channel.send("Welcome, " + str(message.author))
    elif message.content.startswith("bye"):
        await message.channel.send("\U0001f642")
    elif message.content.startswith("password"):
        fig = '+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        password = ''
        for i in range(int(message.content.split(" ")[-1])):
            x = random.randint(0,72)
            password += fig[x]
        await message.channel.send('Your randomised password is: ' + password)
    elif message.content.startswith("joke"):
        y=random.randint(0,7)
        await message.channel.send(jokes[y])
        await message.channel.send(answer[y])
    elif message.content.startswith("fact"):
        z=random.randint(0,7)
        await message.channel.send(facts[z])
    else:
        await message.channel.send("You can use the following commands")
        await message.channel.send("hi, bye, password (yournumber), joke, fact")

client.run("TOKEN")