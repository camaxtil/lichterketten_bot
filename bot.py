import helpers, pylogs, yaml
from twitchio.ext import commands
with open("config.yaml") as file:
	config = yaml.load(file, Loader=yaml.FullLoader)

bot = commands.Bot(
	irc_token=config["token"],
	client_id=config["client_id"],
	nick=config["nick"],
	prefix=config["prefix"],
	initial_channels=[config["channel"]]
)
bot.web_socket = bot._ws
bot.channel_id = helpers.channel.get_channel_id()

if __name__ == "__main__":
	for extension in config["startup_cogs"]:
		try:
			bot.load_module(extension)
			print(f"Loaded extension '{extension.replace('scripts.', '')}'")
		except Exception as e:
			exception = f"{type(e).__name__}: {e}"
			print(f"Failed to load extension {extension.replace('scripts.', '')}\n{exception}")


@bot.event
async def event_command_error(context, error):
	# An argument has not been given
	if isinstance(error, commands.MissingRequiredArgument):
		return pylogs.error("A user tried to execute a command but it was missing an argument!", color=config["colored_logs"])
	# A command check has failed
	elif isinstance(error, commands.CheckFailure):
		return pylogs.error("A user tried to execute a command but it failed a check (probably not moderator)!", color=config["colored_logs"])
	# The command is not existing
	elif isinstance(error, commands.CommandNotFound):
		return pylogs.error("A user tried to execute a command but the command was not existing!", color=config["colored_logs"])
	# Wrong data type as argument
	elif isinstance(error, commands.BadArgument):
		return pylogs.error("A user tried to execute a command but an argument was in a wrong data type!", color=config["colored_logs"])
	raise error

# Run the bot
bot.run()