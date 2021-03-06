"""
owtf.models.config
~~~~~~~~~~~~~~~~~~

"""
from sqlalchemy import Boolean, Column, String

from owtf.db.model_base import Model


class Config(Model):
    __tablename__ = "configuration"

    key = Column(String, primary_key=True)
    value = Column(String)
    section = Column(String)
    descrip = Column(String, nullable=True)
    dirty = Column(Boolean, default=False)

    def to_dict(self):
        config_dict = dict(self.__dict__)
        config_dict.pop("_sa_instance_state")
        return config_dict

    def __repr__(self):
        return "<Config (key='{!s}', value='{!s}', dirty='{!r}')>".format(self.key, self.value, self.dirty)
