from datetime import datetime
from threading import Timer
import os
from selenium import webdriver
import time
from telegram.ext import Updater, CommandHandler
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def start(update, context):
    """Send a message when the command /start is issued."""

    tckn = "TCKN"

    sifre = "SIFRE"

    def lol():

        # get date
        datetime.today()
        datetime(2012, 3, 23, 23, 24, 55, 173504)
        date = datetime.today().weekday()
        # get time
        now = datetime.now()
        saat = now.strftime("%H:%M")

        path = os.getcwd()
        profile = path + r"\dyrdas9x.EBA"
        if "00.00" < saat < "14:40":
            date += 1

        oglen = 0

        fp = webdriver.FirefoxProfile(profile)
        driver = webdriver.Firefox(firefox_profile=fp)

        # giriş
        def giris():

            driver.get("https://eba.gov.tr/#/anasayfa")
            driver.find_element_by_xpath(
                "/html/body/app-root/app-anasayfa-page/div[2]/div/div/div[1]/div[2]/div[3]/div[3]/a[2]").click()
            driver.find_element_by_id("tckn").send_keys(tckn)
            driver.find_element_by_id("password").send_keys(sifre)
            driver.find_element_by_class_name("nl-form-send-btn").click()

        # derse katılım
        def katil():

            driver.get("https://eba.gov.tr/#/anasayfa")
            driver.find_element_by_xpath(
                "/html/body/app-root/app-anasayfa-page/div[2]/div/div/div[1]/div[2]/div[3]/div[3]/a[2]").click()
            time.sleep(2)
            driver.find_element_by_id("joinMeeting").click()
            time.sleep(2)
            driver.find_element_by_id("join").click()

        def ders():
            update.message.reply_text("Derse giriş yapılıyor!")
            katil()
            time.sleep(1800)  # DERS UZUNLUĞU
            update.message.reply_text("Ders Bitti! Beklemeye geçiliyor.")
            time.sleep(605)  # TENEFÜS UZUNLUĞU

        def okul():
            update.message.reply_text(f'Giriş yapılıyor..')
            giris()
            update.message.reply_text(f'Başarıyla Giriş Yapıldı!')
            ders_sayisi = 0
            while ders_sayisi < 8:
                ders()
                ders_sayisi += 1
            update.message.reply_text(f'Daha fazla dersin yok')
            tomorrow()

        def tomorrow():
            if oglen == 1:
                gun = datetime.today()
                yarin = gun.replace(day=gun.day + 1, hour=14, minute=50, second=30, microsecond=0)
                fark = yarin - gun
                sure = fark.seconds + 1
                update.message.reply_text(f'Dersin başlamasına {sure / 3600} saat kaldı!')
                t = Timer(sure, okul)
                t.start()
            else:

                gun = datetime.today()
                yarin = gun.replace(day=gun.day + 1, hour=9, minute=30, second=30, microsecond=0)
                fark = yarin - gun
                sure = fark.seconds + 1
                update.message.reply_text(f'Dersin başlamasına {sure / 3600} saat kaldı!')
                t = Timer(sure, okul)
                t.start()

        def today():
            if oglen == 1:
                gun = datetime.today()
                yarin = gun.replace(day=gun.day + 0, hour=14, minute=50, second=30, microsecond=0)
                fark = yarin - gun
                sure = fark.seconds + 1
                update.message.reply_text(f'Dersin başlamasına {sure / 3600} saat kaldı!')
                t = Timer(sure, okul)
                t.start()
            else:
                gun = datetime.today()
                yarin = gun.replace(day=gun.day + 0, hour=9, minute=30, second=30, microsecond=0)
                fark = yarin - gun
                sure = fark.seconds + 1
                update.message.reply_text(f'Dersin başlamasına {sure / 3600} saat kaldı!')
                t = Timer(sure, okul)
                t.start()

        if "09:30" > saat > "00.00":
            today()
        else:
            tomorrow()
    lol()


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("TOKEN GOES HERE", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))



    # log all errors
    dp.add_error_handler(logging.error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
