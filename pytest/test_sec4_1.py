# fixture
import pytest

@pytest.fixture()
def setup_procceccing(request):
    # 前処理
    print('setup_procceccing')
    def teardown_procceccing():
        # 後処理
        print('teardown_procceccing')
    request.addfinalizer(teardown_procceccing)

def test_hello(setup_procceccing):
    print('test_hello')

def test_goodmorning():
    print('test_goodmorning')