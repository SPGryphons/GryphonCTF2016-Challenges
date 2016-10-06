import discord
from discord.ext import commands
import aiohttp
import asyncio
import base64


class GCTF:
    """ Bot """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def flag(self, ctx):
        """Prints a flag to you"""
        await self.bot.send_message(ctx.message.author, "GCTF{r3d_b07_15_fr13ndly}")

async def greet_member(self, member):
    await t.bot.send_message(member.server, "Welcome " + member.name + " to " + member.server.name)


def setup(bot):
    global t
    bot.add_listener(greet_member, "on_member_join")
    t = GCTF(bot)
    bot.add_cog(t)
