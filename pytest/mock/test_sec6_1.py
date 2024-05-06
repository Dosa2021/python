from translator import GoogleTranslator
import pytest

@pytest.fixture(scope='module')
def trans():
    t = GoogleTranslator()
    print("Create Translator")
    return t


# def test_japanese_to_english(trans):
#     test_translated = trans.convert("俺はジャイアン", "日本語", "英語")
#     assert test_translated == "My Name Is Sato."

# mockerを使用し、GoogleTranslatorクラスのconvertメソッドの返り値をモックする
def test_japanese_to_english(trans, mocker):
    mocker.patch("translator.GoogleTranslator.convert", return_value = "hello world!")
    test_translated = trans.convert("俺はジャイアン", "日本語", "英語")
    print(test_translated)

def test_english_to_japanese(trans, mocker):
    mocker.patch("translator.GoogleTranslator.get_language_id", return_value = "ja")
    test_translated = trans.convert("My Name Is Sato.", "英語", "日本語")
    assert test_translated == "俺はジャイアン"