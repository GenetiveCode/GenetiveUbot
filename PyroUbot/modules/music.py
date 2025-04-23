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
            await message.reply(f"{prs} **Converting to opus...**")
            opus_file = audio_file.rsplit(".", 1)[0] + ".opus"
            os.system(f"ffmpeg -i '{audio_file}' -acodec libopus '{opus_file}' -y")
            os.remove(audio_file)
            audio_file = opus_file

        await client.call_py.play(message.chat.id, MediaStream(audio_file))
        return await message.reply(f"{brhsl} **Playing converted audio!**")

    if len(message.command) < 2:
        return await message.reply(f"{ggl} **Provide a link or title!**")

    query = " ".join(message.command[1:])
    url = query if "youtube.com" in query or "youtu.be" in query else None

    if not url:
        search = VideosSearch(query, limit=1).result()
        if not search["result"]:
            return await message.reply(f"{ggl} **Song not found!**")
        url = search["result"][0]["link"]

    try:
        mex = await message.reply(f"{prs} **Downloading audio...**")
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "downloads/%(title)s.%(ext)s",
            "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "opus", "preferredquality": "192"}],
            "cookiefile": "cookies.txt",
            "noplaylist": True,
            "merge_output_format": "opus",
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = f"downloads/{info['title']}.opus"

        if not os.path.exists(file_path):
            return await mex.edit(f"{ggl} **Download failed!**")

        await client.call_py.play(message.chat.id, MediaStream(file_path))
        await mex.edit(f"{brhsl} **Playing audio!**")
    except Exception as e:
        await mex.edit(f"{ggl} **Error: {str(e)}**")

@PY.UBOT("vplay")
@PY.TOP_CMD
@PY.GROUP
async def play_video(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if message.reply_to_message and message.reply_to_message.video:
        video_file = await message.reply_to_message.download(f"downloads/{message.reply_to_message.video.file_name}")

        await client.call_py.play(message.chat.id, MediaStream(video_file))
        return await message.reply(f"{brhsl} **Playing replied video!**")

    if len(message.command) < 2:
        return await message.reply(f"{ggl} **Provide a link or title!**")

    query = " ".join(message.command[1:])
    url = query if "youtube.com" in query or "youtu.be" in query else None

    if not url:
        search = VideosSearch(query, limit=1).result()
        if not search["result"]:
            return await message.reply(f"{ggl} **Video not found!**")
        url = search["result"][0]["link"]

    try:
        mex = await message.reply(f"{prs} **Downloading video...**")
        ydl_opts = {
            "format": "bv*+ba/b",  # Menggunakan kombinasi best video + best audio
            "outtmpl": "downloads/%(title)s.%(ext)s",
            "cookiefile": "cookies.txt",
            "noplaylist": True,
            "merge_output_format": "mp4",
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = f"downloads/{info['title']}.mp4"

        if not os.path.exists(file_path):
            return await mex.edit(f"{ggl} **Download failed!**")

        await client.call_py.play(message.chat.id, MediaStream(file_path))
        await mex.edit(f"{brhsl} **Playing video!**")
    except Exception as e:
        await mex.edit(f"{ggl} **Error: {str(e)}**")

@PY.UBOT("pause")
@PY.TOP_CMD
@PY.GROUP
async def pause_audio(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    try:
        await client.call_py.pause_stream(message.chat.id)
        await message.reply(f"{brhsl} **Stream paused!**")
    except Exception as e:
        print(e)
        await message.reply(f"{ggl} **Error: {str(e)}**")


@PY.UBOT("resume")
@PY.TOP_CMD
@PY.GROUP
async def resume_audio(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    try:
        await client.call_py.resume_stream(message.chat.id)
        await message.reply(f"{brhsl} **Stream resumed!**")
    except Exception as e:
        print(e)
        await message.reply(f"{ggl} **Error: {str(e)}**")


@PY.UBOT("end")
@PY.TOP_CMD
@PY.GROUP
async def stop_audio(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    
    try:
        await client.call_py.leave_call(message.chat.id)
        await message.reply(f"{brhsl} **Stream stopped and left voice chat!**")
    except Exception as e:
        print(e)
        await message.reply(f"{ggl} **Error: {str(e)}**")
