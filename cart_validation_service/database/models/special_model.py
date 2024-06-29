from sqlalchemy import Column, ForeignKey, Integer, MetaData, Numeric, String, Text, UniqueConstraint, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()
metadata = MetaData()


class Specialty(Base):
    __tablename__ = "specialty"
    metadata,
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, unique=True, nullable=False)

    #doctors = relationship("DoctorAccount", back_populates="specialty")
    #special_items = relationship("SpecialItem", back_populates="specialty")
