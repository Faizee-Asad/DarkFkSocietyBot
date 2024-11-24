# This is test
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

# Replace this with your bot's API token
BOT_TOKEN = "6597274671:AAG_wB6-aktYpNsycKv1HVNHVoG4y9rzXDU"

# Predefined topics and cheat sheets
cheat_sheets = {
    "Termux": {
        "Termux Basic Packages": """TERMUX BASIC PACKAGES:

        pkg update -y
        pkg upgrade -y
        pkg install python -y
        pkg install python2 -y
        pkg install python2-dev -y
        pkg install python3 -y
        pkg install java -y
        pkg install fish -y
        pkg install ruby -y
        pkg install help -y
        pkg install git -y
        pkg install host -y
        pkg install php -y
        pkg install perl -y
        pkg install nmap -y
        pkg install bash -y
        pkg install clang -y
        pkg install nano -y
        pkg install w3m -y
        pkg install havij -y
        pkg install hydra -y
        pkg install figlet -y
        pkg install cowsay -y
        pkg install curl -y
        pkg install tar -y
        pkg install zip -y
        pkg install unzip -y
        pkg install tor -y
        pkg install google -y
        pkg install sudo -y
        pkg install wget -y
        pkg install wireshark -y
        pkg install wgetrc -y
        pkg install wcalc -y
        pkg install bmon -y
        pkg install vpn -y
        pkg install unrar -y
        pkg install toilet -y
        pkg install proot -y
        pkg install net-tools -y
        pkg install golang -y
        pkg install chroot -y
        termux-chroot -y
        pkg install macchanger -y
        pkg install openssl -y
        pkg install cmatrix -y
        pkg install openssh -y
        pkg install wireshark -y
        termux-setup-storage -y
        pkg install macchanger -y
        apt update && apt upgrade -y
        """,
        "SQLMAP": """🔰 Sqlmap 🫧
━━━━━━━━━━━━━━━━━━
@DarkFkSociety_Bot
━━━━━━━━━━━━━━━━━━

🫧 SQLMAP is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers. 🫧
━━━━━━━━━━━━━━━━━━

Installation:

apt update && apt upgrade -y
apt install python python2 python3 -y
apt install git -y 
git clone https://github.com/sqlmapproject/sqlmap
cd sqlmap
python sqlmap.py -h

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🫧  Telegram Channel 🫧
 @DarkFkSociety_Bot
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    }
}

# Start command handler
def start(update: Update, context: CallbackContext):
    """Handle the /start command and display the main menu."""
    keyboard = [
        [InlineKeyboardButton("Termux", callback_data="Termux")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Welcome! Select a topic:", reply_markup=reply_markup)

# Topic selection handler
def handle_topic(update: Update, context: CallbackContext):
    """Handle the topic selection and show the subtopics."""
    query = update.callback_query
    query.answer()

    topic = query.data
    if topic == "Termux":
        # Show the subtopic for "Termux"
        subtopics = cheat_sheets[topic]
        keyboard = [
            [InlineKeyboardButton(subtopic, callback_data=f"{topic}|{subtopic}")]
            for subtopic in subtopics.keys()
        ]
        keyboard.append([InlineKeyboardButton("⬅️ Back to Main Menu", callback_data="main_menu")])
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="Select a subtopic from Termux:", reply_markup=reply_markup)

# Subtopic selection handler
def handle_subtopic(update: Update, context: CallbackContext):
    """Handle the subtopic selection and show the content."""
    query = update.callback_query
    query.answer()

    # Extract topic and subtopic from the callback data
    topic, subtopic = query.data.split("|")
    content = cheat_sheets[topic][subtopic]

    # Add back button
    keyboard = [[InlineKeyboardButton("⬅️ Back", callback_data=f"{topic}")]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Display content with back button
    query.edit_message_text(text=content, reply_markup=reply_markup)

# Handle back to the main menu
def handle_main_menu(update: Update, context: CallbackContext):
    """Return to the main menu."""
    query = update.callback_query
    query.answer()

    # Display main menu
    keyboard = [[InlineKeyboardButton("Termux", callback_data="Termux")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Welcome back to the main menu! Select a topic:", reply_markup=reply_markup)

# Main function to run the bot
def main():
    # Create Updater and Dispatcher
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register command and callback handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(handle_topic, pattern="^Termux$"))
    dispatcher.add_handler(CallbackQueryHandler(handle_subtopic, pattern=".*\|.*"))
    dispatcher.add_handler(CallbackQueryHandler(handle_main_menu, pattern="^main_menu$"))

    # Start the bot
    print("Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
