import discord
from discord.ext import commands
import yt_dlp
import asyncio
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


# ================= SETTINGS =================

TOKEN = "YOUR_DISCORD_TOKEN"

FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"

SPOTIFY_CLIENT_ID = "YOUR_SPOTIFY_ID"
SPOTIFY_CLIENT_SECRET = "YOUR_SPOTIFY_SECRET"

DEFAULT_VOLUME = 0.5

# ===========================================


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# Spotify setup
sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET
    )
)


queues = {}
volume = DEFAULT_VOLUME


ytdl_opts = {
    "format": "bestaudio/best",
    "quiet": True,
    "default_search": "ytsearch",
    "noplaylist": True
}

ffmpeg_opts = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn"
}

ytdl = yt_dlp.YoutubeDL(ytdl_opts)


# =============== HELPERS =================

def get_queue(guild_id):
    if guild_id not in queues:
        queues[guild_id] = []
    return queues[guild_id]


async def play_next(ctx):

    queue = get_queue(ctx.guild.id)

    if not queue:
        return

    query = queue.pop(0)

    info = ytdl.extract_info(query, download=False)

    if "entries" in info:
        info = info["entries"][0]

    url = info["url"]

    source = discord.FFmpegPCMAudio(
        url,
        executable=FFMPEG_PATH,
        **ffmpeg_opts
    )

    source = discord.PCMVolumeTransformer(source, volume)

    vc = ctx.voice_client

    vc.play(
        source,
        after=lambda e: asyncio.run_coroutine_threadsafe(
            play_next(ctx), bot.loop
        )
    )


# =============== EVENTS =================

@bot.event
async def on_ready():
    print(f"✅ Bot online: {bot.user}")


# =============== COMMANDS =================

@bot.command()
async def play(ctx, *, query):

    if not ctx.author.voice:
        await ctx.send("❌ Join a voice channel first!")
        return

    if not ctx.voice_client:
        await ctx.author.voice.channel.connect()

    # Spotify link
    if "open.spotify.com" in query:

        try:
            track = sp.track(query)

            name = track["name"]
            artist = track["artists"][0]["name"]

            query = f"{name} {artist} audio"

        except:
            await ctx.send("❌ Cannot read Spotify link")
            return


    queue = get_queue(ctx.guild.id)
    queue.append(query)

    if not ctx.voice_client.is_playing():
        await play_next(ctx)

    await ctx.send("🎵 Added to queue!")


@bot.command()
async def skip(ctx):

    if ctx.voice_client:
        ctx.voice_client.stop()
        await ctx.send("⏭ Skipped!")


@bot.command()
async def stop(ctx):

    if ctx.voice_client:
        await ctx.voice_client.disconnect()

    queues[ctx.guild.id] = []

    await ctx.send("⏹ Stopped!")


@bot.command()
async def vol(ctx, value):

    global volume

    if value == "+":
        volume = min(1.0, volume + 0.1)

    elif value == "-":
        volume = max(0.0, volume - 0.1)

    if ctx.voice_client and ctx.voice_client.source:
        ctx.voice_client.source.volume = volume

    await ctx.send(f"🔊 Volume: {int(volume * 100)}%")


@bot.command()
async def join(ctx):

    if ctx.author.voice:
        await ctx.author.voice.channel.connect()
        await ctx.send("✅ Joined voice")


@bot.command()
async def leave(ctx):

    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("👋 Left voice")


# =============== START =================

bot.run(TOKEN)
