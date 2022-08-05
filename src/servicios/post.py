# Libs
from datetime import datetime

# Models migrations
from src.modelos.posts import InstagramPublicationsModel
from src.schemas.post import InstagramPublications
from src.settings.database import conn

def getPublicationByShortcode(id):
    return conn.execute(InstagramPublicationsModel.select().where(InstagramPublicationsModel.c.SHORTCODE == id)).first()

def getPublicationInstagramDays(days: int):
    list = []
    try:
        current_time = datetime.datetime.utcnow()
        timeago = current_time - datetime.timedelta(days=days)
        print(timeago)
        conec =  conn.execute(
            InstagramPublicationsModel.select().where(
                InstagramPublicationsModel.c.LOCAL_DATE > timeago
            )
        ).all()

        for publication in conec:
            list.append(publication._asdict())

    except ValueError:
        print(ValueError)
        print("ERROR: [domains.services:instagram_publications] - Error ocurred in find publications of user information")
        list = []

    return list

def updateUserInstagram(publication: InstagramPublications, short_code: str):
    return conn.execute(
        InstagramPublicationsModel.update()
        .values(publication)
        .where(InstagramPublicationsModel.c.SHORTCODE == short_code)
    )

def createpubliacationInstagram(publication: InstagramPublications):
    return conn.execute(InstagramPublicationsModel.insert().values(publication))

def getPublicationsByInstagramUser(username: str):
    list = []
    try:
        consult = None
        consult = InstagramPublicationsModel.select().where(
          InstagramPublicationsModel.c.OWNER_USERNAME == username   
        )
            
        conec =  conn.execute(
            consult
        ).all()

        for publication in conec:
            list.append(publication._asdict())

    except ValueError:
        print(ValueError)
        print("ERROR: [domains.services:publications_Instagram] - Error ocurred in find publications of user information")
        list = []

    return list