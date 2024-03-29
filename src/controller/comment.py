# Libs
import json
import time
from datetime import datetime, timedelta

# Domains
from src.libs.comment import comments
from src.servicios.comments import createComment, getCommentsByPost, updateComment,  getPublicationById
from src.servicios.post import getPublicationsByInstagramUser, getPublicationInstagramDays

def saveComentsBypost(posts):
    try:
        for post in posts:
            if (int(post['COMMENTS'])>0):
                allComments = comments(post['SHORTCODE']) 

                if  allComments!= 'ALL ACOUNTS DEAD':
                    for comment in allComments:
                        commentSaved = getPublicationById(comment['ID'])
                        
                        if not commentSaved:
                            createComment(comment)
                        else:
                            updateComment(comment, comment['ID'])
    
    except ValueError:
        print(ValueError)
        print("ERROR: [useCases:publications_twitter] - Error ocurred in find and save post comments")

def saveComentsByOnePost(post):
    try:  
        allComments = comments(post) 

        if  allComments!= 'ALL ACOUNTS DEAD':
            for comment in allComments:
                commentSaved = getPublicationById(comment['ID'])
                        
                if not commentSaved:
                    createComment(comment)
                else:
                    updateComment(comment, comment['ID'])
    
    except ValueError:
        print(ValueError)
        print("ERROR: [useCases:publications_twitter] - Error ocurred in find and save post comments")
        
def saveComentsByUsername(username: str):
    posts = getPublicationsByInstagramUser(username)

    try:
        for post in posts:
            date = datetime.utcnow() - timedelta(days= 5)
            if (int(post['COMMENTS'])>0 and post['date_create'] >= date):
                commentPosts = getCommentsByPost(post['SHORTCODE'])
                if len(commentPosts) != post['COMMENTS']:
                    allComments = comments(post['SHORTCODE']) 
                    if  allComments != 'ALL ACOUNTS DEAD':
                        for comment in allComments:
                            commentSaved = getPublicationById(comment['ID'])
                            
                            if not commentSaved:
                                createComment(comment)
                            else:
                                updateComment(comment, comment['ID'])
    
    except ValueError:
        print(ValueError)
        print("ERROR: [useCases:publications_twitter] - Error ocurred in find and save post comments")

def saveComentsByDate():
    posts = getPublicationInstagramDays(30)
    try:
        for post in posts:
            date = datetime.utcnow() - timedelta(days= 5)
            if (int(post['COMMENTS'])>0 and post['date_create'] >= date):
                commentPosts = getCommentsByPost(post['SHORTCODE'])
                
                if len(commentPosts) != post['COMMENTS']:
                    allComments = comments(post['SHORTCODE']) 
                    if  allComments != 'ALL ACOUNTS DEAD':
                        for comment in allComments:
                            commentSaved = getPublicationById(comment['ID'])
                            
                            if not commentSaved:
                                createComment(comment)
                            else:
                                updateComment(comment, comment['ID'])
    
    except ValueError:
        print(ValueError)
        print("ERROR: [useCases:publications_twitter] - Error ocurred in find and save post comments")

def getCommentsofPost(post):
    publications = []
    try:
        publications = getCommentsByPost(post)
    except ValueError:
        print(ValueError)
        print("ERROR: [useCases:publications_twitter] - Error ocurred in find and save user information")
        publications = []
    return publications