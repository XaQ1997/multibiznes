import field

class ChanceField(field.Field):
    def __init__(self, field_id, field_name, field_colour):
        super().__init__(field_id, field_name)
        self.colour=field_colour