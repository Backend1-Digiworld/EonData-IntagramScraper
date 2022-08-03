from datetime import datetime, timedelta
from itertools import dropwhile, takewhile

from src.servicios.acount import getAllEnabledAcounts, setUsed, setDead, setAllActive, setAllUnused, deactiveAcount


import instaloader
import logging

logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

def login():
    acounts = getAllEnabledAcounts()
    
    if len(acounts) == 0:
        setAllUnused()

    acounts = getAllEnabledAcounts()
    
    if len(acounts)==0:
        setAllActive()
    
    acounts = getAllEnabledAcounts()
    
    if len(acounts) == 0:
        L = 'ALL ACOUNTS DEAD'
        logging.info(f'ALL ACOUNTS DEAD')
        return L
    else:
        for acount in acounts:
            username = acount['username']
            password = acount ['password']
            acountId = int(acount['id'])
            acount.pop('id')
            
            logging.info(f'Loging with acount username: {username} password: {password}')
            try:
                L = instaloader.Instaloader()
                L.login(username, password)
                setUsed(acount, acountId)
                return L
        
            except Exception as error:
                logging.error(error)
                logging.error(username)
                setUsed(acount, acountId)
                deactiveAcount(acount, acountId)
                return login()

def posts(username: str):
    loged = login()
    
    if loged == 'ALL ACOUNTS DEAD':
        return 'ALL ACOUNTS DEAD'
    else:
        postsSave = []
        logging.info(f'getting posts from {username}')
        try:
            postsS = instaloader.Profile.from_username(loged.context, username).get_posts()
            
            SINCE = datetime.utcnow()
            UNTIL = SINCE - timedelta(days= 30)
            
            for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, postsS)):
                caption_hashtags = ''
                for capHas in post.caption_hashtags:
                    caption_hashtags = caption_hashtags+' '+capHas 
                
                caption_mentions = ''
                for capMen in post.caption_mentions:
                    caption_mentions = caption_mentions+' '+capMen 
                
                tagged_users = ''
                for tagUs in post.tagged_users:
                    tagged_users = tagged_users+' '+tagUs 
                
                postUser = {
                    'SHORTCODE': post.shortcode,
                    'TITLE': post.title,
                    'OWNER_USERNAME': post.owner_username,
                    'OWNER_ID': int(post.owner_id),
                    'LOCAL_DATE': post.date_local,
                    'CAPTION': post.caption,
                    'CAPTION_HASHTAGS': caption_hashtags,
                    'CAPTIONS_MENTIONS': caption_mentions,
                    'URL': post.url,
                    'TYPENAME': post.typename,
                    'TAGGED_USERS': tagged_users,
                    'VIDEO_URL': post.video_url,
                    'VIDEO_VIEW_COUNT': post.video_view_count,
                    'VIDEO_DURATION': post.video_duration,
                    'LIKES': post.likes,
                    'COMMENTS': post.comments,
                    'date_create': datetime.utcnow()
                }
                
                postsSave.append(postUser)
            
            return postsSave
        
        except Exception as error:
            logging.error(error)
            logging.error(username)
            setDead()
            return posts(username)