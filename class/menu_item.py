class MenuItem:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print('こんにちは')

    def info(self):
        print(self.name)

# menu_item_1 = MenuItem('サンドウィッチ')
# menu_item_1.hello()
# menu_item_1.info()