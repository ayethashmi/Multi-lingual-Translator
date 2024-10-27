# pip install googletrans==4.0.0-rc1
# pip install easyocr

from googletrans import Translator

translator = Translator(service_urls=['translate.google.com'])
text = input("Enter a word: ")
lang = input("Enter the lang code: ")
translation = translator.translate(text, dest=lang)
print("Translation:", translation.text)