import os, sys, asyncio
from config import *
from pyrogram import filters, Client


@Client.on_message(filters.private & filters.command(["help"]))
async def start(client,message):
	botdata(int(botid))
#	data = find_one(int(botid))
#	total_rename = data["total_rename"]
#	total_size = data["total_size"]
	await message.reply_text(f"Origional BOT :- <a href='https://t.me/GangsterBaby_renamer_BOT'>Gangster Baby</a>\nCreater :- <a href='https://t.me/LazyDeveloper'>🦋LazyDeveloper🦋</a>\n\n Thank you **<a href='https://t.me/mRiderDM'>LazyDeveloperr</a>** for your hard work \n\n❤️ we love you <a href='https://t.me/mRiderDM'>**LazyDeveloper**</a> ❤️",quote=True)
