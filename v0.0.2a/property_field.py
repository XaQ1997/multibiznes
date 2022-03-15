import field
import property_card

class PropertyField(field.Field):
    def __init__(self, field_id, field_name, field_colour, field_value):
        super().__init__(field_id, field_name)
        self.colour=field_colour
        self.value=field_value