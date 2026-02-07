# MusicBot
a simple discord music bot


# 🎵 Discord Music Bot (YouTube & Spotify)

A simple Discord music bot made with Python.

Supports:
- YouTube
- Spotify links
- Queue system
- Volume control
- Voice channels

---

## ✨ Features

- 🎶 Play music from YouTube
- 🎧 Play Spotify links
- 📜 Queue system
- ⏭ Skip songs
- ⏹ Stop music
- 🔊 Volume control
- 🔌 Join / Leave voice channels
- 🔁 Auto play next song

---

## 📦 Requirements

You need:

- Python 3.8+
- FFmpeg
- Discord Bot Token
- Spotify API credentials

Install Python libraries:

pip install discord.py yt-dlp spotipy asyncio


Download FFmpeg:
https://ffmpeg.org/download.html

---

## ⚙️ IMPORTANT: FFmpeg PATH (REQUIRED)

⚠️ You MUST change the FFmpeg path in the code or the bot will NOT play sound.

Open `bot.py` and edit:

FFMPEG_PATH = r"C:\path\to\ffmpeg.exe"


Example:

FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"


Make sure the file exists on your PC.

---

## ⚙️ Setup

### 1. Create Discord Bot

1. Go to:
   https://discord.com/developers/applications
2. Create New Application
3. Go to "Bot"
4. Click "Add Bot"
5. Copy Bot Token
6. Enable:
   ✅ Message Content Intent

Put token in `bot.py`:

TOKEN = "YOUR_DISCORD_TOKEN"


---

### 2. Get Spotify API

1. Go to:
   https://developer.spotify.com/dashboard
2. Create App
3. Copy Client ID & Client Secret

Put in `bot.py`:

SPOTIFY_CLIENT_ID = "YOUR_ID"
SPOTIFY_CLIENT_SECRET = "YOUR_SECRET"


---

### 3. Invite Bot to Server

Generate invite link with permissions:

- Read Messages
- Send Messages
- Connect
- Speak

Add bot to your server.

---

## ▶️ Run the Bot

Open terminal in project folder and run:

python bot.py


If everything is correct, you will see:

✅ Bot online


---

## 📁 Project Structure

music-bot/
│
├── bot.py
├── README.md
└── requirements.txt (optional)


---

## 🎮 Commands

| Command | Description |
|---------|-------------|
| !play <song/link> | Play song |
| !skip | Skip song |
| !stop | Stop & clear queue |
| !vol + | Volume up |
| !vol - | Volume down |
| !join | Join voice |
| !leave | Leave voice |

---

## 📌 Examples

Play from YouTube:

!play eminem lose yourself


Play from Spotify:

!play https://open.spotify.com/track/xxxx


Increase volume:

!vol +


---

## ⚠️ Security Warning

❗ NEVER share your Discord bot token.

If your token is leaked:

1. Go to Developer Portal
2. Reset Token
3. Replace it in code

---

## 🛠 Troubleshooting

### ❌ No Sound

✔ Check FFmpeg path  
✔ Check volume (!vol +)  
✔ Restart bot  

---

### ❌ Bot Doesn't Join Voice

✔ Check permissions  
✔ Re-invite bot  
✔ Make sure you are in voice  

---

### ❌ Spotify Not Working

✔ Check API credentials  
✔ Check internet connection  
