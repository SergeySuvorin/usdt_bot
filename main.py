

from email import message
from lib2to3.pgen2 import token
from logging import exception
from bs4 import BeautifulSoup
import requests
import jwt
import base64
import time
import datetime
import random
from binance_api import Binance
from binance.client import Client
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import os
from aiogram import Bot, Dispatcher, executor, types, asyncio

link_bestc_sell = 'https://bestcoin.cc/?refer_id=22&cur_from=USDTTRC20&cur_to=TCSBRUB&lng=ru'
link_alfa_buy = 'https://alfabit.exchange/ru/exchange/TCSBRUB/USDTBEP20'
p2p_link_b = 'https://p2p.binance.com/ru/trade/RosBank/USDT?fiat=RUB'
p2p_link_b_t='https://p2p.binance.com/ru/trade/Tinkoff/USDT?fiat=RUB'
p2p_link_s_tink = 'https://p2p.binance.com/ru/trade/sell/USDT?fiat=RUB&payment=Tinkoff'
p2p_link_s_rosb = 'https://p2p.binance.com/ru/trade/sell/USDT?fiat=RUB&payent=RosBank&payment=RosBank'

p2p_link_b_raif = 'https://p2p.binance.com/ru/trade/RaiffeisenBankRussia/USDT?fiat=RUB'
p2p_link_s_raif = 'https://p2p.binance.com/ru/trade/sell/USDT?fiat=RUB&payment=RaiffeisenBankRussia'
p2p_link_b_qiwi = 'https://p2p.binance.com/ru/trade/QIWI/USDT?fiat=RUB'
p2p_link_s_qiwi = 'https://p2p.binance.com/ru/trade/sell/USDT?fiat=RUB&payment=QIWI'




def jwts():
    private_key = 'private=key'
    uid = 'uid'

    host = 'garantex.io'

    key = base64.b64decode(private_key)
    iat = int(time.mktime(datetime.datetime.now().timetuple()))

    claims = {
        "exp": iat + 1*60*60,  # JWT Request TTL in seconds since epoch
        "jti": hex(random.getrandbits(12)).upper()
    }

    jwt_token = jwt.encode(claims, key, algorithm="RS256")
    ret = requests.post('https://dauth.' + host + '/api/v1/sessions/generate_jwt',
                        json={'kid': uid, 'jwt_token': jwt_token})
    token = ret.json().get('token')
    return token

host = 'garantex.io'
ret = requests.get('https://' + host + '/api/v2/depth?market=usdtrub', headers={'Authorization': 'Bearer ' + jwts()})


api_key = 'api'
api_secret = 'api_s'
client = Binance(api_key, api_secret)


def bestcoin():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(url= link_bestc_sell)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source,"lxml")
    driver.close()
    driver.quit()
    return soup.find('aside').text

def alfa_b():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(url= link_alfa_buy)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source,"lxml")
    driver.close()
    driver.quit()
    return soup.find('div','text-center').text


def p2p_b():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(url= p2p_link_b)
    time.sleep(5)
    driver.find_element_by_id('onetrust-accept-btn-handler').click()
    time.sleep(3)
    driver.find_element_by_class_name('css-1pcqseb').click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source,"lxml")
    driver.close()
    driver.quit()
    return soup.find("div", 'css-1kj0ifu').text, soup.find("div", 'css-1rhb69f').text,soup.find("div", 'css-1a0u4z7').text,soup.find("div", 'css-19crpgd').text,soup.find("div", 'css-1kj0ifu').text,soup.find("div", 'css-3v2ep2').text,soup.find("div", 'css-16w8hmr').text 
    
def p2p_b_t():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(url= p2p_link_b_t)
    time.sleep(5)
    driver.find_element_by_id('onetrust-accept-btn-handler').click()
    time.sleep(3)
    driver.find_element_by_class_name('css-1pcqseb').click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source,"lxml")
    driver.close()
    driver.quit()
    return soup.find("div", 'css-1kj0ifu').text, soup.find("div", 'css-1rhb69f').text,soup.find("div", 'css-1a0u4z7').text,soup.find("div", 'css-19crpgd').text,soup.find("div", 'css-1kj0ifu').text,soup.find("div", 'css-3v2ep2').text,soup.find("div", 'css-16w8hmr').text 

def p2p_s_rosb():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(url= p2p_link_s_rosb)
    time.sleep(5)
    driver.find_element_by_id('onetrust-accept-btn-handler').click()
    time.sleep(3)
    driver.find_element_by_class_name('css-1pcqseb').click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source,"lxml")
    driver.close()
    driver.quit()
    return soup.find("div", 'css-1kj0ifu').text, soup.find("div", 'css-1rhb69f').text,soup.find("div", 'css-1a0u4z7').text,soup.find("div", 'css-19crpgd').text,soup.find("div", 'css-1kj0ifu').text,soup.find("div", 'css-3v2ep2').text,soup.find("div", 'css-16w8hmr').text 

def p2p_s_tink():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(url= p2p_link_s_tink)
    time.sleep(5)
    driver.find_element_by_id('onetrust-accept-btn-handler').click()
    time.sleep(3)
    driver.find_element_by_class_name('css-1pcqseb').click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source,"lxml")
    driver.close()
    driver.quit()
    return soup.find("div", 'css-1kj0ifu').text, soup.find("div", 'css-1rhb69f').text,soup.find("div", 'css-1a0u4z7').text,soup.find("div", 'css-19crpgd').text,soup.find("div", 'css-1kj0ifu').text,soup.find("div", 'css-3v2ep2').text,soup.find("div", 'css-16w8hmr').text 

def p2p_b_raif():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(url= p2p_link_b_raif)
    time.sleep(5)
    driver.find_element_by_id('onetrust-accept-btn-handler').click()
    time.sleep(3)
    driver.find_element_by_class_name('css-1pcqseb').click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source,"lxml")
    driver.close()
    driver.quit()
    return soup.find("div", 'css-1kj0ifu').text, soup.find("div", 'css-1rhb69f').text,soup.find("div", 'css-1a0u4z7').text,soup.find("div", 'css-19crpgd').text,soup.find("div", 'css-1kj0ifu').text,soup.find("div", 'css-3v2ep2').text,soup.find("div", 'css-16w8hmr').text 

def p2p_s_raif():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(url= p2p_link_s_raif)
    time.sleep(5)
    driver.find_element_by_id('onetrust-accept-btn-handler').click()
    time.sleep(3)
    driver.find_element_by_class_name('css-1pcqseb').click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source,"lxml")
    driver.close()
    driver.quit()
    return soup.find("div", 'css-1kj0ifu').text, soup.find("div", 'css-1rhb69f').text,soup.find("div", 'css-1a0u4z7').text,soup.find("div", 'css-19crpgd').text,soup.find("div", 'css-1kj0ifu').text,soup.find("div", 'css-3v2ep2').text,soup.find("div", 'css-16w8hmr').text 

def p2p_b_qiwi():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(url= p2p_link_b_qiwi)
    time.sleep(5)
    driver.find_element_by_id('onetrust-accept-btn-handler').click()
    time.sleep(3)
    driver.find_element_by_class_name('css-1pcqseb').click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source,"lxml")
    driver.close()
    driver.quit()
    return soup.find("div", 'css-1kj0ifu').text, soup.find("div", 'css-1rhb69f').text,soup.find("div", 'css-1a0u4z7').text,soup.find("div", 'css-19crpgd').text,soup.find("div", 'css-1kj0ifu').text,soup.find("div", 'css-3v2ep2').text,soup.find("div", 'css-16w8hmr').text 

def p2p_s_qiwi():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get(url= p2p_link_s_qiwi)
    time.sleep(5)
    driver.find_element_by_id('onetrust-accept-btn-handler').click()
    time.sleep(3)
    driver.find_element_by_class_name('css-1pcqseb').click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source,"lxml")
    driver.close()
    driver.quit()
    return soup.find("div", 'css-1kj0ifu').text, soup.find("div", 'css-1rhb69f').text,soup.find("div", 'css-1a0u4z7').text,soup.find("div", 'css-19crpgd').text,soup.find("div", 'css-1kj0ifu').text,soup.find("div", 'css-3v2ep2').text,soup.find("div", 'css-16w8hmr').text 











def main():
    p2p_buy = p2p_b()
    p2p_buy_t = p2p_b_t()
    p2p_sell_t = p2p_s_tink()
    p2p_sell_r = p2p_s_rosb()
    bestcoin_sell = bestcoin()
    garantex_buy = requests.get('https://' + host + '/api/v2/depth?market=usdtrub', headers={'Authorization': 'Bearer ' + jwts()}).json().pop("asks")[0].pop("price")
    garantex_sell = requests.get('https://' + host + '/api/v2/depth?market=usdtrub', headers={'Authorization': 'Bearer ' + jwts()}).json().pop("bids")[0].pop("price")
    bnb = client.depth(symbol='USDTRUB').pop("asks")[0][0][:5]
    bns = client.depth(symbol='USDTRUB').pop("bids")[0][0][:5]
    alfa_br = alfa_b()[20:25]
    p2p_buy_raif = p2p_b_raif()
    p2p_sell_raif = p2p_s_raif()
    p2p_buy_qiwi = p2p_b_qiwi()
    p2p_sell_qiwi = p2p_s_qiwi()
    return p2p_buy, p2p_buy_t, p2p_sell_t, p2p_sell_r, bestcoin_sell, garantex_buy, garantex_sell, bnb, bns, alfa_br, p2p_buy_raif, p2p_sell_raif, p2p_buy_qiwi, p2p_sell_qiwi


TOKEN = "bot_token"
bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.reply("What's up Doc?\n Let's do everything right now!")



spread = 1.007
spread_with_garantex = 1.01
async def svyazki():
    while True:
            @dp.message_handler(commands='start')
            async def start(message:types.Message):
                await message.reply("What's up Doc?\n Let's do everything right now!")

            temp = main()
            p2p_buyer = float(temp[0][0][:5])
            p2p_buyer_t = float(temp[1][0][:5])
            p2p_seller_t = float(temp[2][0][:5])
            p2p_seller_r = float(temp[3][0][:5])
            bestcoin_seller = float(temp[4][-10:-5])
            garantex_buyer = float(temp[5])*1.002
            garantex_seller = float(temp[6])*0.998
            binance_buyer = float(temp[7])*1.15
            binance_seller = float(temp[8])
            alfa_buyer = float(temp[9])
            p2p_buyer_raif = float(temp[10][0][:5])
            p2p_seller_raif = float(temp[11][0][:5])
            p2p_buyer_qiwi = float(temp[12][0][:5])
            p2p_seller_qiwi = float(temp[13][0][:5])
            # print(p2p_buyer,p2p_buyer_t,p2p_seller_t,p2p_seller_r,bestcoin_seller,garantex_buyer,garantex_seller,binance_buyer,binance_seller,alfa_buyer,p2p_buyer_raif,p2p_seller_raif, p2p_buyer_qiwi,p2p_seller_qiwi)
            if bestcoin_seller/garantex_buyer>=spread_with_garantex:
                for i in range(1):
                    await bot.send_message(-1001762743594,'*Buy Garantex -> Sell Bestcoin*✅' +f'\nGarantex_price = {garantex_buyer} ₽\nBestcoin_price = {bestcoin_seller} ₽\n*SPREAD* = {round(bestcoin_seller/garantex_buyer,3)} 🔥', parse_mode="Markdown")
                
            if p2p_seller_r/garantex_buyer>=spread_with_garantex and p2p_seller_r != 74.81:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy Garantex -> Sell p2p Росбанк</b>✅\nGarantex_price = {garantex_buyer} ₽\nP2P_Rosbank_price = {p2p_seller_r} ₽\n<b>SPREAD</b> = {round(p2p_seller_r/garantex_buyer,3)} 🔥 ', parse_mode="HTML")
                
            if p2p_seller_t/garantex_buyer>=spread_with_garantex and p2p_seller_t != 74.81:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy Garantex -> Sell p2p Тинькофф</b>✅' + f'\nGarantex_price = {garantex_buyer} ₽\nP2P_Tinkoff_price = {p2p_seller_t} ₽\n<b>SPREAD</b> = {round(p2p_seller_t/garantex_buyer,3)} 🔥', parse_mode="HTML")
            
            if garantex_seller/p2p_buyer>=spread_with_garantex and p2p_buyer != 74.81:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy p2p Росбанк -> Sell Garantex</b>✅ \nP2P_Rosbank_price = {p2p_buyer} ₽\nGarantex_price = {garantex_seller} ₽\n<b>SPREAD</b> = {round(garantex_seller/p2p_buyer,3)} 🔥',parse_mode="HTML" )

            if garantex_seller/p2p_buyer_t>=spread_with_garantex and p2p_buyer_t != 74.81:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy p2p Тинькофф -> Sell Garantex</b>✅ \nP2P_Tinkoff_price = {p2p_buyer_t} ₽\nGarantex_price = {garantex_seller} ₽\n<b>SPREAD</b> = {round(garantex_seller/p2p_buyer_t,3)} 🔥',parse_mode="HTML" )   
        
            if bestcoin_seller/p2p_buyer>=spread and p2p_buyer != 74.81:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy p2p Росбанк -> Sell Bestcoin</b>✅ \nP2P_Rosbank_price = {p2p_buyer} ₽\nBestcoin_price = {bestcoin_seller} ₽\n<b>SPREAD</b> = {round(bestcoin_seller/p2p_buyer,3)} 🔥',parse_mode="HTML" )
            
            if bestcoin_seller/p2p_buyer_t>=spread and p2p_buyer_t != 74.81:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy p2p Тинькофф -> Sell Bestcoin</b>✅ \nP2P_Tinkoff_price = {p2p_buyer_t} ₽\nBestcoin_price = {bestcoin_seller} ₽\n<b>SPREAD</b> = {round(bestcoin_seller/p2p_buyer_t,3)} 🔥',parse_mode="HTML" )
        
            if garantex_seller/binance_buyer >= spread_with_garantex:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy Binance -> Sell Garantex</b>✅ \nBinance_price (с учетом покупки рублей на p2p) = {binance_buyer} ₽\nGarantex_price = {garantex_seller} ₽\n<b>SPREAD</b> = {round(garantex_seller/binance_buyer,3)} 🔥',parse_mode="HTML" )
        
            if garantex_seller/alfa_buyer >= spread_with_garantex:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy AlfaBit -> Sell Garantex</b>✅ \nAlfaBit_price = {alfa_buyer} ₽\nGarantex_price = {garantex_seller} ₽\n<b>SPREAD</b> = {round(garantex_seller/alfa_buyer,3)} 🔥',parse_mode="HTML" )
        
            if p2p_seller_r/alfa_buyer >= spread and p2p_seller_r != 74.81:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy AlfaBit -> Sell p2p Росбанк</b>✅ \nAlfaBit_price = {alfa_buyer} ₽\nP2P_Rosbank_price = {p2p_seller_r} ₽\n<b>SPREAD</b> = {round(p2p_seller_r/alfa_buyer,3)} 🔥',parse_mode="HTML" )
                
            if bestcoin_seller/binance_buyer>= spread:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy Binance -> Sell Bestcoin</b>✅ \nBinance_price (с учетом покупки рублей на p2p) = {binance_buyer} ₽\nBestcoin_price = {bestcoin_seller} ₽\n<b>SPREAD</b> = {round(bestcoin_seller/binance_buyer,3)} 🔥',parse_mode="HTML")

            if p2p_seller_r/binance_buyer>= spread and p2p_seller_r != 74.81:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy Binance -> Sell P2P Росбанк</b>✅ \nBinance_price (с учетом покупки рублей на p2p) = {binance_buyer} ₽\nP2P_Rosbank_price = {p2p_seller_r} ₽\n<b>SPREAD</b> = {round(p2p_seller_r/binance_buyer,3)} 🔥',parse_mode="HTML")

            if p2p_seller_t/binance_buyer>= spread and p2p_seller_t != 74.81:
                    for i in range(1):
                        await bot.send_message(-1001762743594,f'<b>Buy Binance -> Sell P2P Тинькофф</b>✅ \nBinance_price (с учетом покупки рублей на p2p) = {binance_buyer} ₽\nP2P_Tinkoff_price = {p2p_seller_t} ₽\n<b>SPREAD</b> = {round(p2p_seller_t/binance_buyer,3)} 🔥',parse_mode="HTML")


            if p2p_seller_raif/binance_buyer >= spread and p2p_seller_raif != 74.81:
                    for i in range(1):
                        await bot.send_message(-1001762743594,f'<b>Buy Binance -> Sell P2P Raif</b>✅ \nBinance_price (с учетом покупки рублей на p2p) = {binance_buyer} ₽\nP2P_Raif_price = {p2p_seller_raif} ₽\n<b>SPREAD</b> = {round(p2p_seller_raif/binance_buyer,3)} 🔥',parse_mode="HTML")

            if p2p_seller_qiwi/binance_buyer>= spread and p2p_seller_qiwi != 74.81:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy Binance -> Sell P2P Qiwi</b>✅ \nBinance_price (с учетом покупки рублей на p2p) = {binance_buyer} ₽\nP2P_Qiwi_price = {p2p_seller_qiwi} ₽\n<b>SPREAD</b> = {round(p2p_seller_qiwi/binance_buyer,3)} 🔥',parse_mode="HTML")

            if p2p_seller_raif/alfa_buyer >= spread and p2p_seller_raif != 74.81:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy AlfaBit -> Sell p2p Raif</b>✅ \nAlfaBit_price = {alfa_buyer} ₽\nP2P_Raif_price = {p2p_seller_raif} ₽\n<b>SPREAD</b> = {round(p2p_seller_raif/alfa_buyer,3)} 🔥',parse_mode="HTML" )

            if p2p_seller_qiwi/alfa_buyer >= spread and p2p_seller_qiwi != 74.81:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy AlfaBit -> Sell p2p Qiwi</b>✅ \nAlfaBit_price = {alfa_buyer} ₽\nP2P_Qiwi_price = {p2p_seller_qiwi} ₽\n<b>SPREAD</b> = {round(p2p_seller_qiwi/alfa_buyer,3)} 🔥',parse_mode="HTML" )

            if bestcoin_seller/p2p_buyer_raif>=spread and p2p_buyer_raif != 74.81:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy p2p Raif -> Sell Bestcoin</b>✅ \nP2P_Raif_price = {p2p_buyer_raif} ₽\nBestcoin_price = {bestcoin_seller} ₽\n<b>SPREAD</b> = {round(bestcoin_seller/p2p_buyer_raif,3)} 🔥',parse_mode="HTML" )

            if bestcoin_seller/p2p_buyer_qiwi>=spread and p2p_buyer_qiwi != 74.81:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy p2p Qiwi -> Sell Bestcoin</b>✅ \nP2P_Qiwi_price = {p2p_buyer_qiwi} ₽\nBestcoin_price = {bestcoin_seller} ₽\n<b>SPREAD</b> = {round(bestcoin_seller/p2p_buyer_qiwi,3)} 🔥',parse_mode="HTML" )

            if garantex_seller/p2p_buyer_raif>=spread_with_garantex and p2p_buyer_raif != 74.81:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy p2p raif -> Sell Garantex</b>✅ \nP2P_Raif_price = {p2p_buyer_raif} ₽\nGarantex_price = {garantex_seller} ₽\n<b>SPREAD</b> = {round(garantex_seller/p2p_buyer_raif,3)} 🔥',parse_mode="HTML" )   

            if garantex_seller/p2p_buyer_qiwi>=spread_with_garantex and p2p_buyer_qiwi != 74.81:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy p2p Qiwi -> Sell Garantex</b>✅ \nP2P_Qiwi_price = {p2p_buyer_qiwi} ₽\nGarantex_price = {garantex_seller} ₽\n<b>SPREAD</b> = {round(garantex_seller/p2p_buyer_qiwi,3)} 🔥',parse_mode="HTML" )   

            if p2p_seller_raif/garantex_buyer>=spread_with_garantex and p2p_seller_raif != 74.81:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy Garantex -> Sell p2p Raif</b>✅\nGarantex_price = {garantex_buyer} ₽\nP2P_Raif_price = {p2p_seller_raif} ₽\n<b>SPREAD</b> = {round(p2p_seller_raif/garantex_buyer,3)} 🔥 ', parse_mode="HTML")

            if p2p_seller_qiwi/garantex_buyer>=spread_with_garantex and p2p_seller_qiwi != 74.81:
                for i in range(1):
                    await bot.send_message(-1001762743594,f'<b>Buy Garantex -> Sell p2p Qiwi</b>✅\nGarantex_price = {garantex_buyer} ₽\nP2P_Qiwi_price = {p2p_seller_qiwi} ₽\n<b>SPREAD</b> = {round(p2p_seller_qiwi/garantex_buyer,3)} 🔥 ', parse_mode="HTML")


        
            await asyncio.sleep(20)




if __name__ == "__main__":
    asyncio.run(svyazki())
    executor.start_polling(dp, skip_updates=True)


