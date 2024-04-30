# 様々なテスト関数
def test_calculate():
    result = 5 * 2
    assert result == 10

def test_len():
    text = "h"
    assert len(text) == 1

def test_contain():
    text = "hello"
    assert "ll" in text