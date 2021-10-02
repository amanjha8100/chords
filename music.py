import asyncio
import discord
from discord.ext import commands

from youtube_dl import YoutubeDL


class music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.is_playing = False

        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        self.FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

        self.vc = ""

    # @commands.Cog.listener()
    # async def on_voice_state_update(self, ctx, *args):
    #     # time = 0
    #     # print("If listening")
    #     # if not self.vc.is_playing:
    #     #     while True:
    #     #         await asyncio.sleep(1)
    #     #         time = time+1
    #     #         print(time)
    #     #         if self.vc.is_playing:
    #     #             time=0
    #     #         if time==20:
    #     #             await self.vc.disconnect()
    #     #         if not self.vc.is_connected():
    #     #             break
    #     while self.vc.is_playing:
    #         await asyncio.sleep(1)
    #     else:
    #         await asyncio.sleep(15)
    #         while self.vc.is_playing:
    #             break
    #         else:
    #             await self.vc.disconnect()

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):

        if not member.id == self.bot.user.id:
            return

        elif before.channel is None:
            voice = self.vc
            time = 0
            while True:
                await asyncio.sleep(1)
                time = time + 1
                if voice.is_playing:
                    time = 0
                if time == 20:
                    await voice.disconnect()
                if not voice.is_connected():
                    break

    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" %
                                        item, download=False)['entries'][0]
            except Exception:
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title']}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']

            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(
                m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    async def play_music(self, ctx):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']

            if self.vc == "" or not self.vc.is_connected() or self.vc == None:
                self.vc = await self.music_queue[0][1].connect()
            else:
                await self.vc.move_to(self.music_queue[0][1])

            await ctx.send(f""":arrow_forward: Playing **{self.music_queue[0][0]['title']}** -- requested by {self.music_queue[0][2]}""")

            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(
                m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False

    @commands.command(name="p", help="Plays a selected song from youtube")
    async def p(self, ctx, *args):
        query = " ".join(args)

        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send("Connect to a voice channel!")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("Could not download the song. Incorrect format try another keyword.")
            else:
                await ctx.send(f""":headphones: **{song["title"]}** has been added to the queue by {ctx.author.mention}""")
                self.music_queue.append(
                    [song, voice_channel, ctx.author.mention])

                if self.is_playing == False:
                    await self.play_music(ctx)

    @commands.command(name="q", help="Displays the current songs in queue")
    async def q(self, ctx):
        retval = ""
        for i in range(0, len(self.music_queue)):
            retval += f"""{i+1}. **{self.music_queue[i][0]['title']}** -- added by {self.music_queue[i][2]}\n"""

        if retval != "":
            await ctx.send(retval)
        else:
            await ctx.send("No music in queue")

    @commands.command(name="s", help="Skips the current song being played")
    async def skip(self, ctx):
        if self.vc != "" and self.vc:
            await ctx.send("""***Skipped current song !***""")
            self.vc.stop()
            await self.play_music(ctx)

    @commands.command(name="l", help="Leaves if commanded to the voice channel")
    async def leave(self, ctx, *args):
        if self.vc.is_connected():
            await ctx.send("""**Bye Bye **:slight_smile:""")
            await self.vc.disconnect(force=True)

    @commands.command(name="help", help="Return all the possible commands")
    async def help(self, ctx):
        help_message = """
        ```
        _p : Plays the song with search keyword following the command
        _s : skips the currently playing music
        _q : shows the music added in list/queue
        _l : commands the bot to leave the voice channel
        _help : shows all the commands of the bot.

        Developer : Aman Prakash Jha
        ```
        """
        await ctx.send(help_message)
