from dao.customer_dao import CustomerDao
from exception.invalid_parameter import InvalidParameterError
from exception.customer_not_found import CustomerNotFoundError


class CustomerService:

    def __init__(self):
        self.customer_dao = CustomerDao()


    def get_all_customers(self):
        list_of_customer_objects = self.customer_dao.get_all_customers()


        list_of_customer_dictionaries = []
        for customer_obj in list_of_customer_objects:
            list_of_customer_dictionaries.append(customer_obj.to_dict())

        return list_of_customer_dictionaries





    def get_customer_by_id(self, customer_id):
        customer_obj = self.customer_dao.get_customer_by_id(customer_id)
        if not customer_obj:
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")

        return customer_obj.to_dict()






    def delete_customer_by_id(self, customer_id):
        if not self.customer_dao.delete_customer_by_id(customer_id):
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")






    def add_customer(self, customer_object):
        if " " in customer_object.firstname:
            raise InvalidParameterError("Firstname cannot contain spaces")

        if len(customer_object.firstname) < 1:
            raise InvalidParameterError("Firstname must be at least 1 character")

        added_customer_object = self.customer_dao.add_customer(customer_object)
        return added_customer_object.to_dict()





    def update_customer_by_id(self, customer_object):
        updated_customer_object = self.customer_dao.update_customer_by_id(customer_object)

        if updated_customer_object is None:
            raise CustomerNotFoundError(f"Customer with id {customer_object.id} was not found")

        return updated_customer_object.to_dict()