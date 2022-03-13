import field

class TaxField(field.Field):
    def __init__(self, field_id, field_name, field_tax):
        super().__init__(field_id, field_name)
        self.tax=field_tax