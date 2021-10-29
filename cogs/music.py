import asyncio
import discord
from discord.ext import commands

from random import shuffle
from youtube_dl import YoutubeDL

from cogs.utils.roles import voice_channel_moderator_roles


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.isTimed = False
        self.is_playing = False
        self.current_song = None
        self.music_queue = []
        self.skip_votes = set()

        self.YDL_OPTIONS = {"format": "bestaudio", "noplaylist": "True"}
        self.FFMPEG_OPTIONS = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            "options": "-vn",
        }

        self.vc = ""

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
                info = ydl.extract_info("ytsearch:%s" % item, download=False)[
                    "entries"
                ][0]
            except Exception:
                return False
        return {
            "source": info["formats"][0]["url"],
            "title": info["title"],
            "song_length": info["duration"],
        }

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]["source"]

            self.current_song = self.music_queue.pop(0)

            self.vc.play(
                discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS),
                after=lambda e: self.play_next(),
            )
        else:
            self.is_playing = False
            self.current_song = None

    async def play_music(self, ctx):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]["source"]

            if self.vc == "" or not self.vc.is_connected() or self.vc == None:
                self.vc = await self.music_queue[0][1].connect()
            else:
                await self.vc.move_to(self.music_queue[0][1])

            await ctx.send(
                f""":arrow_forward: Playing **{self.music_queue[0][0]['title']}** -- requested by {self.music_queue[0][2]}"""
            )

            self.vc.play(
                discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS),
                after=lambda e: self.play_next(),
            )
            self.current_song = self.music_queue.pop(0)

        else:
            self.is_playing = False
            self.current_song = None

    @commands.command(
        name="p",
        help="Plays a selected song from youtube \U0001F3B5",
        aliases=["play"],
    )
    async def p(self, ctx, *args):
        query = " ".join(args)

        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send("Connect to a voice channel!")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send(
                    "Could not download the song. Incorrect format try another keyword."
                )
            else:
                await ctx.send(
                    f""":headphones: **{song["title"]}** has been added to the queue by {ctx.author.mention}"""
                )
                self.music_queue.append([song, voice_channel, ctx.author.mention])

                if self.is_playing == False:
                    await self.play_music(ctx)

    @commands.command(
        name="cp",
        help="Shows the currently playing song \U0001F440",
        aliases=["playing"],
    )
    async def cp(self, ctx):
        msg = (
            "No music playing"
            if self.current_song is None
            else f"""Currently Playing: **{self.current_song[0]['title']}** -- added by {self.current_song[2]}\n"""
        )
        await ctx.send(msg)

    @commands.command(
        name="q",
        help="Shows the music added in list/queue \U0001F440",
        aliases=["queue"],
    )
    async def q(self, ctx):
        print(self.music_queue)
        retval = ""
        for (i, m) in enumerate(self.music_queue):
            retval += f"""{i+1}. **{m[0]['title']}** -- added by {m[int(2)]}\n"""

        if retval != "":
            await ctx.send(retval)
        else:
            await ctx.send("No music in queue")

    @commands.command(name="cq", help="Clears the queue", aliases=["clear"])
    async def cq(self, ctx):
        self.music_queue = []
        await ctx.send("""***Queue cleared !***""")

    @commands.command(name="shuffle", help="Shuffles the queue")
    async def shuffle(self, ctx):
        shuffle(self.music_queue)
        await ctx.send("""***Queue shuffled !***""")

    @commands.command(
        name="s", help="Skips the current song being played", aliases=["skip"]
    )
    async def skip(self, ctx):
        if self.vc != "" and self.vc:
            await ctx.send("""***Skipped current song !***""")
            self.skip_votes = set()
            self.vc.stop()
            await self.play_music(ctx)

    @commands.command(
        name="voteskip",
        help="Vote to skip the current song being played",
        aliases=["vs"],
    )
    async def voteskip(self, ctx):
        if ctx.voice_client is None:
            return
        num_members = len(ctx.voice_client.channel.members) - 1
        self.skip_votes.add(ctx.author.id)
        votes = len(self.skip_votes)
        if votes >= num_members / 2:
            await ctx.send(f"Vote passed by majority ({votes}/{num_members}).")
            await self.skip(ctx)

    @commands.command(
        name="l",
        help="Commands the bot to leave the voice channel \U0001F634",
        aliases=["leave"],
    )
    @commands.has_any_role(*voice_channel_moderator_roles)
    async def leave(self, ctx, *args):
        if self.vc.is_connected():
            await ctx.send("""**Bye Bye **:slight_smile:""")
            await self.vc.disconnect(force=True)

    @commands.command(
        name="pn", help="Moves the song to the top of the queue \U0001F4A5"
    )
    @commands.has_any_role(*voice_channel_moderator_roles)
    async def playnext(self, ctx, *args):
        query = " ".join(args)

        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send("Connect to a voice channel")
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send(
                    "Could not download the song. Incorrect format try another keyword."
                )
            else:
                vote_message = await ctx.send(
                    f":headphones: **{song['title']}** will be added to the top of the queue by {ctx.author.mention}\n"
                    "You have 30 seconds to vote by reacting :+1: on this message.\n"
                    "If more than 50% of the people in your channel agree, the request will be up next!"
                )
                await vote_message.add_reaction("\U0001F44D")
                await asyncio.sleep(30)
                voters = len(voice_channel.members)
                voters = voters - 1 if self.vc else voters
                result_vote_msg = await ctx.fetch_message(vote_message.id)
                votes = (
                    next(
                        react
                        for react in result_vote_msg.reactions
                        if str(react.emoji) == "\U0001F44D"
                    ).count
                    - 1
                )
                if votes >= voters / 2:
                    self.music_queue.insert(
                        0, [song, voice_channel, ctx.author.mention]
                    )
                    await ctx.send(
                        f":headphones: **{song['title']}** will be added played next!"
                    )
                else:
                    self.music_queue.append([song, voice_channel, ctx.author.mention])
                    await ctx.send(
                        f":headphones: **{song['title']}** will be played add the end of the queue!"
                    )

                if self.is_playing == False or (
                    self.vc == "" or not self.vc.is_connected() or self.vc == None
                ):
                    await self.play_music(ctx)

    """Pause the currently playing song."""

    @commands.command(name="pause", help="Pause the currently playing song")
    @commands.has_any_role(*voice_channel_moderator_roles)
    async def pause(self, ctx):
        vc = ctx.voice_client

        if not vc or not vc.is_playing():
            return await ctx.send("I am currently playing nothing!", delete_after=20)
        elif vc.is_paused():
            return

        vc.pause()
        await ctx.send(f":pause_button:  {ctx.author.mention} Paused the song!")

    """Resume the currently playing song."""

    @commands.command(name="resume", help="Resume the currently playing song")
    @commands.has_any_role(*voice_channel_moderator_roles)
    async def resume(self, ctx):
        vc = ctx.voice_client

        if not vc or vc.is_playing():
            return await ctx.send("I am already playing a song!", delete_after=20)
        elif not vc.is_paused():
            return

        vc.resume()
        await ctx.send(f":play_pause:  {ctx.author.mention} Resumed the song!")

    @commands.command(
        name="r",
        help="removes song from queue at index given. \U0001F4A9",
        aliases=["remove"],
    )
    @commands.has_any_role(*voice_channel_moderator_roles)
    async def remove(self, ctx, *args):
        query = "".join(*args)
        index = 0
        negative = True if (query[0] == "-") else False
        if not negative:
            for i in range(len(query)):
                convert = (int)(query[i])
                index = index * 10 + convert
        index -= 1

        if negative:
            await ctx.send("Index cannot be less than one")
        elif index >= len(self.music_queue):
            await ctx.send("Wrong index. Indexed music not present in the queue")
        else:
            await ctx.send(
                f""":x: Music at index {query} removed by {ctx.author.mention}"""
            )
            self.music_queue.pop(index)

    @commands.command(
        name="rep",
        help="Restarts the current song. \U000027F2",
        aliases=["restart"],
    )
    @commands.has_any_role(*voice_channel_moderator_roles)
    async def restart(self, ctx):
        song = []
        if self.current_song != None:
            song = self.current_song[0]
            voice_channel = ctx.author.voice.channel
            self.music_queue.insert(0, [song, voice_channel, ctx.author.mention])
            self.vc.stop()
            if len(self.music_queue) > 0:
                self.is_playing = True

                m_url = self.music_queue[0][0]["source"]

                if self.vc == "" or not self.vc.is_connected() or self.vc == None:
                    self.vc = await self.music_queue[0][1].connect()
                    await ctx.send("No music added")
                else:
                    await self.vc.move_to(self.music_queue[0][1])

                    await ctx.send(
                        f""":repeat: Replaying **{self.music_queue[0][0]['title']}** -- requested by {self.music_queue[0][2]}"""
                    )

                    self.vc.play(
                        discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS),
                        after=lambda e: self.play_next(),
                    )
                    self.current_song = self.music_queue.pop(0)

        else:
            self.is_playing = False
            self.current_song = None
            await ctx.send(f""":x: No music playing""")

    @commands.command(
        name="qt",
        help="Calculates and outputs the total length of the songs in the queue.",
        aliases=["queuetime"],
    )
    async def qt(self, ctx):
        remaining_time = 0
        for song in self.music_queue:
            remaining_time += song[0]["song_length"]

        remaining_time_minutes = str(remaining_time // 60)
        remaining_time = str(remaining_time % 60)
        remaining_time = f"{remaining_time_minutes}:{remaining_time}"

        await ctx.send(f"""The queue has a total of {remaining_time} remaining!""")

    @commands.command(
        name="sleep", help="Sets the bot to sleep. \U0001F4A4", aliases=["timer"]
    )
    @commands.has_any_role(*voice_channel_moderator_roles)
    async def sleep(self, ctx, *args):
        second = int(0)
        query = list(args)
        if self.is_playing == False:
            return await ctx.send(f"No music playing")

        if len(query) == 0 and self.isTimed:
            self.isTimed = False
            return
        elif len(query) == 2 and not self.isTimed:
            try:
                if query[0] == "m":
                    second = int(query[1]) * 60
                elif query[0] == "h":
                    second = int(query[1]) * 3600
                elif query[0] == "s":
                    second = int(query[1])
                else:
                    await ctx.send("Invalid time format.")
                    return
            except:
                await ctx.send("Invalid time specified")
                return
        elif len(query) == 2 and self.isTimed:
            await ctx.send("Timer already set. Unset to reset.")
            return
        else:
            await ctx.send("Invalid time format.")
            return
        seconds = f"{second}"
        if second < 0:
            await ctx.send("Time cannot be negative")
        else:
            self.isTimed = True
            message = await ctx.send("Timer set for : " + seconds + " seconds.")
            while True and self.isTimed:
                second = second - 1
                if second == 0:
                    await message.edit(new_content=("Ended!"))
                    break
                await message.edit(new_content=("Timer: {0}".format(second)))
                await asyncio.sleep(1)

            if self.isTimed == False:
                await ctx.send("Timer disabled.")
            else:
                await ctx.send(
                    f""" **{ctx.message.author.mention} Sleep time exceeded! Bye-Bye!** :slight_smile: """
                )
                self.isTimed = False
                await self.vc.disconnect(force=True)


def setup(bot):
    bot.add_cog(Music(bot))
