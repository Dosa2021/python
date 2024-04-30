# 前処理 & 後処理

# 前処理
import pytest

# NOTE: こっちの書き方ではだめだった。（udemiy）下の書き方でいけた
# def step_function(function):
#     print('step_function')

@pytest.fixture()
def hoge():
    print('start----')
    yield
    print('end----')
    message = "hoge"
    return message


def test_hello_world(hoge):
    print('test_hello_world')



