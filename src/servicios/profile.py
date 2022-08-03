# Libs
from datetime import datetime

# Models migrations
from src.modelos.accounts import InstagramUserModel
from src.schemas.profile import InstagramUser
from src.settings.database import conn

def getAllUsersEnable():
    list = []
    try:
        connect = conn.execute(InstagramUserModel.select().where(InstagramUserModel.c.is_active == True)).all()
        for user in connect:
            list.append(user._asdict())

    except ValueError:
        print(ValueError)
        print("ERROR: [domains.services:users] - Error ocurred in find users enabled")
        list = []

    return list
    
def getUserByInstagramId(id):
    return conn.execute(InstagramUserModel.select().where(InstagramUserModel.c.id == id)).first()

def getUserByInstagramName(name: str):
    user = {}
    try:
        connect = conn.execute(InstagramUserModel.select().where(InstagramUserModel.c.username == name)).first()
        user = connect._asdict()
    except Exception as error:
        user = {}
    return user

def createUserInstagram(user: InstagramUser):
    return conn.execute(InstagramUserModel.insert().values(user))

def updateUserInstagram(user: InstagramUser, InstagramId):
    try:
        conn.execute(InstagramUserModel.update().values(user).where(InstagramUserModel.c.id == InstagramId))
        
    except Exception as error:
        pass
    
def getAllInstagramUsers():
    list = []
    try:
        connect = conn.execute(InstagramUserModel.select()).all()
        for user in connect:
            list.append(user._asdict())

    except ValueError:
        print(ValueError)
        print("ERROR: [domains.services:InstagramUser] - Error ocurred in find InstagramUser enabled")
        list = []

    return list