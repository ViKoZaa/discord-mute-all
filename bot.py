import discord

TOKEN = ""

client = discord.Client()

def get_channels(guild):
    list = []
    for channel in guild.voice_channels:
        list.append(channel.id)
    return list


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send("Willkommen auf dem Server!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Muten
    if message.content == "!muteall":
        if message.author.voice is not None:
            channels_list = get_channels(message.author.guild)
            channel_index = channels_list.index(message.author.voice.channel.id)
            for member in message.author.guild.voice_channels[channel_index].members:
                # Rolle erstellen
                role = discord.utils.get(message.author.guild.roles, name="Muted")
                if not role:
                    try:
                        await message.author.guild.create_role(name="Muted", reason="Used for muting", colour=discord.Colour(0xFF0000))
                    except discord.Forbidden:
                        return await message.author.send("I have no permissions to make a muted role")
                role = discord.utils.get(message.author.guild.roles, name='Muted')
                await member.add_roles(role)
            await message.channel.send('Alle gemutet')
        else:
            await message.channel.send('Du bist in keinem Voice Channel')

    # Entmuten
    if message.content == "!unmuteall":
        if message.author.voice is not None:
            channels_list = get_channels(message.author.guild)
            channel_index = channels_list.index(message.author.voice.channel.id)
            for member in message.author.guild.voice_channels[channel_index].members:
                role = discord.utils.get(message.author.guild.roles, name='Muted')
                await member.remove_roles(role)
            await message.channel.send('Alle entmutet')
        else:
            await message.channel.send('Du bist in keinem Voice Channel')

    if message.content == "severin355":
        for member in message.author.guild.voice_channels[channel_index].members:
            await member.edit(nick="severin355")

client.run(TOKEN)
