from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

Naruto=Client(
    "Imdb Bot",
    bot_token="5250937026:AAEveOUt5fOisEK7JD1ByjfOuNcLeX0bBus",
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
       caption="𝙷𝙴𝚈 <a href=https://t.me/{}></a> 𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 𝙰 <a href='https://t.me/PyrogramTextBot'>𝙵𝙻𝚄𝙵𝙵𝚈 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</a> 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 𝙾𝚁 𝙾𝚆𝙽𝙴𝚁 𝙸𝚂  <a href=https://t.me/TEAM_KERALA>𝚃𝙶 𝙵𝙻𝚄𝙵𝙵𝚈</a>",
       reply_markup=InlineKeyboardMarkup( [[
          ],[
          InlineKeyboardButton ("𝕋𝔼𝕃𝔼𝔾ℝ𝔸𝕄 𝔹𝕆𝕋", url="t.me/TgFluffyV1Bot"),
          InlineKeyboardButton ("𝕋𝔼𝕃𝔼𝔾ℝ𝔸𝕄 𝔹𝕆𝕋", url="t.me/SAZUKI_FILTER_BOT"),
          ],[
          InlineKeyboardButton ("ℙ𝔸𝕀𝔻 ℙℝ𝕆𝕄𝕆𝕋𝕀𝕆ℕ", url="t.me/TEAM_KERALA"),
          ]]

        )
        
     )
   

Naruto.run()
