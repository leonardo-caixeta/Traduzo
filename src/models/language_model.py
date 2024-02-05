from models.abstract_model import AbstractModel
from database.db import db
from os import environ


class LanguageModel(AbstractModel):
    _collection = db[environ.get("DB_NAME")]

    def __init__(self, data: dict):
        super().__init__(data)

    def to_dict(self) -> dict:
        return {
            "name": self.data.get("name"),
            "acronym": self.data.get("acronym"),
            }
