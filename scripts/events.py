import helpers, os, platform, pylogs, twitchio, yaml, time
from twitchio.ext import commands
with open("config.yaml") as file:
    config = yaml.load(file, Loader=yaml.FullLoader)



@commands.cog(name="events")
class Events:
    kette_1 = "7"
    kette_2 = "11"
    kette_3 = "12"
    allowed_user = ["ceda_camaxtil"]

    def __init__(self, bot):
        self.bot = bot

    # The code in this is executed when the bot is ready
    async def event_ready(self):
        pylogs.info(f"Logged in as {config['nick']} (ID: {self.bot.channel_id})", color=config["colored_logs"])
        print("------------------------------------")
        await self.bot.web_socket.send_privmsg(str(config["channel"]), str("/me has landed on this stream!"))

    # The code in this is executed whenever there is a message sent in the chat
    async def event_message(self, context):
        
        #Follow Alert
        if "!follow" in context.content.lower():
            if context.author in Events.allowed_user:
                command = context.content.split(" ")
                if(len(command) == 2):
                    await self.bot.web_socket.send_privmsg(config["channel"],"Follow alert für " + command[1])
                else:
                    await self.bot.web_socket.send_privmsg(config["channel"],"Follow alert ")
                os.system("python3 ./scripts/controller.py -1 " + Events.kette_1)
                os.system("python3 ./scripts/controller.py -1 " + Events.kette_2)
                os.system("python3 ./scripts/controller.py -1 " + Events.kette_3)
        
        #Sub Alert
        if "!sub" in context.content.lower():
            if context.author in Events.allowed_user:
                command = context.content.split(" ")
                if(len(command) == 2):
                    await self.bot.web_socket.send_privmsg(config["channel"],"Sub alert für " + command[1])
                else:
                    await self.bot.web_socket.send_privmsg(config["channel"],"Sub alert ")
            for i in range(16):
                os.system("python3 ./scripts/controller.py " + str(i) + " " + Events.kette_1 )
                os.system("python3 ./scripts/controller.py " + str(i) + " " + Events.kette_2 )
                os.system("python3 ./scripts/controller.py " + str(i) + " " + Events.kette_3 )
                time.sleep(0.5)
        
        #reset fairy lights to off
        if "!reset" in context.content.lower():
            if context.author in Events.allowed_user:
                await self.bot.web_socket.send_privmsg(config["channel"],"Reset")
                os.system("python3 ./scripts/controller.py 0 " + Events.kette_1)
                os.system("python3 ./scripts/controller.py 0 " + Events.kette_2)
                os.system("python3 ./scripts/controller.py 0 " + Events.kette_3)

        #change color of fairy light
        if "!kette" in context.content.lower():
            if context.author in Events.allowed_user:
                entry = context.content.split(" ")
                if entry[1] == "1":
                    kette = Events.kette_1
                elif entry[1] == "2":
                    kette = Events.kette_2
                elif entry[1] == "3":
                    kette = Events.kette_3
                elif entry[1] == "?":
                    await self.bot.web_socket.send_privmsg(config["channel"],"Nutzung: !kette $ketten_nummer $farben_nummer ")  
                    return 0
                else:
                    await self.bot.web_socket.send_privmsg(config["channel"],"Diese Kette gibt es nicht.")  
                    await self.bot.web_socket.send_privmsg(config["channel"],"Nutzung: !kette $ketten_nummer $farben_nummer ")  
                    await self.bot.web_socket.send_privmsg(config["channel"],"Nutzung: !sub  löst sub alert aus")
                    await self.bot.web_socket.send_privmsg(config["channel"],"Nutzung: !follow löst follow alert aus")    
                    return 0
                if int(entry[2]) <= 16 :
                    os.system("python3 ./scripts/controller.py " + str(entry[2]) + " " + kette)
                    await self.bot.web_socket.send_privmsg(config["channel"],"Ändere Farbe von Kette" + str(entry[1]) + " zu " + str(entry[2]))          
                else:
                    await self.bot.web_socket.send_privmsg(config["channel"],"Diese Farbe gibt es nicht! Es gibt nur 16 Farben")
                    await self.bot.web_socket.send_privmsg(config["channel"], context.content) 

        if "!off" in context.content.lower():
            if context.author in Events.allowed_user:
                await self.bot.web_socket.send_privmsg(config["channel"],"BYE ")
                os.system("python3 ./scripts/controller.py 0 " + Events.kette_1)
                os.system("python3 ./scripts/controller.py 0 " + Events.kette_2)
                os.system("python3 ./scripts/controller.py 0 " + Events.kette_3)
                os.system("sudo reboot")

