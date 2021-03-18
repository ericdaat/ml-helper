import os
import uuid
from datetime import datetime

import numpy as np
import sqlalchemy as db
from sqlalchemy_utils import UUIDType
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src.config import DATABASE_URL


metadata = db.MetaData()
Base = declarative_base(metadata=metadata)
engine = db.create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


class Model(Base):
    __tablename__ = "model"

    uuid = db.Column(UUIDType, primary_key=True, default=uuid.uuid4)

    id = db.Column(db.String, unique=True)
    last_updated = db.Column(db.DateTime,
                             default=datetime.now,
                             onupdate=datetime.now)

    params = db.Column(db.JSON)

    epochs = relationship("Epoch")


class Epoch(Base):
    __tablename__ = "epoch"
    __table_args__ = (
        db.UniqueConstraint("model_id", "number", name="unique_epoch"),
    )

    uuid = db.Column(UUIDType, primary_key=True, default=uuid.uuid4)
    model_id = db.Column(
        db.String,
        db.ForeignKey("model.id"),
    )

    created_at = db.Column(db.DateTime, default=datetime.now)

    number = db.Column(db.Integer, nullable=False)

    training_loss = db.Column(db.Float)
    eval_loss = db.Column(db.Float)

    training_F1 = db.Column(db.Float)
    eval_F1 = db.Column(db.Float)

    training_acc = db.Column(db.Float)
    eval_acc = db.Column(db.Float)

    def __repr__(self):
        template_str = "Epoch {epoch}: "\
                       "Training Loss={train_loss:.4} "\
                       "Eval Loss={eval_loss:.4f} "\
                       "Training Accuracy={train_acc:.4f} "\
                       "Eval Accuracy={eval_acc:.4f}."

        return template_str.format(
            epoch=str(self.number).zfill(3),
            train_loss=self.training_loss or np.nan,
            eval_loss=self.eval_loss or np.nan,
            train_acc=self.training_acc or np.nan,
            eval_acc=self.eval_acc or np.nan
        )

