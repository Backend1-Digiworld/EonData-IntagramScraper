from datetime import datetime, timedelta
from itertools import dropwhile, takewhile

from src.servicios.acount import getAllEnabledAcounts, setDead, setUsed, setDead, setAllActive, setAllUnused, deactiveAcount

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


def comments(post: str):
    loged = login()
    commentsE = []
    
    if loged == 'ALL ACOUNTS DEAD':
        return 'ALL ACOUNTS DEAD'
    else:
        try:
            logging.info(f'Getting comments of post: {post}')
            commentsS = instaloader.Post.from_shortcode(loged.context, post).get_comments()
            
            for comment in commentsS: 
                commentE={
                    "POST": post,
                    "TYPE": 'COMMENT FATHER',
                    "ID": comment[0],
                    "DATE": comment[1],
                    "TEXT": comment[2],
                    "OWNER_ID": comment[3].userid,
                    "OWNER_USERNAME": comment[3].username,
                    "LIKES": comment[4],
                    "date_create": datetime.utcnow()
                }
                commentsE.append(commentE)
                
                count = 1
                for answer in comment[5]:
                    answerC = {
                        "POST": post,
                        "TYPE": 'COMMENT CHILD '+str(count),
                        "ID": answer[0],
                        "DATE": answer[1],
                        "TEXT": answer[2],
                        "OWNER_ID": answer[3].userid,
                        "OWNER_USERNAME": answer[3].username,
                        "LIKES": answer[4],
                        "date_create": datetime.utcnow()
                    }
                    commentsE.append(answerC)
                    count +=1
        
        except Exception as error:
            logging.error(error)
            logging.error('COMMENTS POST '+ post)
            setDead()
            #return comments(post)
            pass
            
        return commentsE

