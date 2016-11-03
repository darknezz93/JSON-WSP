from ladon.types.ladontype import LadonType

class Customer(LadonType):
    id = {
        'type': str
    }
    name = {
        'type': str
    }
    age = {
        'type': int,
        'nullable': True
    }
    receive_newsletter = {
        'type': bool,
        'nullable': False,
        'default': False
    }