# Libs
from datetime import datetime

# Models migrations
from src.modelos.sessions import InstagramAcountModel
from src.schemas.session import InstagramAcount
from src.settings.database import conn

def getAllEnabledAcounts():
    list = []
    try:
        connect = conn.execute(InstagramAcountModel.select().where(InstagramAcountModel.c.available == True, InstagramAcountModel.c.is_used == False, InstagramAcountModel.c.is_dead == False)
                               .order_by(InstagramAcountModel.c.last_use.desc())).all()
        for user in connect:
            list.append(user._asdict())

    except ValueError:
        print(ValueError)
        print("ERROR: [domains.services:acounts] - Error ocurred in get list active acounts")
        list = []

    return list

def getAllAcounts():
    list =[]
    try:
        connect = conn.execute(InstagramAcountModel.select()).all()
        for user in connect:
            list.append(user._asdict())

    except ValueError:
        print(ValueError)
        print("ERROR: [domains.services:acounts] - Error ocurred in get list active acounts")
        list = []

    return list

def setUsed(acount: InstagramAcount, acountId: int):
    acount['is_used'] = True
    acount['last_use'] = datetime.utcnow()
    
    conn.execute(
        InstagramAcountModel.update()
        .values(acount)
        .where(InstagramAcountModel.c.id == acountId))
    
def deactiveAcount(acount: InstagramAcount, acountId: int):
    acount['available'] = False
    acount['last_use'] = datetime.utcnow()
    
    return conn.execute(
        InstagramAcountModel.update()
        .values(acount)
        .where(InstagramAcountModel.c.id == acountId)
    )

def setDead():
    connect = conn.execute(InstagramAcountModel.select().order_by(InstagramAcountModel.c.last_use.desc())).first()
    acount = connect._asdict()
    acount['is_dead'] = True
    acount['last_use'] = datetime.utcnow()
    acountId = acount.pop('id')
    
    return conn.execute(
        InstagramAcountModel.update()
        .values(acount)
        .where(InstagramAcountModel.c.id == int(acountId))
    )
    
def setAllUnused():
    acounts = getAllAcounts()
    
    for acount in acounts:
        if acount['is_used']:
           acount['is_used'] = False
        acountId = acount['id']
        acount.pop('id')
        conn.execute(
        InstagramAcountModel.update()
        .values(acount)
        .where(InstagramAcountModel.c.id == acountId))
        
def setAllActive():
    acounts = getAllAcounts()
    
    for acount in acounts:
        if not acount['available']:
           acount['available'] = True
        acountId = acount['id']
        acount.pop('id')
        conn.execute(
        InstagramAcountModel.update()
        .values(acount)
        .where(InstagramAcountModel.c.id == acountId))