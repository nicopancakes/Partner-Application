import discord as d
i = d.Intents.default(); i.messages = True
B = d.Client(intents=i)
t,c,m = input("T >"), int(input("C >")), input("M >")
@B.event
async def on_message(x):
    if x.channel.id == c and x.author != B.user:
        await x.channel.send(m)
B.run(t)