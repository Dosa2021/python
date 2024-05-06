# fixture
import pytest

@pytest.fixture(scope='module')
def setup_module(request):
    print('setup_module')
    def teardown_procceccing():
        print('teardown_module')
    request.addfinalizer(teardown_procceccing)

class TestSec4_2():
    def test_hello(self, setup_procceccing):
        print('test_hello')


    def test_hello_2(self, setup_procceccing):
        print('test_hello_2')