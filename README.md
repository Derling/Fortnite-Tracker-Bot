# Fortnite-Tracker-Bot
A discord bot that displays solos, duos, and squads stats for a player on any platform

## Requirements

Install [python3.6](https://www.python.org/downloads/) <br/>
Create an api key for [Fortnite Tracker](https://fortnitetracker.com/site-api) <br/>
[Use pip to install discord.py](https://pypi.org/project/discord.py/) <br/>
[Clone](https://git-scm.com/docs/git-clone) this repository somewhere on your machine!

## Create the bot! *

### Create a server
If you don't already have a server, create one for free at https://discordapp.com. Simply log in, and then click the plus on the left side of the main window and create a new server.

### Create an app
Go to https://discordapp.com/developers/applications/me and create a new app. On your app detail page, save the Client ID. You will need it later to authorize your bot for your server.

### Create a bot account for your app
After creating app, on the app details page, scroll down to the section named bot, and create a bot user. **Save the token, you will need it later to run the bot.**

### Authorize the bot for your server
Visit the URL https://discordapp.com/oauth2/authorize?client_id=XXXXXXXXXXXX&scope=bot but replace XXXX with your app client ID. Choose the server you want to add it to and select authorize.

## Update constants

### bot_constants
In bot_constants.py replace the string in TOKEN to the token that was generated for your discord bot

### client_constants
In client_constants.py replace the string in KEY to the key that was generated for your Fortnite Tracker account.

## Activate the bot
[Run](https://www.pythoncentral.io/execute-python-script-file-shell/) the bot.py file! <br/>
In the command line you should see something like: <br/>
```
Logged in as
fortnite-tracker
012345678901234567
------
```

## How to use the bot
Currently the bot supports looks ups on overall, season 3 and season 4 stats. <br/>
To trigger the bot use ` !tracker {epic_name} {platform} ` <br/>

### Overall stats lookup
To lookup the overall stats of a person, type ` !tracker {epic_name} {platform} all ` <br/>
The `all ` is optional but is used to explicitly show others in the server what you were looking for. ` !tracker {epic_name} {platform} ` works in the same way.

### Season 3 stats lookup
To lookup the season 3 stats of a person, type ` !tracker {epic_name} {platform} season3 ` </br>
This is **not** case-sensitive so ` !tracker {epic_name} {platform} Seasson3 ` also works

### Season 4 stats lookup
To lookup the season 4 stats of a person, type ` !tracker {epic_name} {platform} season4 ` </br>
This is **not** case-sensitive so ` !tracker {epic_name} {platform} Seasson4 ` also works

## Examples
` !tracker ninja pc ` would have the bot write: <br/>
ninja's overall stats are:  <br/>
solos:     11.8 KD 3416 Games <br/>
duos:      12.58 KD 2691 Games <br/>
squads:   7.91 KD 1508 Games <br/>
<br/> <br/>
` !tracker ninja pc season3 ` would have the bot write: <br/>
ninja's season3 stats are: <br/>
solos:     12.55 KD 1064 Games <br/>
duos:      15.73 KD 951 Games <br/>
squads:   9.4 KD 429 Games <br/>
<br/> <br/>
` !tracker ninja pc season4 ` would have the bot write: <br/>
ninja's season4 stats are: <br/>
solos:     15.8 KD 123 Games <br/>
duos:      14.35 KD 108 Games <br/>
squads:   23.64 KD 76 Games <br/>
<br/>
*The steps for creating a bot were taken from [here](https://www.devdungeon.com/content/make-discord-bot-python)
