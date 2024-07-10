import pytest
from translator import GoogleTranslator

@pytest.fixture(scope='module')
def trans():
    t = GoogleTranslator()
    print("Create Translator")
    return t

def test_japanese_to_english(trans, mocker):
    mocker.patch("translator.GoogleTranslator.convert", return_value = "hello")
    test_translated = trans.convert("俺はジャイアン", "日本語", "英語") 
    print(test_translated)