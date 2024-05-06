# 関数名によるテストのskip
# 
# pytest pytest/test_sec5_3.py -k "hello" -s
# と実行することで、「hello」が含まれたテストのみ実行
def test_hello():
    print('test_hello')

def test_hello_2():
    print('test_hello_2')

def test_hello_3():
    print('test_hello_3')

def test_goodmorning():
    print('test_goodmorning')    