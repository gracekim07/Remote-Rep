class Customer:
    def __init__(self, id, firstname, birthday, active):
        self.id = id
        self.firstname = firstname
        self.birthday = birthday
        self.active = active

    def to_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "birthday": self.birthday,
            "active": self.active
        }