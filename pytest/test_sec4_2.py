# fixture を使って、クラスの前処理と後処理
import pytest

@pytest.fixture()
def setup_procceccing(request):
    print('setup_procceccing')
    def teardown_procceccing():
        print('teardown_procceccing')
    request.addfinalizer(teardown_procceccing)

class TestSec4_2():
    def test_hello(self, setup_procceccing):
        print('test_hello')

    def test_goodmorning(self):
        print('test_goodmorning')

    def test_goodafternoon(self, setup_procceccing):
        print('test_goodafternoon')