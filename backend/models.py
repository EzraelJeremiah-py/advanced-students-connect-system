from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    author_id = Column(Integer, ForeignKey("students.id"))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

class Reshare(Base):
    __tablename__ = "reshares"
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    student_id = Column(Integer, ForeignKey("students.id"))

