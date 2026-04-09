from googletrans import Translator

translator = Translator()

text = input("Enter English text: ")

# Translate to Italian (it)
translated = translator.translate(text, src='en', dest='it')

print("Italian translation:", translated.text)