from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b>How to Use This Bot</b>
Click the "Help" button to view the image:
"""

    close = [
        [InlineKeyboardButton("Close", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("Help", callback_data="help"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("About", callback_data="about"),
            InlineKeyboardButton("Close", callback_data="close")
        ],
    ]

    ABOUT = """
About this Bot:
  • Creator: @SexyNano
  • Framework: Pyrograms
"""

    HELP_IMAGE = "https://graph.org/file/120bf7519b24e50dd0b46.jpg"
