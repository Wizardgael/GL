from model.mapping import Base
from sqlalchemy.orm import relationship
import uuid

from sqlalchemy import Column, String, UniqueConstraint, ForeignKey, Table
from model.mapping.sport import association_table

class Member(Base):
    __tablename__ = 'members'
    __table_args__ = (UniqueConstraint('firstname', 'lastname'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)

    email = Column(String(256), nullable=False)

    sports = relationship(
        "Sport",
        secondary=association_table,
        back_populates="members")

    def __repr__(self):
        return "<Member(%s %s)>" % (self.firstname, self.lastname.upper())

    def to_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "sports": self.get_sports()
        }

    def get_sports(self):
        l = []
        for sport in self.sports:
            l.append(sport.to_dict()['name'])
        return l