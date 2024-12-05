from googletrans import Translator

class GoogleTranslator():
    def __init__(self):
        self.translator = Translator()

    def get_language_id(self, language_name):
        languages = {
            '日本語': 'ja',
            '英語': 'en'
        }
        return languages[language_name]

    def convert(self, text_original, language_original_name, language_translator_name):
        language_original_id = self.get_language_id(language_original_name)
        language_translator_id = self.get_language_id(language_translator_name)
        text_original_translator = self.translator.translate(text_original, dest=language_translator_id)
        return text_original_translator.text

gt = GoogleTranslator()
res = gt.convert("俺はジャイアン", "日本語", "英語")
print('res-----')
print(res)
