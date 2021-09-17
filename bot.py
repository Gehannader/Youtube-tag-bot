# ©youtubeslgeekshow me 

import os
import pyrogram
from pyrogram import Client, filters
from youtubesearchpython import VideosSearch
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import User, Message, InlineQuery, InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton
import YoutubeTags
from YoutubeTags import videotags

JOIN_ASAP = " **You cant use me untill subscribe our updates channel** ☹️\n\n So Please join our updates channel by the following button and hit on the ` /start ` button again 😊"

FSUBB = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Join our update Channel 🗣", url=f"https://t.me/sl_bot_zone") 
        ]]      
    )

SEARCH_BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝑺𝒍 𝑩𝒐𝒕 𝒁𝒐𝒏𝒆 ✍️", url=f"https://t.me/SL_bot_zone"),
                    InlineKeyboardButton("𝓢𝓛 𝓑𝓸𝓽 𝓒𝓱𝓪𝓽", url=f"https://t.me/slbotzone"),
                ],
                [
                    InlineKeyboardButton(text="Search Inline🔎 ", switch_inline_query_current_chat="")],
            ]
        )

text = "👋 Hello There,\n\n **I'm Youtube Bot**.\n\n🌺Features\n🍃Inline youtube search.\n🍂Youtube Tag   Extractor.\n\n✨ Pọwẹrẹɗ Ɓy : @SL_bot_zone\n\n✮───────────────✮\n\n🌟 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 : @supunmabot\n\n✮───────────────✮"

BUTTON = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𝑺𝒍 𝑩𝒐𝒕 𝒁𝒐𝒏𝒆 ✍️", url=f"https://t.me/SL_bot_zone"),
                    InlineKeyboardButton("𝓢𝓛 𝓑𝓸𝓽 𝓒𝓱𝓪𝓽", url=f"https://t.me/slbotzone"),
                ],
                [
                    InlineKeyboardButton(text="📦 Socure Code 📦", url=f"https://github.com/youtubeslgeekshow/youtubebot")],
            ]
        )

slbotzone = Client(
    "@slbotzone", 
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]    
)
   
@slbotzone.on_message(filters.command(["start"]))
async def start(bot, message):
    try:
        await message._client.get_chat_member(int("-1001325914694"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return       
    await message.reply_text(text=text,reply_markup=SEARCH_BUTTON)
   


@slbotzone.on_message(filters.regex("https://www.youtube.com") | filters.regex("http://www.youtube.com") | filters.regex("https://youtu.be/") | filters.regex("https://www.youtu.be/") | filters.regex("http://www.youtu.be/"))
async def tag(bot, message):
    link = str(message.text)
    tags = videotags(link) 
    if tags=="":
         await message.reply_text(" `𝐍𝐨 𝐓𝐚𝐠𝐬 𝐅𝐨𝐮𝐧𝐝 🔖`")
    else:
         await message.reply_text(text=f"** 𝑺𝒆𝒍𝒆𝒄𝒕 𝒘𝒉𝒂𝒕 𝒚𝒐𝒖 𝒘𝒂𝒏𝒕 𝒕𝒐 𝒂𝒄𝒄𝒐𝒎𝒑𝒍𝒊𝒔𝒉 𝒘𝒊𝒕𝒉 𝒕𝒉𝒆 𝒃𝒖𝒕𝒕𝒐𝒏 𝒃𝒆𝒍𝒐𝒘 **\n\n𝓣𝓱𝓮𝓼𝓮 𝓪𝓻𝓮 𝓽𝓱𝓮 𝓽𝓪𝓰𝓼 𝓾𝓼𝓮𝓭 𝓯𝓸𝓻 𝓽𝓱𝓮 𝓿𝓲𝓭𝓮𝓸 𝔂𝓸𝓾 𝓼𝓮𝓷𝓽 𝓶𝓮\n\n\n ` {tags} ` \n\n\n 🔥 Pọwẹrẹɗ Ɓy : @SL_bot_zone\n\n☘️ 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 : @supunmabot",reply_markup=BUTTON)
 

@slbotzone.on_inline_query()
async def search(client: Client, query: InlineQuery):
    answers = []
    search_query = query.query.lower().strip().rstrip()

    if search_query == "":
        await client.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text="Type video name here..",
            switch_pm_parameter="help",
            cache_time=0
        )
    else:
        videosSearch = VideosSearch(search_query, limit=50)

        for v in videosSearch.result()["result"]:
            answers.append(
                InlineQueryResultArticle(
                    title=v["title"],
                    description=" {} .".format(
                       v["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "https://www.youtube.com/watch?v={}".format(
                            v["id"]
                        )
                    ),
                    thumb_url=v["thumbnails"][0]["url"]
                )
            )

        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="**Error: Search timed out❌**",
                switch_pm_parameter="",
            )

print(
    """
┏━┳┓╋╋╋╋╋┏┓╋╋╋┏┓┏┓╋╋┏┓
┃━┫┗┳━┓┏┳┫┗┳━┳┛┃┃┗┳━┫┗┓
┣━┃┏┫╋┗┫┏┫┏┫┻┫╋┃┃╋┃╋┃┏┫
┗━┻━┻━━┻┛┗━┻━┻━┛┗━┻━┻━┛
⚊❮❮❮❮  I am supun  ❯❯❯❯⚊
⚊❮❮❮❮  Join @sl_bot_zone ❯❯❯❯⚊
"""
)
slbotzone.run()

