from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start = 
        [
           
            InlineKeyboardButton('Source', url='github.com/miuiprojects')
        ]
       

close = 
        [
            
            InlineKeyboardButton('Close', callback_data='close_btn')
        ]
        

start_buttons = InlineKeyboardMarkup(start)
close_button = InlineKeyboardMarkup(close)
