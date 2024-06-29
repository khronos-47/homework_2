from sqlalchemy import Column, ForeignKey, Integer, MetaData, Numeric, String, Text, UniqueConstraint, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()
metadata = MetaData()

class UserAccount(Base):
    __tablename__ = "user_account"
    metadata,
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(Text, nullable=False)
    phone = Column(Text, unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)

    #receipts = relationship("Receipt", back_populates="user")

class DoctorAccount(Base):
    __tablename__ = "doctor_account"
    metadata,
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(Text, nullable=False)
    phone = Column(Text, unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    specialty_id = Column(Integer, ForeignKey("specialty.id"))

    #specialty = relationship("Specialty", back_populates="doctors")

