from sqlalchemy.orm import declarative_base, sessionmaker, declared_attr,relationship
from datetime import datetime
import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    DateTime,
    func,
)

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:password@localhost/postgres"
engine = create_async_engine(PG_CONN_URI, echo=True, )


class Base:
    # required in order to access columns with server defaults
    # or SQL expression defaults, subsequent to a flush, without
    # triggering an expired load
    __mapper_args__ = {"eager_defaults": True}

    @declared_attr
    def __tablename__(cls):
        return f"hw04_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

Base = declarative_base(bind=engine, cls=Base)

# expire_on_commit=False will prevent attributes from being expired
# after commit.
Session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


class TimestampMixin:
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )

class User(TimestampMixin, Base):

    name = Column(String(50), unique=True)
    username = Column(String(32), unique=True)
    email = Column(String(50), unique=True)
    
    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"username={self.username!r},name={self.name!r},email={self.email!r},  "
            f"created_at={self.created_at})"
        )

    def __repr__(self):
        return str(self)


class Post(TimestampMixin, Base):
    title = Column(String(120), nullable=False, default="", server_default="")
    body = Column(Text, nullable=False, default="", server_default="")
    status = Column(String(10), nullable=False, default="draft", server_default="draft")

    user_id = Column(Integer, ForeignKey("hw04_users.id"), nullable=False)
    user = relationship("User", back_populates="posts")

    
    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"title={self.title!r}, user_id={self.author_id}, "
            f"created_at={self.created_at}"
            ")"
        )

    def __repr__(self):
        return str(self)


