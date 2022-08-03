from datetime import datetime

from src.controller.post import saveAllPosts
from src.controller.profile import saveProfile
from src.controller.comment import saveComentsBypost, saveComentsByOnePost, saveComentsByUsername

import typer

app = typer.Typer()

@app.command()
def get_all(username: str):
    saveProfile(username)
    posts = saveAllPosts(username)
    saveComentsBypost(posts)
    
@app.command()
def get_profile(username: str):
    saveProfile(username)

@app.command()
def get_post(username: str):
    saveProfile(username)
    saveAllPosts(username)

@app.command()
def get_comments(post: str):
    saveComentsByOnePost(post)

@app.command()
def get_commentsByUsername(username: str):
    saveComentsByUsername(username)

@app.command()
def get_post_commets(username: str):
    posts = saveAllPosts(username)
    saveComentsBypost(posts)

if __name__ == "__main__":
    app()
