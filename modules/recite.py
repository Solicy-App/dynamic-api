from api_response import Response
from schema import Schema, And, Use

schema = Schema({
    'message': And(Use(str)),
})


def process(db, args):
    return Response(success=True, message=args['message'], data=None, status=200)
