# fixture
import pytest

@pytest.fixture(scope='class')
def setup_procceccing(request):
    print('setup_procceccing')
    def teardown_procceccing():
        print('teardown_procceccing')
    request.addfinalizer(teardown_procceccing)

class TestSec4_2():
    def test_hello(self, setup_procceccing):
        print('test_hello')


    def test_hello_2(self, setup_procceccing):
        print('test_hello_2')