from sqlalchemy import create_engine, Column, Integer, String, Numeric, ForeignKey, Text, UniqueConstraint,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()
metadata = MetaData()
class Specialty(Base):
    __tablename__ = 'specialty'
    metadata,
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, unique=True, nullable=False)

    doctors = relationship('DoctorAccount', back_populates='specialty')
    special_items = relationship('SpecialItem', back_populates='specialty')

class CommonItem(Base):
    __tablename__ = 'common_item'
    metadata,
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    amount = Column(Integer, nullable=False)
    price = Column(Numeric(8, 2), nullable=False)
    dosage_form = Column(Text, nullable=False)
    manufacturer = Column(Text, nullable=False)
    barcode = Column(Text, unique=True, nullable=False)
    
    def __repr__(self):
        columns = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return f'<{self.__tablename__}: {", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'

class SpecialItem(Base):
    __tablename__ = 'special_item'
    metadata,
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    amount = Column(Integer, nullable=False)
    price = Column(Numeric(8, 2), nullable=False)
    dosage_form = Column(Text, nullable=False)
    manufacturer = Column(Text, nullable=False)
    barcode = Column(Text, unique=True, nullable=False)
    specialty_id = Column(Integer, ForeignKey('specialty.id'))

    specialty = relationship('Specialty', back_populates='special_items')

class ReceiptItem(Base):
    __tablename__ = 'receipt_item'
    metadata,
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    amount = Column(Integer, nullable=False)
    price = Column(Numeric(8, 2), nullable=False)
    dosage_form = Column(Text, nullable=False)
    manufacturer = Column(Text, nullable=False)
    barcode = Column(Text, unique=True, nullable=False)

class UserAccount(Base):
    __tablename__ = 'user_account'
    metadata,
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(Text, nullable=False)
    phone = Column(Text, unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)

    receipts = relationship('Receipt', back_populates='user')

class DoctorAccount(Base):
    __tablename__ = 'doctor_account'
    metadata,
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(Text, nullable=False)
    phone = Column(Text, unique=True, nullable=False)
    password_hash = Column(Text, nullable=False)
    specialty_id = Column(Integer, ForeignKey('specialty.id'))

    specialty = relationship('Specialty', back_populates='doctors')
    def __repr__(self):
        columns = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return f'<{self.__tablename__}: {", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'

class Receipt(Base):
    __tablename__ = 'receipt'
    metadata,
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user_account.id'))
    item_id = Column(Integer, ForeignKey('receipt_item.id'))

    user = relationship('UserAccount', back_populates='receipts')
    item = relationship('ReceiptItem')

    __table_args__ = (UniqueConstraint('user_id', 'item_id', name='_user_item_uc'),)

    def __repr__(self):
        columns = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return f'<{self.__tablename__}: {", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'