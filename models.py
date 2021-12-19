from sqlalchemy import Column, Integer, String, Float
from database import Base


class GeoData(Base):
    __tablename__ = "tbl_geodata"

    id = Column(Integer, primary_key=True, index=True)

    street_number = Column(Integer)
    street_name = Column(String)
    locality = Column(String)
    country = Column(String)
    postal_code = Column(Integer)

    formatted_address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    place_id = Column(String, unique=True, index=True)
