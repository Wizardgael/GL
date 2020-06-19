from model.mapping import Base
from sqlalchemy.orm import relationship
import uuid

from sqlalchemy import Column, String, UniqueConstraint, ForeignKey, Table, Integer
from model.mapping.sport import sport_member, coach_member

class Member(Base):
    __tablename__ = 'members'
    __table_args__ = (UniqueConstraint('firstname', 'lastname'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)

    email = Column(String(256), nullable=False)
    admin = Column(Integer, nullable=False)

    sports = relationship(
        "Sport",
        secondary=sport_member,
        back_populates="members")

    coached = relationship(
        "Sport",
        secondary=coach_member,
        back_populates="coachs")

    def __repr__(self):
        return "<Member(%s %s)>" % (self.firstname, self.lastname.upper())

    def to_dict(self):
        return {
            "id": self.id,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "sports": self.get_sports(),
            "coach": self.coached.__len__() > 0,
            "coached": self.get_coached(),
            'self': self,
            "admin": self.admin > 0
        }

    def get_sports(self):
        l = []
        for sport in self.sports:
            l.append(sport.to_dict()['name'])
        return l
    
    def get_coached(self):
        l = []
        for sport in self.coached:
            l.append(sport.to_dict()['name'])
        return l
