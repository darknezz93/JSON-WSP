from ladon.ladonizer import ladonize
from ladon.compat import PORTABLE_STRING

from Customer import Customer

class CustomerService(object):

    customers = []

    @ladonize(Customer, rtype=bool)
    def createCustomer(self, customer):
        self.customers.append(customer)
        if customer in self.customers:
            return True
        return False

    @ladonize(PORTABLE_STRING, rtype=Customer)
    def getCustomerById(self, id):
        for customer in self.customers:
            if customer.id == id:
                return customer
        return None

