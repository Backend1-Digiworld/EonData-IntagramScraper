import instaloader

  
def getUserPassword(acounts):
    acountS = None
    
    for acount in acounts:
        if acount['active'] == 1 and acount['used'] == 0:
            acountS = acount
            return [acounts, acountS]
    
    if acountS == None:
        acounts = setAllUnussed(acounts)
        for acount in acounts:
            if acount['active'] == 1:
                acountS = acount
                return [acounts, acountS]
    
    if acountS == None:
        acounts = verifyAcounts(acounts)
               
    return [acounts, acountS]


def setAllUnussed(acounts):
    for acount in acounts:
        acount['used'] = 0  
    
    return acounts

def deactiveAcount(acountUsername, acounts):
    for acount in acounts:
        if acount['username'] == acountUsername:
           acount['active'] = 0 
    
    return acounts

def setUsed(acountUsername, acounts): 
    for acount in acounts:
        if acount['username'] == acountUsername:
           acount['used'] = 1 
    
    return acounts

def verifyAcounts(acounts):
    for acount in acounts:
        if acount['active'] == 0:
            try:
                L = instaloader.Instaloader()
                L.login(acount['username'], acount['password'])
                acount['active'] = 1
            
            except Exception as error:
                pass
    
    return acounts