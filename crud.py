from sqlalchemy.orm import Session
import models


def get_geodata_by_street_and_number(db: Session, street_name: str, street_number: int):
    result = db.query(models.GeoData).filter(
        (models.GeoData.street_name == street_name) | (models.GeoData.street_number == street_number)).all()

    for result in result:
        return {
            'formatted_address': result.formatted_address,
            'latitude': result.latitude,
            'longitude': result.longitude,
            'place_id': result.place_id
        }


def create_geodata(db: Session, geodata: models.GeoData):
    db_geodata = models.GeoData(
        street_number=geodata.street_number,
        street_name=geodata.street_name,
        locality=geodata.locality,
        country=geodata.country,
        postal_code=geodata.postal_code,
        formatted_address=geodata.formatted_address,
        latitude=geodata.latitude,
        longitude=geodata.longitude,
        place_id=geodata.place_id
    )
    db.add(db_geodata)
    db.commit()
    db.refresh(db_geodata)
    return db_geodata
