# Libs
import json
import time
from datetime import datetime

# Domains
from src.libs.perfil import perfil
from src.servicios.profile import createUserInstagram, updateUserInstagram, getUserByInstagramName, getAllInstagramUsers

def saveProfile(username: str):
    userToSave = {}
    try:
        userInfo = perfil(username)
        if userInfo != None:
            userFinder = getUserByInstagramName(username)
            if not userFinder:
                userToSave = {
                    "id": userInfo.userid,
                    "username": userInfo.username,
                    "full_name": userInfo.full_name,
                    "biography": userInfo.biography,
                    "profile_pic_url": userInfo.profile_pic_url,
                    "external_url": userInfo.external_url,
                    "media_count": userInfo.mediacount,
                    "followed_by_count": userInfo.followees,
                    "follows_count": userInfo.followers,
                    "is_private": userInfo.is_private,
                    "is_verified": userInfo.is_verified,
                    'date_create': datetime.utcnow()
                }
                createUserInstagram(userToSave)
            else:
                userToSave = {
                    "id": str(userInfo.userid),
                    "username": userInfo.username,
                    "full_name": userInfo.full_name,
                    "biography": userInfo.biography,
                    "profile_pic_url": userInfo.profile_pic_url,
                    "external_url": userInfo.external_url,
                    "media_count": userInfo.mediacount,
                    "followed_by_count": userInfo.followees,
                    "follows_count": userInfo.followers,
                    "is_private": userInfo.is_private,
                    "is_verified": userInfo.is_verified,
                    "url": 'https://www.instagram.com/'+username,
                    'date_create': datetime.utcnow()
                }
                updateUserInstagram(userToSave, str(userInfo.userid))
        else:
            userToSave = {}  
    except ValueError:
        print(ValueError)
        print("ERROR: [useCases:users] - Error ocurred in find and save user information")
        userToSave = {}
    return userToSave

def getInfoOfUser(username: str):
    userFinder = {}
    try:
        userFinder = getUserByInstagramName(username)
    except ValueError:
        print(ValueError)
        print("ERROR: [useCases:users] - Error ocurred in find and save user information")
        userFinder = {}
    return userFinder

def getUsersList():
    userList = []
    try:
        userList = getAllInstagramUsers()
    except ValueError:
        print(ValueError)
        print("ERROR: [useCases:users] - Error ocurred in find users list")
        userList = []
    return userList