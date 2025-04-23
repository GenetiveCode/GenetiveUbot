from pyrogram import Client, filters
from pyrogram.types import Message
from asyncio import get_event_loop
from functools import partial
from yt_dlp import YoutubeDL
from pytgcalls import PyTgCalls
from pytgcalls.types import MediaStream
from pytgcalls.types.calls import Call
from pyrogram.errors import ChatAdminRequired, UserBannedInChannel
from pytgcalls.exceptions import NotInCallError
from youtubesearchpython import VideosSearch
import os
import wget
import math
from datetime import timedelta
from time import time
from pyrogram.errors import FloodWait, MessageNotModified
from youtubesearchpython import VideosSearch
from pyrogram.enums import ChatType
from PyroUbot import *

__MODULE__ = "streaming"
__HELP__ = f"""
<blockquote>
╭
┊➤ᴘʟᴀʏ [ ᴜʀʟ,ᴛɪᴛʟᴇ,ʀᴇᴘʟʏ-ᴍᴘ3 ] 
┊ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ᴏs
┊➤ᴠᴘʟᴀʏ[ ᴜʀʟ,ᴛɪᴛʟᴇ,ʀᴇᴘʟʏ-ᴍᴘ4 ]
┊ᴘʟᴀʏɪɴɢ ᴠɪᴅᴇᴏ ɪɴ ᴏs
┊➤ᴇɴᴅ
┊ᴇɴᴅᴇᴅ ᴏs
┊➤ᴘᴀᴜsᴇ
┊ᴘᴀᴜsᴇ ᴀᴜᴅɪᴏ ᴏʀ ᴠɪᴅᴇᴏ ᴏs
┊➤ʀᴇsᴜᴍᴇ
┊ʀᴇsᴜᴍᴇ ᴠɪᴅᴇᴏ ᴏʀ ᴀᴜᴅɪᴏ ᴏs
╰</blockquote>
"""

import os
from yt_dlp import YoutubeDL
from youtubesearchpython import VideosSearch
from pytgcalls.types import MediaStream

@PY.UBOT("play")
@PY.TOP_CMD
@PY.GROUP
async def play_audio(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if message.reply_to_message and message.reply_to_message.audio:
        audio_file = await message.reply_to_message.download(f"downloads/{message.reply_to_message.audio.file_name}")

        if not audio_file.endswith(".opus"):
      
