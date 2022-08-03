import instaloader
import logging

from src.servicios.acount import getAllEnabledAcounts, setUsed, setDead, setAllActive, setAllUnused, deactiveAcount

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

def perfil(username: str):
    loged = login()
    profile = None
    if loged == 'ALL ACOUNTS DEAD':
        profile =  'ALL ACOUNTS DEAD' 
    else: 
        logging.info(f'getting perfil from {username}')
        try:
            profile = instaloader.Profile.from_username(loged.context, username)
        
        except Exception as error:
            logging.error(error)
            logging.error(username)
            setDead()
            perfil(username)
        
    return profile