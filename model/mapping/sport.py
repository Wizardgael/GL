from model.mapping import Base
from sqlalchemy.orm import relationship
import uuid

from sqlalchemy import Column, String, UniqueConstraint, ForeignKey, Table

sport_member = Table('sport_member', Base.metadata,
                            Column('member_id', String, ForeignKey("members.id")),
                            Column('sports_id', String, ForeignKey("sports.id"))
)

coach_member = Table('coach_member', Base.metadata,
                            Column('member_id', String, ForeignKey("members.id")),
                            Column('sports_id', String, ForeignKey("sports.id"))
)

class Sport(Base):
    __tablename__ = 'sports'
    __table_args__ = (UniqueConstraint('name'),)

    id = Column(String(36), default=str(uuid.uuid4()), primary_key=True)

    name = Column(String(50), nullable=False)

    description = Column(String(256), nullable=False)

    members = relationship(
        "Member",
        secondary=sport_member,
        back_populates="sports")
    
    coachs = relationship(
        "Member",
        secondary=coach_member,
        back_populates="coached")

    def __repr__(self):
        return "<Sport(%s %s)>" % (self.name, self.description)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "self": self
        }
