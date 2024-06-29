from sqlalchemy import Column, ForeignKey, Integer, MetaData, Numeric, String, Text, UniqueConstraint, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


Base = declarative_base()
metadata = MetaData()

class CommonItem(Base):
    __tablename__ = "common_item"
    metadata,
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    amount = Column(Integer, nullable=False)
    price = Column(Numeric(8, 2), nullable=False)
    dosage_form = Column(Text, nullable=False)
    manufacturer = Column(Text, nullable=False)
    barcode = Column(Text, unique=True, nullable=False)


class ReceiptItem(Base):
    __tablename__ = "receipt_item"
    metadata,
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    amount = Column(Integer, nullable=False)
    price = Column(Numeric(8, 2), nullable=False)
    dosage_form = Column(Text, nullable=False)
    manufacturer = Column(Text, nullable=False)
    barcode = Column(Text, unique=True, nullable=False)

class SpecialItem(Base):
    __tablename__ = "special_item"
    metadata,
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    amount = Column(Integer, nullable=False)
    price = Column(Numeric(8, 2), nullable=False)
    dosage_form = Column(Text, nullable=False)
    manufacturer = Column(Text, nullable=False)
    barcode = Column(Text, unique=True, nullable=False)
    specialty_id = Column(Integer, ForeignKey("specialty.id"))

    #specialty = relationship("Specialty", back_populates="special_items")