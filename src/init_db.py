# -*- coding: utf-8 -*-

import os, logging
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Table, Column, Integer, String, Boolean, DateTime, MetaData, ForeignKey
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

logger = logging.getLogger(__name__)

engine = create_engine('sqlite:///../data/ods-slack.db', echo=True)
Base = declarative_base()

if __name__ == '__main__':
    Base.metadata.create_all(engine)
