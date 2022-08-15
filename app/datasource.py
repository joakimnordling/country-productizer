from typing import Any, Dict

data = {
    "FI": {
        "code": "FI",
        "name": "Finland",
        "capital": {
            "name": "Helsinki",
            "lat": 60.170833,
            "lon": 24.9375,
        },
        "languages": ["fi", "sv"],
        "area": 338455,
    },
    "NR": {
        "code": "NR",
        "name": "Nauru",
        "capital": None,
        "languages": ["na", "en"],
        "area": 21,
    },
}


async def get_data(country: str) -> Dict[str, Any]:
    """
    Get the country data.

    This would in practice fetch the data from your underlying data source,
    such as a database, sensor or another API.

    :param country: Two-letter country code.
    :return: The data for the country.
    :raise KeyError: If no data is found for the country.
    """
    return data[country.upper()]
