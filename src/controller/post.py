# Libs
import json
import time
from datetime import datetime, timedelta

# Domains
from src.libs.post import posts
from src.servicios.post import createpubliacationInstagram, getPublicationByShortcode, getPublicationInstagramWeeks, updateUserInstagram, getPublicationsByInstagramUser

def saveAllPosts(username: str):
    try:
        posttoComment = []
        date = datetime.utcnow() - timedelta(days= 5)
        publicationsRaw = posts(username)
        if publicationsRaw != 'ALL ACOUNTS DEAD':
            for media in publicationsRaw:
                mediaExist = getPublicationByShortcode(media['SHORTCODE'])
                if not mediaExist:
                    createpubliacationInstagram(media)
                    posttoComment.append(media)
                else:
                    if media['date_create'] <= date:
                        if media['COMMENTS'] != mediaExist['COMMENTS']:
                            posttoComment.append(media) 
                    updateUserInstagram(media, media['SHORTCODE'],)
        return posttoComment
    except ValueError:
        print(ValueError)
        print("ERROR: [useCases:publications_twitter] - Error ocurred in find and save user post")

def getPublicationsOfUser(username):
    publications = []
    try:
        publications = getPublicationsByInstagramUser(username)
    except ValueError:
        print(ValueError)
        print("ERROR: [useCases:publications_twitter] - Error ocurred in find and save user information")
        publications = []
    return publications

def getPostWeeks(username, days):
    publications = []
    try:
        publications = getPublicationInstagramWeeks(username, days)
    except ValueError:
        print(ValueError)
        print("ERROR: [useCases:publications_twitter] - Error ocurred in find and save user information")
        publications = []
    return publications