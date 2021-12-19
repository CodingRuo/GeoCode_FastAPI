from fastapi import Depends, FastAPI
from functions import get_geodata, string_to_list
from sqlalchemy.orm import Session
import crud
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/address/{address}")
def read_address(address: str, db: Session = Depends(get_db)):

    street = string_to_list(address)
    street_name = street[0]
    street_number = int(street[1])

    db_address = crud.get_geodata_by_street_and_number(db, street_name=street_name, street_number=street_number)

    if db_address:
        return db_address

    api_map_data = get_geodata(address)

    crud.create_geodata(
        db,
        models.GeoData(
            street_number=int(api_map_data['street_number']),
            street_name=api_map_data['street_name'],
            locality=api_map_data['locality'],
            country=api_map_data['country'],
            postal_code=int(api_map_data['postal_code']),
            formatted_address=api_map_data['formatted_address'],
            latitude=float(api_map_data['latitude']),
            longitude=float(api_map_data['longitude']),
            place_id=api_map_data['place_id']
        )
    )

    return {
        'formatted_address': api_map_data['formatted_address'],
        'latitude': api_map_data['latitude'],
        'longitude': api_map_data['longitude']
    }
