from api_response import Response
from schema import Schema, And, Use

schema = Schema({
    'base': And(Use(int)),
    'exponent': And(Use(int)),
})


def process(db, args):
    return Response(success=True, message=f"{args['base']} to exponent {args['exponent']}", data=pow(args['base'], args['exponent']))
