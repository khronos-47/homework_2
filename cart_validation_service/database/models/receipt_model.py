from sqlalchemy import Column, ForeignKey, Integer, MetaData, Numeric, String, Text, UniqueConstraint, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from cart_validation_service.database.models.user_model import UserAccount

Base = declarative_base()
metadata = MetaData()

class Receipt(Base):
    __tablename__ = "receipt"
    metadata,
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user_account.id"))
    item_id = Column(Integer, ForeignKey("receipt_item.id"))

    #user = relationship("UserAccount", back_populates="receipts")
    #item = relationship("ReceiptItem")

    __table_args__ = (UniqueConstraint("user_id", "item_id", name="_user_item_uc"),)

    
