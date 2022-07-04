from sqlalchemy import Column, BIGINT, Text, VARCHAR, Integer, String, Sequence
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Dick_player(Base):
    __tablename__ = "dick_game"

    id = Column(BIGINT, primary_key=True,  autoincrement=True)
    key = Column(Text)
    size = Column(BIGINT)
    name = Column(Text)
    time = Column(BIGINT)
    chat_id = Column(BIGINT)
    tlgr_id = Column(BIGINT)









