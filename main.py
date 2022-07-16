from ast import Try
from datetime import datetime
import logging
from time import sleep
from random import randint
from xml.etree.ElementTree import Comment
import typer
import openpyxl

import controller as con

app = typer.Typer()

logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)


@app.command()
def get_allAboutUser():
    username = 'minuto30'
    acounts = [
    {'username': 'juancamilomastinez', 'password': 'Juancamar05', 'active': 1, 'used': 0},
    {'username': 'fopusimilazici', 'password': 'Chupameestepenco', 'active': 1, 'used': 0},
    {'username': 'monicaperez6500', 'password': 'MonicaPerez01', 'active': 1, 'used': 0},
    {'username': 'alejandro_diomedes_gomez', 'password': 'Diomedes2000', 'active': 1, 'used': 0},
    {'username': 'tellezalberto309', 'password': '*12345678*', 'active': 1, 'used': 0},
    {'username': 'luisdaniel11123', 'password': 'Test111.', 'active': 1, 'used': 0},
    {'username': 'maturanadaniela255', 'password': 'Test111.', 'active': 1, 'used': 0},
    {'username': 'dortiz334455', 'password': 'Test111.', 'active': 1, 'used': 0},
    {'username': 'elmarmaria192', 'password': 'Maria123*', 'active': 1, 'used': 0},
    {'username': 'lucimurcia199', 'password': 'Lucimurcia123*', 'active': 1, 'used': 0},
    {'username': 'macarbajala', 'password': 'MaesCar123*', 'active': 1, 'used': 0}
     ]
    
    logging.info(f'getting perfil from {username}')
    wb = openpyxl.Workbook()
    perfil = con.perfil(username, wb, acounts)
    wb = perfil[0]
    acounts = perfil[1]
    
    if acounts != None:
        logging.info(f'getting posts from {username}')
        post = con.posts(username, wb, acounts)
        wb = post[0]
        posts = post[1]
        acounts = post[2]
        
        if acounts != None:
            commentsE = wb.create_sheet('COMMENTS '+username)
            commentsE.append(('POST', 'TYPE', 'ID', 'DATE', 'TEXT', 'OWNER ID',  'OWNER USERNAME', 'LIKES'))
            for postS in posts:
                logging.info(f'getting comments from {username} post {postS[0]}')
                comment = con.comments(username, wb, postS[0], acounts)
                wb = comment[0]
                acounts = comment[1]
                if acounts != None:
                    break
                sleep(30)
    
    wb.save('./EXCELS/'+username+'.xlsx')


if __name__ == "__main__":
    app()
