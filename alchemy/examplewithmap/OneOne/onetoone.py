from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint

class Base(DeclarativeBase):
    pass

class Parent(Base):
    __tablename__ = "parent_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    child: Mapped["Child"] = relationship(back_populates="parent", uselist=False)


class Child(Base):
    __tablename__ = "child_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
    parent: Mapped["Parent"] = relationship(back_populates="child", single_parent=True)
    __table_args__ = (UniqueConstraint("parent_id"),)
    
engine = create_engine('postgresql://postgres:roop@localhost/mydb1') #, echo=True)

Base.metadata.create_all(engine)
