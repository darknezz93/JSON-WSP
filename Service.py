from ladon.compat import PORTABLE_STRING
from ladon.ladonizer import ladonize

class Service(object):

        @ladonize(PORTABLE_STRING,rtype=str)
        def hello(self,name):
                return "Hello " + name