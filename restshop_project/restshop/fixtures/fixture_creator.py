from collections import defaultdict


class FixtureCreator:

    PROPERTY = 'restshop.Property'
    PROPERTY_VALUE = 'restshop.PropertyValue'
    TAG = 'restshop.Tag'
    USER = 'auth.User'
    SELLER = 'restshop.Seller'
    PRODUCT = 'restshop.Product'
    UNIT = 'restshop.Unit'
    UNIT_IMAGE = 'restshop.UnitImage'

    def __init__(self, data):
        """Initialize fixtures.

        Fixtures for each model are stored in self._fixtures dict,
        where the key is the name of the model.
        """
        self._data = data
        self._fixtures = defaultdict(list)
        self._auto_ids = defaultdict(int)

        self._init_properties()
        self._init_property_values()

    def get_fixtures(self):
        """Return valid Django fixtures list."""
        result = []

        fixtures_order = [
            self.PROPERTY,
            self.PROPERTY_VALUE,
            self.TAG,
            self.USER,
            self.SELLER,
            self.PRODUCT,
            self.UNIT,
            self.UNIT_IMAGE,
        ]

        for key in fixtures_order:
            result += self._fixtures[key]

        return result

    def _auto_id(self, model_name):
        """Get id for new record (counted in ascending order from 1)."""
        self._auto_ids[model_name] += 1
        return self._auto_ids[model_name]

    def _get_id(self, model_name, fields, values):
        """Get id of a specific record.

        Argument 'fields' can be either string or list of strings.
        Arguments 'values' can be any type, if 'fields' is a string.
        Otherwise, 'values' must be a list, too.

        Returns the first record in 'model_name' model,
        where all 'fields' values equal to corresponding 'values'.
        """
        if isinstance(fields, str):
            fields = [fields]
            values = [values]
        elif isinstance(fields, (list, tuple)) and isinstance(values, (list, tuple)):
            if len(fields) != len(values):
                raise AttributeError('Arguments fields and values must be the same length')
        else:
            raise AttributeError('Argument fields must be one of one of: str, list, tuple')

        for model in self._fixtures[model_name]:
            if all(model['fields'][fields[i]] == values[i]
                   for i in range(len(fields))):
                return model['pk']

    def _exists(self, model_name, fields, values):
        """Check if a specific record exists.

        Arguments 'fields' and 'values' can be either strings or lists of strings.
        """
        return self._get_id(model_name, fields, values) is not None

    def _add_record(self, model_name, fields, pk=None):
        """Add a record to fixtures list."""
        self._fixtures[model_name].append({
                'model': model_name,
                'pk': self._auto_id(model_name) if pk is None else pk,
                'fields': fields
        })

    def _init_properties(self):
        for property_name in ['Size', 'Color']:
            self._add_record(self.PROPERTY, {
                'name': property_name
            })

    def _init_property_values(self):
        color_property = self._get_id(self.PROPERTY, 'name', 'Color')
        size_property = self._get_id(self.PROPERTY, 'name', 'Size')

        for item in self._data:
            color = item['color']

            if not self._exists(self.PROPERTY_VALUE, 'value', color):
                self._add_record(self.PROPERTY_VALUE, {
                    'value': color,
                    'property': color_property
                })

            for size in item['sizes']:
                if not self._exists(self.PROPERTY_VALUE, 'value', size):
                    self._add_record(self.PROPERTY_VALUE, {
                        'value': size,
                        'property': size_property
                    })