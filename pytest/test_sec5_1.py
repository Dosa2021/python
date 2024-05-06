# テストのskip
import pytest


def test_hello():
    print('test_hello')

# 1. これでこのメソッドのみskipされる
@pytest.mark.skip(reason="write reason")
def test_hello_2():
    print('test_hello_2')

def test_hello_3():
    print('test_hello_3')