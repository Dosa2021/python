class GoogleTranslator():
    def get_language_id(self, language_name):
        pass
        # languages = {
        #     '日本語': 'ja',
        #     '英語': 'en'
        # }
        # return languages[language_name]

    def convert(self, text_original, language_original_name, language_translator_name):
        language = self.get_language_id(language_translator_name)

        if language == 'ja':
            return "俺はジャイアン"

        return "My Name Is Sato."


# gt = GoogleTranslator()
# res = gt.convert("俺はジャイアン", "日本語", "英語")
# print('r--------------')
# print(res)
