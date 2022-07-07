from model.customer import Customer
import psycopg
import copy


class CustomerDao:

    def get_all_customers(self):

        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="Iloveyou27") as conn:

            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers")

                my_list_of_customer_objs = []

                for customer in cur:
                    u_id = customer[0]
                    firstname = customer[1]
                    birthday = customer[2]
                    active = customer[3]

                    my_customer_obj = Customer(u_id, firstname, birthday, active)
                    my_list_of_customer_objs.append(my_customer_obj)

                return my_list_of_customer_objs


    def get_customer_by_id(self, customer_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="Iloveyou27") as conn:

            with conn.cursor() as cur:

                cur.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))

                customer_row = cur.fetchone()
                if not (customer_row):
                    return None

                u_id = customer_row[0]
                firstname = customer_row[1]
                birthday = customer_row[2]
                active = customer_row[3]

                return Customer(u_id, firstname, birthday, active)



    def delete_customer_by_id(self, customer_id):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="Iloveyou27") as conn:

            with conn.cursor() as cur:
                cur.execute("DELETE FROM customers WHERE id = %s", (customer_id,))


                rows_deleted = cur.rowcount

                if rows_deleted != 1:
                    return False
                else:
                    conn.commit()
                    return True





    def add_customer(self, customer_object):
        firstname_to_add = customer_object.firstname
        birthday_to_add = customer_object.birthday

        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="Iloveyou27") as conn:

            with conn.cursor() as cur:
                cur.execute("INSERT INTO customers (firstname, birthday) VALUES (%s, %s) RETURNING *", (firstname_to_add,
                                                                                                       birthday_to_add))

                customer_row_that_was_just_inserted = cur.fetchone()
                conn.commit()
                return Customer(customer_row_that_was_just_inserted[0], customer_row_that_was_just_inserted[1],
                            customer_row_that_was_just_inserted[2], customer_row_that_was_just_inserted[3])




    def update_customer_by_id(self, customer_object):
        with psycopg.connect(host="127.0.0.1", port="5432", dbname="postgres", user="postgres",
                             password="Iloveyou27") as conn:

            with conn.cursor() as cur:
                cur.execute("UPDATE customers SET firstname = %s, birthday = %s, active_customer = %s WHERE id = %s RETURNING *",
                            (customer_object.firstname, customer_object.birthday, customer_object.active, customer_object.id))

                conn.commit()

                updated_customer_row = cur.fetchone()
                if updated_customer_row is None:
                    return None

                return Customer(updated_customer_row[0], updated_customer_row[1], updated_customer_row[2], updated_customer_row[3])





