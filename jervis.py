import os
import telebot
import requests

from lxml import html
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from string_var import *
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN_Jervis')
bot = telebot.TeleBot(BOT_TOKEN)

def gen_markup_link():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Türkçe", callback_data="dlink_tr"),
                               InlineKeyboardButton("English", callback_data="dlink_eng"))
    return markup

def gen_markup_script():
    markup = InlineKeyboardMarkup()
    for btn in buttons:
        markup.add(InlineKeyboardButton(btn, callback_data=btn))
    return markup

def get_latest_link():
    ntext = []
    response = requests.get(url, headers=headers)
    html_content = response.content
    tree = html.fromstring(html_content)
    element = tree.xpath(version_xpath)[0]
    
    links = tree.xpath('//a')
    text = element.text_content().strip()
    ntext.append(text)

    for link in links:
        href = link.get('href')
        if href and href.endswith('.msi') and "eng" in href:
            ntext.append(href)
    return ntext

def xscript_handler(message, ifile):
    pic_path = "{}{}.png".format(pics_path, ifile)
    photo = open(pic_path, 'rb')
    bot.send_photo(message.chat.id, photo)

    txt_path = "{}{}.txt".format(txts_path, ifile)
    txt_file = open(txt_path, 'rb')
    bot.send_document(message.chat.id, txt_file)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "dlink_tr":
        ytext = get_latest_link()
        tr_text, tr_linkfull, tr_linkdesktop = ytext[0].replace("English","Turkish"), ytext[1].replace("eng","trk"), ytext[2].replace("eng","trk")
        download_links = "\n{}\n\nFull : {}\n\nDesktop : {}".format(tr_text, tr_linkfull, tr_linkdesktop)
        bot.reply_to(call.message, download_links)
    elif call.data == "dlink_eng":
        ytext = get_latest_link()
        eng_text, eng_linkfull, eng_linkdesktop = ytext[0], ytext[1], ytext[2]
        download_links = "\n{}\n\nFull : {}\n\nDesktop : {}".format(eng_text, eng_linkfull, eng_linkdesktop)
        bot.reply_to(call.message, download_links)
    else: 
        xscript_handler(call.message, call.data)

    bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
    bot.answer_callback_query(callback_query_id=call.id, text="", show_alert=False)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)

@bot.message_handler(commands=['latest'])
def sign_handler(message):
    sent_msg = bot.send_message(message.chat.id, text = "Download Links : ", reply_markup=gen_markup_link())

@bot.message_handler(commands=['script'])
def sign_handler(message):
    sent_msg = bot.send_message(message.chat.id, text = "Script Sample : ", reply_markup=gen_markup_script())

@bot.message_handler(commands=['useful_websites'])
def useful_sites(message):
    bot.send_message(chat_id = message.chat.id, text = helper_links, parse_mode = "HTML", disable_web_page_preview=True, disable_notification=True)

@bot.message_handler(commands=['get_id'])
def get_chatid(message):
    day = message.chat.id
    bot.send_message(message.chat.id, day)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()