import field

class PolicemanField(field.Field):
    def __init__(self, sending_id, field_id=31, field_name="Policjant"):
        super().__init__(field_id, field_name)
        self.sending_id=sending_id