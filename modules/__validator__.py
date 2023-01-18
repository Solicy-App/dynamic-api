from schema import SchemaError

from api_exception import ValidationError


def validate(schema, obj):
    try:
        schema.validate(obj)
        return True
    except SchemaError as e:
        raise ValidationError(message=e.code)
