from main import get_temperature
import pytest
from unittest.mock import patch


listas_de_Testes = [
        (62, -14.235004, -51.92528, 16),
]


@pytest.mark.parametrize("temperature, lat, lng, expected", listas_de_Testes)
def test_get_temperature_by_lat_lng(temperature, lat, lng, expected):
    lat = -14.235004

    lng = -51.92528

    mock_get_patcher = patch('main.requests.get')

    temperature = {
        "currently": {
            "temperature": temperature
        }
    }

    mock_get = mock_get_patcher.start()

    mock_get.return_value.json.return_value = temperature

    response = get_temperature(lat, lng)

    mock_get.stop()

    assert response == expected
