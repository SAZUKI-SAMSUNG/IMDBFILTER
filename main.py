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
       caption="Hey My Name is <a href='https://t.me/PyrogramTextBot'>PyrogramBot</a>",
       reply_markup=InlineKeyboardMarkup( [[
          InlineKeyboardButton ("𝗝𝗢𝗜𝗡 𝗚𝗥𝗢𝗨𝗣", url="t.me/midnightmoviesofficial"),
          InlineKeyboardButton ("𝗝𝗢𝗜𝗡 𝗖𝗛𝗔𝗡𝗡𝗘𝗟", url="t.me/FILE_ADD_CHANNEL"),
          ],[
          InlineKeyboardButton ("𝗕𝗢𝗧 𝗢𝗪𝗡𝗘𝗥", url="t.me/TEAM_KERALA"),
          InlineKeyboardButton ("𝗕𝗢𝗧 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥", url="t.me/PR0FESS0R_99"),
          ],[
          InlineKeyboardButton ("𝗕𝗢𝗧 𝗘𝗗𝗜𝗧𝗜𝗡𝗚", url="t.me/TEAM_KERALA"),
          ],[
          InlineKeyboardButton ("𝗔𝗗𝗗 𝗠𝗘 𝗧𝗢 𝗔 𝗖𝗛𝗔𝗧 𝗚𝗥𝗢𝗨𝗣", url="http://t.me/PyrogramTextBot?startgroup=true")
          ]]

        )
        
     )
   

Naruto.run()
