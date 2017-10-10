# Dark Autumn
Sanity - 5 points

## Challenge 
> We've just trained our Discord moderator-bot to understand the seasons of the year. Since it's currently autumn, perhaps you can ask our bot to shed some light on it? Type !help within our Discord server to get the help menu from moderator-bot.

## Solution

Type `!help` and we get this message

	Red - A multifunction Discord bot by Twentysix

	CustomCommands:
	  customcom  Custom commands management
	General:
	  8          Ask 8 ball a question
	  choose     Chooses between multiple choices.
	  flip       Flips a coin... or a user.
	  lmgtfy     Creates a lmgtfy link
	  poll       Starts/stops a poll
	  roll       Rolls random number (between 1 and user choice)
	  rps        Play rock paper scissors
	  serverinfo Shows server's informations
	  stopwatch  Starts/stops stopwatch
	  urban      Urban Dictionary search
	  userinfo   Shows users's informations
	Mod:
	  names      Show previous names/nicknames of a user
	Owner:
	  contact    Sends a message to the owner
	  info       Shows info about Red
	  set        Changes Red's core settings
	  uptime     Shows Red's uptime
	  version    Shows Red's current version
	Seasons:
	  autumn     Print autumn definition
	​No Category:
	  help       Shows this message.

	Type !help command for more info on a command.
	You can also type !help category for more info on a category.

Type `!autumn` and we get this message
	
	Autumn is the year's last, loveliest smile. Find out more at autumniqa7dc3j4p.onion! Visit either with a Tor browser, or perhaps even onion.casa!

We need Tor to view the flag.

	$ torsocks curl -s autumniqa7dc3j4p.onion | html2text
	It's so strange how autumn is so beautiful,
	yet everything is dying.
	GCTF{d4rk_hum0r_15_b357_hum0r}

## Flag
`GCTF{d4rk_hum0r_15_b357_hum0r}`
