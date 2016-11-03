from ladon.ladonizer import ladonize

class Calculator(object):

        @ladonize(int, int,rtype=int)
        def add(self, a, b):
                return a + b

        @ladonize(int, int, rtype=int)
        def susbtract(self, a, b):
            return a - b

        @ladonize(int, int, rtype=int)
        def add(self, a, b):
            return a + b

        @ladonize(int, int, rtype=int)
        def divide(self, a, b):
            return a / b

