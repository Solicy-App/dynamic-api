from api_response import Response
from schema import Schema, And, Use
from .database.models import Users

schema = Schema({
    'id': And(Use(str)),
    'name': And(Use(str)),
    'lastLoginTime': And(Use(str)),
    'serverId': And(Use(str)),
    'level': And(Use(str)),
    'clanId': And(Use(str)),
    'clanRole': And(Use(str)),
    'avatarId': And(Use(str)),
    'isChatModerator': And(Use(bool)),
    'frameId': And(Use(int)),
    'leagueId': And(Use(int)),
    'allowPm': And(Use(str)),
    'accountId': And(Use(str)),
    'timeZone': And(Use(int)),
    'starMoney': And(Use(str)),
    'vipPoints': And(Use(str)),
    'gold': And(Use(int)),
    'flags': And(Use(str)),
    'nextDayTs': And(Use(int)),
    'nextServerDayTs': And(Use(int)),
    'experience': And(Use(str)),
    'maxLevel': And(Use(int)),
    'registrationTime': And(Use(str)),
})


def process(db, args):
    try:

        user = Users(**args)
        db.session.add(user)
        db.session.commit()

    except Exception as e:
        print(e)
        return Response(
            success=False,
            message=str(e),
            data=None
        )


    return Response(
        success=True,
        message="successfully created!",
        data=user.serialize()
    )
