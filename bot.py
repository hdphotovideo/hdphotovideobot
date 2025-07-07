import os
from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from photo_enhancer import enhance_photo
from video_enhancer import enhance_video

TOKEN = "7820406117:AAGbyDTykehhUtjp9V4r-nhp13zOar17D_c"

def handle_media(update: Update, ctx: CallbackContext):
    msg = update.message
    file = msg.photo[-1] if msg.photo else msg.video or msg.document
    if not file:
        msg.reply_text("कृपया Photo किंवा Video पाठवा.")
        return
    msg.reply_text("🔄 Enhancing, थोड्या वेळाने परत मिळेल…")
    fpath = file.get_file().download()
    out = ""
    if msg.photo:
        out = enhance_photo(fpath)
    else:
        out = enhance_video(fpath)
    msg.reply_document(open(out, 'rb'))
    os.remove(fpath); os.remove(out)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.photo | Filters.video | Filters.document.category("video"), handle_media))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
