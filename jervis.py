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
    """
    Generates an inline keyboard markup with buttons for language selection.

    Returns:
        InlineKeyboardMarkup: An object containing two buttons, one for Turkish ("Türkçe") 
                              and one for English ("English"), each with corresponding callback data.
    """
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Türkçe", callback_data="dlink_tr"),
                               InlineKeyboardButton("English", callback_data="dlink_eng"))
    return markup

def gen_markup_script():
    """
    Generates an inline keyboard markup for Telegram bot.

    This function creates an InlineKeyboardMarkup object and adds buttons to it
    using the provided list of buttons. Each button is represented by an 
    InlineKeyboardButton with the button text and callback data set to the 
    button text.

    Returns:
        InlineKeyboardMarkup: The generated inline keyboard markup with the 
        specified buttons.
    """
    markup = InlineKeyboardMarkup()
    for btn in buttons:
        markup.add(InlineKeyboardButton(btn, callback_data=btn))
    return markup

def get_latest_link():
    """
    Fetches the latest link and its associated text content from a specified URL.
    This function sends a GET request to the specified URL, parses the HTML content,
    and extracts the text content of a specific element identified by an XPath expression.
    It also retrieves all anchor tags and filters them to find links that end with '.msi'
    and contain the substring "eng". The text content and the filtered links are then
    returned as a list.
    Returns:
        list: A list containing the text content of the specified element and the filtered links.
    """
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
    """
    Handles the sending of a photo and a text document to a Telegram chat.

    Args:
        message (telegram.Message): The message object containing chat information.
        ifile (str): The identifier for the file to be sent.

    Returns:
        None
    """
    pic_path = "{}{}.png".format(pics_path, ifile)
    photo = open(pic_path, 'rb')
    bot.send_photo(message.chat.id, photo)

    txt_path = "{}{}.txt".format(txts_path, ifile)
    txt_file = open(txt_path, 'rb')
    bot.send_document(message.chat.id, txt_file)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    """
    Handles callback queries from Telegram bot interactions.

    Args:
        call (telebot.types.CallbackQuery): The callback query object containing data about the interaction.

    Behavior:
        - If the callback data is "dlink_tr", it fetches the latest download link, modifies it for Turkish language, 
          and replies to the message with the Turkish download links.
        - If the callback data is "dlink_eng", it fetches the latest download link and replies to the message with 
          the English download links.
        - For any other callback data, it delegates the handling to the xscript_handler function.

    After handling the callback, it removes the inline keyboard markup from the message and answers the callback query.

    Note:
        - The function assumes the existence of `get_latest_link`, `bot`, and `xscript_handler` in the current scope.
    """
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
    """
    Sends a welcome message to the user.

    Args:
        message (telebot.types.Message): The message object containing chat information.

    Returns:
        None
    """
    markup = telebot.types.ReplyKeyboardMarkup()
    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)

@bot.message_handler(commands=['latest'])
def sign_handler(message):
    """
    Handles the sign command by sending a message with download links.

    Args:
        message (telegram.Message): The message object that triggered the handler.

    Returns:
        None
    """
    sent_msg = bot.send_message(message.chat.id, text = "Download Links : ", reply_markup=gen_markup_link())

@bot.message_handler(commands=['script'])
def sign_handler(message):
    """
    Handles the sign command by sending a message with a sample script and a custom keyboard.

    Args:
        message (telegram.Message): The message object that triggered the handler.

    Returns:
        None
    """
    sent_msg = bot.send_message(message.chat.id, text = "Script Sample : ", reply_markup=gen_markup_script())

@bot.message_handler(commands=['useful_websites'])
def useful_sites(message):
    """
    Sends a message containing helpful links to the user.

    Args:
        message (telegram.Message): The message object containing the chat ID.

    Returns:
        None
    """
    bot.send_message(chat_id = message.chat.id, text = helper_links, parse_mode = "HTML", disable_web_page_preview=True, disable_notification=True)

@bot.message_handler(commands=['get_id'])
def get_chatid(message):
    """
    Extracts the chat ID from the given message and sends it back to the same chat.

    Args:
        message (telebot.types.Message): The message object containing the chat ID.

    Returns:
        None
    """
    day = message.chat.id
    bot.send_message(message.chat.id, day)

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    """
    Responds to a message by echoing back the text of the message.

    Args:
        message: The message object that contains the text to be echoed back.
    """
    bot.reply_to(message, message.text)

bot.infinity_polling()