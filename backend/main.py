from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Post, Reshare

DATABASE_URL = "sqlite:///./students_connect.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/post/")
def create_post(content: str, student_id: int, db=Depends(get_db)):
    post = Post(content=content, author_id=student_id)
    db.add(post)
    db.commit()
    db.refresh(post)
    return {"message": "Post created", "post_id": post.id}

@app.post("/reshare/")
def reshare_post(post_id: int, student_id: int, db=Depends(get_db)):
    reshare = Reshare(post_id=post_id, student_id=student_id)
    db.add(reshare)
    db.commit()
    return {"message": "Post reshared"}

@app.get("/feed/")
def get_feed(db=Depends(get_db)):
    posts = db.query(Post).all()
    reshares = db.query(Reshare).all()
    feed = []

    for post in posts:
        feed.append({"type": "post", "id": post.id, "content": post.content, "author": post.author_id})

    for reshare in reshares:
        feed.append({"type": "reshare", "post_id": reshare.post_id, "student_id": reshare.student_id})

    return {"feed": feed}


