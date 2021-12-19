import requests


def get_geodata(address: str):
    api_key = 'AIzaSyAKOMOG0QYfX_Zvf7fkZSDROOKOHnbPor4'
    params = {
        'key': api_key,
        'address': address
    }
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
    response = requests.get(base_url, params=params).json()
    response.keys()
    return refactor_map_data(response['results'])


def string_to_list(address: str):

    replaced_whitespace = address.replace(" ", ",")
    string_list = replaced_whitespace.split(",")
    filtered_list = list(filter(None, string_list))

    return filtered_list


def refactor_map_data(address: dict):

    address = address

    street_number = address[0]['address_components'][0]['long_name']
    stree_name = address[0]['address_components'][1]['long_name']
    locality = address[0]['address_components'][2]['long_name']
    country = address[0]['address_components'][5]['long_name']
    postal_code = address[0]['address_components'][6]['long_name']

    formatted_address = address[0]['formatted_address']
    latitude = address[0]['geometry']['location']['lat']
    longitude = address[0]['geometry']['location']['lng']
    place_id = address[0]['place_id']

    return {
        'street_number': street_number,
        'street_name': stree_name,
        'locality': locality,
        'country': country,
        'postal_code': postal_code,
        'formatted_address': formatted_address,
        'latitude': latitude,
        'longitude': longitude,
        'place_id': place_id
    }
