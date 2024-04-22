import logging
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["book_rental"]
collection = db["books"]

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Xin chào! Hãy sử dụng lệnh /rent để thuê sách.')

def rent(update: Update, context: CallbackContext) -> None:
    book_name = " ".join(context.args)
    book = collection.find_one({"name": book_name})
    if book:
        if book["rented"]:
            update.message.reply_text("Sách đã được thuê.")
        else:
            collection.update_one({"_id": book["_id"]}, {"$set": {"rented": True}})
            update.message.reply_text(f"Thuê sách {book_name} thành công.")
    else:
        update.message.reply_text("Không tìm thấy sách.")

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Xin lỗi, tôi không hiểu yêu cầu của bạn.")

def main() -> None:
    # Thiết lập updater và dispatcher
    updater = Updater("7063104617:AAFY9UgdPCv60zcvQhJ_PBxY-TGM6XuzUYY")
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("rent", rent))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


def rent(update: Update, context: CallbackContext) -> None:
    book_name = " ".join(context.args)
    
    # Tìm kiếm sách trong cơ sở dữ liệu MongoDB
    book = collection.find_one({"name": book_name})
    if book:
        if book["rented"]:
            update.message.reply_text("Sách đã được thuê.")
        else:
            # Cập nhật trạng thái thuê của sách trong cơ sở dữ liệu
            collection.update_one({"_id": book["_id"]}, {"$set": {"rented": True}})
            update.message.reply_text(f"Thuê sách {book_name} thành công.")
    else:
        update.message.reply_text("Không tìm thấy sách.")
