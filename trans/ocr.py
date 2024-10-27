import easyocr
from googletrans import Translator
translator = Translator(service_urls=['translate.google.com'])

#reader = easyocr.Reader(['ur','en']) # this needs to run only once to load the model into memory
reader = easyocr.Reader(['ur','en'], gpu=False)
output = reader.readtext('test.jpg', detail = 0)

print(output)
translation = translator.translate(output[0], dest='en')
print("Translation:", translation.text)