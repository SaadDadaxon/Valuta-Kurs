import requests
from bot import dp, bot
from aiogram import executor
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from reply import menu


url2 = f'https://v6.exchangerate-api.com/v6/0753aa896d38ae15e6abdf9e/pair/USD/UZS'

response = requests.get(url2)
data = response.json()

print(data)


@dp.message_handler(Command('start'))
async def start(ms: Message):
    txt = f"Assalomu Alaykum Mr.{ms.from_user.full_name} siz bu bot orqali o'zingizga kerakli valuta kurslarini aniqlab olishingiz mumkin"
    await ms.answer(txt, reply_markup=menu)


@dp.message_handler(text='Valuta Kurslar')
async def kalit(ms: Message):
    kalitlar = ("USD/ " "LSL/ " "LYD/ " "MAD/ " "MDL/ " "MGA/ " "MKD/ " "MMK/ "
                "MNT/ " "MOP/ " "MRU/ " "MUR/ " "MVR/ " "MWK/ " "MXN/ " "MYR/ "
                "MZN/ " "NAD/ " "NGN/ " "NIO/ " "NOK/ " "NPR/ " "NZD/ " "OMR/ "
                "PAB/ " "PEN/ " "PGK/ " "PHP/ " "PKR/ " "PLN/ " "PYG/ " "QAR/ "
                "RON/ " "RSD/ " "RUB/ " "RWF/ " "SAR/ " "SBD/ " "SCR/ " "SDG/ "
                "SEK/ " "SGD/ " "SHP/ " "SLE/ " "SLL/ " "SOS/ " "SRD/ " "SSP/ "
                "STN/ " "SYP/ " "SZL/ " "THB/ " "TJS/ " "TMT/ " "TND/ " "TOP/ "
                "TRY/ " "TTD/ " "TVD/ " "TWD/ " "TZS/ " "UAH/ " "UGX/ " "UYU/ "
                "UZS/ " "VES/ " "VND/ " "VUV/ " "WST/ " "XAF/ " "XCD/ " "XDR/ "
                "XOF/ " "XPF/ " "YER/ " "ZAR/ " "ZMW/ " "ZWL/ " "AED/ " "AFN/ "
                "ALL/ " "AMD/ " "ANG/ " "AOA/ " "ARS/ " "AUD/ " "AWG/ " "AZN/ "
                "BAM/ " "BBD/ " "BDT/ " "BGN/ " "BHD/ " "BIF/ " "BMD/ " "BND/ "
                "BOB/ " "BRL/ " "BSD/ " "BTN/ " "BWP/ " "BYN/ " "BZD/ " "CAD/ "
                "CDF/ " "CHF/ " "CLP/ " "CNY/ " "COP/ " "CRC/ " "CUP/ " "CVE/ "
                "CZK/ " "DJF/ " "DKK/ " "DOP/ " "DZD/ " "EGP/ " "ERN/ " "ETB/ "
                "EUR/ " "FJD/ " "FKP/ " "FOK/ " "GBP/ " "GEL/ " "GGP/ " "GHS/ "
                "GIP/ " "GMD/ " "GNF/ " "GTQ/ " "GYD/ " "HKD/ " "HNL/ " "HRK/ "
                "HTG/ " "HUF/ " "IDR/ " "ILS/ " "IMP/ " "INR/ " "IQD/ " "IRR/ "
                "ISK/ " "JEP/ " "JMD/ " "JOD/ " "JPY/ " "KES/ " "KGS/ " "KHR/ "
                "KID/ " "KMF/ " "KRW/ " "KWD/ " "KYD/ " "KZT/ " "LAK/ " "LBP/ "
                "LKR/ " "LRD/ ")
    ishlatish = f"Mr.{ms.from_user.full_name} sizga kerakli valutani💰 (Masalan: USD/UZS) ko'rinishida Yozing"
    await ms.answer(kalitlar)
    print(ms.from_user.full_name)
    print(ms.text)
    await ms.answer(ishlatish)


@dp.message_handler(text='Bot Yaratuvchisi')
async def kalit(ms: Message):
    txt = f"Bot Yaratuvchisi Mr.Dadakhon @DadaXON_Saad"
    await ms.answer(txt)


@dp.message_handler()
async def valuta(ms: Message):
    try:
        ker = ms.text
        response = requests.get(f'https://v6.exchangerate-api.com/v6/0753aa896d38ae15e6abdf9e/pair/{ker}')
        data = response.json()
        kurs = data['conversion_rate']
        sotish = data['base_code']
        olish = data['target_code']
        txt1 = f"Mr.{ms.from_user.full_name} siz olmoqchi bo'lgan valuta💰 1 {sotish}💲 = {kurs} {olish} "
        print(ms.from_user.full_name)
        print(ms.text)
        await ms.answer(txt1)
    except:
        print(ms.from_user.full_name)
        print(ms.text)
        await ms.answer("Siz kalit so'zini xato kiritding")


if __name__ == '__main__':
    executor.start_polling(dp)
