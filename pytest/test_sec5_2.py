# グループ名によるテストのskip
import pytest


def test_hello():
    print('test_hello')

# 2. これで、
# pytest pytest/test_sec5_2.py -m "morning"
# と実行すると、このメソッドのみテストされる
# 
# 逆に、
# pytest pytest/test_sec5_2.py -m "not morning"
# と実行すると、このメソッドのみテストされない
@pytest.mark.morning
def test_hello_2():
    print('test_hello_2')

def test_hello_3():
    print('test_hello_3')