import discord
import logging
import fsecont as fse
import json
loglevel = logging.INFO
logging.basicConfig(filename="N&M_Bot_Log.txt", filemode="w", encoding="utf-8", level=loglevel)

conf = open("config.json", "r", encoding="utf-8")
confJson = json.load(conf)
discordKey = confJson["DiscordToken"]

bot = discord.Bot()
guilds = [987855799038648390, 1010798164976095232, 1058187644615528459]
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    logging.info("Bot started")


@bot.slash_command(guild_ids = guilds)
async def lease(ctx,
    fromuser: discord.Option(discord.SlashCommandOptionType.string),
    touser: discord.Option(discord.SlashCommandOptionType.string),
    aircraftreg: discord.Option(discord.SlashCommandOptionType.string)
    ):
    fse.leaseACReg(fromuser, touser, aircraftreg)
    response = "Aircraft Leased"
    await ctx.respond(response)

@bot.slash_command(guild_ids = guilds)
async def returnlease(ctx,
    fromuser: discord.Option(discord.SlashCommandOptionType.string),
    aircraftreg: discord.Option(discord.SlashCommandOptionType.string),
    ):
    #if fse.checkLeased(aircraftreg):
        #fse.returnLease(fromuser, aircraftreg)
        #response = "Lease Returned"
    #else:
        #response = "Aircraft Not Leased"
    status = fse.returnLease(fromuser, aircraftreg)
    if status:
        response = "Lease Returned"
    else:
        response = "Aircraft Not Leased"
    await ctx.respond(response)
bot.run(discordKey)