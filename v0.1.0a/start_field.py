import field

class StartField(field.Field):
    def __init__(self, salary, field_id=1, field_name="START"):
        super().__init__(field_id, field_name)
        self.salary=salary

    def get_salary(self):
        return self.salary