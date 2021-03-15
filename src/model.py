import uuid
from datetime import datetime

import sqlalchemy as db
from sqlalchemy_utils import UUIDType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


metadata = db.MetaData()
Base = declarative_base(metadata=metadata)


class Model(Base):
    __tablename__ = "model"

    uuid = db.Column(UUIDType, primary_key=True, default=uuid.uuid4)

    id = db.Column(db.String, unique=True)
    last_updated = db.Column(db.DateTime,
                             default=datetime.now,
                             onupdate=datetime.now)

    params = db.Column(db.JSON)

    epoch = relationship("Epoch")


class Epoch(Base):
    __tablename__ = "epoch"
    __table_args__ = (
        db.UniqueConstraint("model_id", "number", name="unique_epoch"),
    )

    uuid = db.Column(UUIDType, primary_key=True, default=uuid.uuid4)
    model_id = db.Column(
        db.String,
        db.ForeignKey('model.id'),
    )

    created_at = db.Column(db.DateTime, default=datetime.now)

    number = db.Column(db.Integer, nullable=False)

    training_loss = db.Column(db.Float)
    eval_loss = db.Column(db.Float)

    training_F1 = db.Column(db.Float)
    eval_F1 = db.Column(db.Float)

    training_acc = db.Column(db.Float)
    eval_acc = db.Column(db.Float)
