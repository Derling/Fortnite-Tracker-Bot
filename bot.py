import discord
import fort_client as fc
from bot_constants import TOKEN, LOOKUP_ALL, LOOKUP_SEASON, \
    SEASONS, INVALID_COMMAND

client = discord.Client()

def format_msg(data, player_name, platform, season='overall'):
    if not data:
        return f'no data for {player_name} on {platform}'
    return (f'{player_name}\'s {season.lower()} stats are: \n' + \
        f"solos:     {data['solos']['kd']} KD {data['solos']['matches']} Games \n" + \
        f"duos:      {data['duos']['kd']} KD {data['duos']['matches']} Games \n" + \
        f"squads:   {data['squads']['kd']} KD {data['squads']['matches']} Games \n")
    

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!tracker'):
        stats_client = fc.Client()
        params = message.content.split()[1:]
        if len(params) == LOOKUP_ALL:
            data = stats_client.send_request(*params)
        elif len(params) == LOOKUP_SEASON and params[-1].casefold() in SEASONS:
            data = stats_client.send_request(*params)
        else:
            await client.send_message(message.channel, INVALID_COMMAND)
            return
        msg = format_msg(data, *params)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)