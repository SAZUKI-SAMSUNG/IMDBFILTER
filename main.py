from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

Naruto=Client(
    "Imdb Bot",
    bot_token="5250937026:AAFA2aduIz2mORKBJrrC8ki7pMtdQREM4Wg",
    api_id="15316155",
    api_hash="c2340e29da60393bc3c96fa7c0870911"
)




ALL_PIC = [
 "https://telegra.ph/file/13527c7b40976c1368cca.jpg",
 "https://telegra.ph/file/73ad5f7b9ac871d08d058.jpg",
 "https://telegra.ph/file/56e2c12ed686eeb4513da.jpg",
 "https://telegra.ph/file/7cde9e71ebffa93a0d209.jpg",
 "https://telegra.ph/file/cdd859489cae56263bd74.jpg"
]




@Naruto.on_message(filters.command("start"))
async def start_message(bot, message):
   await message.reply_photo(
       photo=random.choice(ALL_PIC),
       caption="Hey My Name is <a href='https://t.me/PyrogramTextBot'>𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 𝙱𝙾𝚃</a>",
       reply_markup=InlineKeyboardMarkup( [[
          ],[
          InlineKeyboardButton ("𝗕𝗢𝗧 𝗢𝗪𝗡𝗘𝗥", url="t.me/TEAM_KERALA"),
          InlineKeyboardButton ("𝗕𝗢𝗧 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥", url="t.me/PR0FESS0R_99"),
          ]]

        )
        
     )
   

Naruto.run()
