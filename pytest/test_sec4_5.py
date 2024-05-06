# fixture
import pytest

@pytest.fixture(autouse=True)
def setup_module(request):
    print('setup_module')
    def teardown_procceccing():
        print('teardown_module')
    request.addfinalizer(teardown_procceccing)

class TestSec4_5():
    def test_hello(self):
        print('test_hello')


    def test_hello_2(self):
        print('test_hello_2')