from telegram import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler

# Replace with your actual bot token
TOKEN = "7727818329:AAFhHktxV1WmqtmWTloeJHCH2HQ3Fd39Z3I"

async def start(update: Update, context):
    """Send a welcome message with a game link."""
    game_link = "https://srivathsavsree.github.io/jump-game/"  # Your GitHub Pages game link
    keyboard = [
        [
            InlineKeyboardButton("Play Game", url=game_link)
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to the Jump Game! Click below to play.", reply_markup=reply_markup)

async def help_command(update: Update, context):
    """Send help message."""
    await update.message.reply_text("Use /start to play the game.")

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Add bot commands
    commands = [BotCommand("start", "Start the game"), BotCommand("help", "Get help")]
    application.bot.set_my_commands(commands)

    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
