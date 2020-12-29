class contacts:
    def __init__(self, contact_id, name, phone_no, email, address, uuid):
        self.contact_id = contact_id
        self.name = name
        self.phone_no = phone_no
        self.email = email
        self.address = address
        self.user_id = uuid

    def get_all(self):
        pass