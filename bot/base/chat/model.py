from sqlalchemy import Column, BIGINT, TEXT
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Chat(Base):
    __tablename__ = "chat"

    id = Column(BIGINT, primary_key=True,  autoincrement=True)
    chai_id = Column(BIGINT)
    lang = Column(TEXT)