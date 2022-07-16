from datetime import datetime, timedelta
from itertools import dropwhile, takewhile



from servicios.acount import getUserPassword, deactiveAcount, setUsed, verifyAcounts

import instaloader
import logging
logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

def login(acounts):
    acountInfo = getUserPassword(acounts)
    
    acount = acountInfo[1]
    acounts = acountInfo[0]
    
    username = acount['username']
    password = acount ['password']
    
    try:
        L = instaloader.Instaloader()
        L.login(username, password)
        acounts = setUsed(username, acounts)
        return [L, acounts]
    
    except Exception as error:
        logging.error(error)
        logging.error(username)
        acounts = deactiveAcount(username, acounts)
        return login(acounts)
        
    
    

def perfil(username: str, wb, acounts):
    loginP = login(acounts)
    acounts = loginP[1]
    L = loginP[0]
    
    perfil = wb.create_sheet('PERFIL '+username)
    
    user = instaloader.Profile.from_username(L.context, username)
    
    perfilUser = (
        user.userid,
        user.username, 
        user.full_name, 
        user.profile_pic_url,
        user.biography,
        user.external_url,
        user.followers,
        user.followees,
        user.mediacount,
        user.is_private,
        user.is_verified,
        user.is_business_account
        )
    
    perfil.append(('ID','USERNAME', 'FULL NAME', 'PROFILE PIC URL', 'BIOGRAPHY', 'EXTERNAL URL', 'FOLLOWERS', 'FOLLOWEES',
                    'MEDIACOUNT', 'IS PRIVATE', 'IS VERIFIED', 'IS BUSINESS ACOUNT' ))
    
    perfil.append(perfilUser)
    
    return [wb, acounts]

def posts(username: str, wb, acounts):
    loginP = login(acounts)
    acounts = loginP[1]
    L = loginP[0]
    
    postsE = wb.create_sheet('POSTS '+username)
    
    posts = instaloader.Profile.from_username(L.context, username).get_posts()
    
    
    SINCE = datetime.now()
    UNTIL = SINCE - timedelta(days= 30)
    
    postsExcel = []
    
    for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
        caption_hashtags = ''
        for capHas in post.caption_hashtags:
            caption_hashtags = caption_hashtags+' '+capHas 
        
        caption_mentions = ''
        for capMen in post.caption_mentions:
            caption_mentions = caption_mentions+' '+capMen 
        
        tagged_users = ''
        for tagUs in post.tagged_users:
            tagged_users = tagged_users+' '+tagUs 
        
        postUser = (
            post.shortcode,
            str(post.title),
            post.owner_username,
            post.owner_id,
            str(post.date_local),
            post.caption,
            caption_hashtags,
            caption_mentions,
            post.url,
            post.typename,
            tagged_users,
            str(post.video_url),
            post.video_view_count,
            post.video_duration,
            post.likes,
            post.comments
        )
        
        postsExcel.append(postUser)
    
    postsE.append(('SHORTCODE', 'TITLE', 'OWNER USERNAME', 'OWNER ID', 'LOCAL DATE', 'CAPTION',
                   'CAPTION HASHTAGS', 'CAPTIONS MENTIONS', 'URL', 'TYPENAME', 'TAGGED_USERS',
                   'VIDEO URL', 'VIDEO VIEW COUNT', 'VIDEO DURATION', 'LIKES', 'COMMENTS'))
    
    for postE in postsExcel:
        postsE.append(postE)
    
    return [wb, postsExcel, acounts]
    
def comments(username: str, wb, post, acounts):
    loginP = login(acounts)
    acounts = loginP[1]
    L = loginP[0]
    
    commentsE = wb['COMMENTS '+username]
    
    comments = instaloader.Post.from_shortcode(L.context, post).get_comments()
    
    for comment in comments: 
        commentE=(
            post,
            'COMMENT FATHER',
            comment[0],
            comment[1],
            comment[2],
            comment[3].userid,
            comment[3].username,
            comment[4]
        )
        commentsE.append(commentE)
        
        count = 1
        for answer in comment[5]:
            answerC = (
                post,
                'COMMENT CHILD '+str(count),
                answer[0],
                answer[1],
                comment[2],
                comment[3].userid,
                comment[3].username,
                comment[4]
            )
            commentsE.append(answerC)
            count +=1
        
    return [wb, acounts]
        
        
    