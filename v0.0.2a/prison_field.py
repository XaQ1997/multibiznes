import field

class PrisonField(field.Field):
    def __init__(self, field_id=11, field_name='Więzienie'):
        super().__init__(field_id, field_name)
        self.prisoners={}

    def add_prisoner(self, prisoner):
        self.prisoners[prisoner.name]=3

    def get_prisoners(self):
        return self.prisoners