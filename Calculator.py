from ladon.ladonizer import ladonize

class Calculator(object):

        @ladonize(int, int, rtype=int)
        def add(self, a, b):
                return a + b

        @ladonize(int, int, rtype=int)
        def substract(self, a, b):
            return a - b

        @ladonize(int, int, rtype=int)
        def add(self, a, b):
            return a + b

        @ladonize(int, int, rtype=float)
        def divide(self, a, b):
            return a / b

