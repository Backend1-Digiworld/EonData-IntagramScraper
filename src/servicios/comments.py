# Libs
from datetime import datetime

# Models migrations
from src.modelos.comments import InstagramCommentModel
from src.schemas.comment import InstagramComment
from src.settings.database import conn

def getPublicationById(id):
    return conn.execute(InstagramCommentModel.select().where(InstagramCommentModel.c.ID == id)).first()

def getCommentsByPost(shortcode: str):
    list = []
    try:
        conec =  conn.execute(
            InstagramCommentModel.select().where(
                InstagramCommentModel.c.POST == shortcode
            )
        ).all()

        for comment in conec:
            list.append(comment._asdict())

    except ValueError:
        print(ValueError)
        print("ERROR: [domains.services:instagram_commnets] - Error ocurred in find comments by post")
        list = []

    return list

def updateComment(comment: InstagramComment, id: int):
    return conn.execute(
        InstagramCommentModel.update()
        .values(comment)
        .where(InstagramCommentModel.c.ID == id)
    )

def createComment(comment: InstagramComment):
    return conn.execute(InstagramCommentModel.insert().values(comment))
