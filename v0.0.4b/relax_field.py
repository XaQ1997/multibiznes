import field

class RelaxField(field.Field):
    def __init__(self, field_name, field_id=21):
        super().__init__(field_id, field_name)