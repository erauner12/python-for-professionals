class Cash(object):
    def __init__(self, value):
        self.value = value

    @property
    def formatted(self):
        return '${:.2f}'.format(self.value)

    @formatted.setter
    def formatted(self, new):
        self.value = float(new[1:])


wallet = Cash(2.50)
print(wallet.value)
wallet.formatted = '$123.45'
print(wallet.value)
