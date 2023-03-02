from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    lastLoginTime = db.Column(db.String(20), nullable=False)
    serverId = db.Column(db.String(20), nullable=False)
    level = db.Column(db.String(20), nullable=False)
    clanId = db.Column(db.String(20), nullable=False)
    clanRole = db.Column(db.String(20), nullable=False)
    avatarId = db.Column(db.String(20), nullable=False)
    isChatModerator = db.Column(db.Boolean, nullable=False)
    frameId = db.Column(db.Integer, nullable=False)
    leagueId = db.Column(db.Integer, nullable=False)
    allowPm = db.Column(db.String(20), nullable=False)
    accountId = db.Column(db.String(20), nullable=False)
    timeZone = db.Column(db.Integer, nullable=False)
    starMoney = db.Column(db.String(20), nullable=False)
    vipPoints = db.Column(db.String(20), nullable=False)
    gold = db.Column(db.Integer, nullable=False)
    flags = db.Column(db.String(20), nullable=False)
    nextDayTs = db.Column(db.Integer, nullable=False)
    nextServerDayTs = db.Column(db.Integer, nullable=False)
    experience = db.Column(db.String(20), nullable=False)
    maxLevel = db.Column(db.String(20), nullable=False)
    registrationTime = db.Column(db.String(20), nullable=False)

    def __init__(self, id, name, lastLoginTime, serverId, level, clanId, clanRole, avatarId, isChatModerator,
                 frameId, leagueId, allowPm, accountId, timeZone, starMoney, vipPoints, gold, flags,
                 nextDayTs, nextServerDayTs, experience, maxLevel, registrationTime):
        self.id = id
        self.name = name
        self.lastLoginTime = lastLoginTime
        self.serverId = serverId
        self.level = level
        self.clanId = clanId
        self.clanRole = clanRole
        self.avatarId = avatarId
        self.isChatModerator = isChatModerator
        self.frameId = frameId
        self.leagueId = leagueId
        self.allowPm = allowPm
        self.accountId = accountId
        self.timeZone = timeZone
        self.starMoney = starMoney
        self.vipPoints = vipPoints
        self.gold = gold
        self.flags = flags
        self.nextDayTs = nextDayTs
        self.nextServerDayTs = nextServerDayTs
        self.experience = experience
        self.maxLevel = maxLevel
        self.registrationTime = registrationTime

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastLoginTime": self.lastLoginTime,
            "serverId": self.serverId,
            "level": self.level,
            "clanId": self.clanId,
            "clanRole": self.clanRole,
            "avatarId": self.avatarId,
            "isChatModerator": self.isChatModerator,
            "frameId": self.frameId,
            "leagueId": self.leagueId,
            "allowPm": self.allowPm,
            "accountId": self.accountId,
            "timeZone": self.timeZone,
            "starMoney": self.starMoney,
            "vipPoints": self.vipPoints,
            "gold": self.gold,
            "flags": self.flags,
            "nextDayTs": self.nextDayTs,
            "nextServerDayTs": self.nextServerDayTs,
            "experience": self.experience,
            "maxLevel": self.maxLevel,
            "registrationTime": self.registrationTime,
        }

