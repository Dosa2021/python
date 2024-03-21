import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


Engine = create_engine(
    f"postgresql://{os.environ['TAXI_CLOUD_REDSHIFT_USER']}:{os.environ['TAXI_CLOUD_REDSHIFT_PASSWORD']}@{os.environ['TAXI_CLOUD_REDSHIFT_HOST']}:{os.environ['TAXI_CLOUD_REDSHIFT_PORT']}/{os.environ['TAXI_CLOUD_REDSHIFT_DATABASE']}",
    pool_recycle=1800)

session = Session(
  autocommit = False,
  autoflush = True,
  bind = Engine
)

Base = declarative_base()
