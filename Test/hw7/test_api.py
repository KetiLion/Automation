import requests
import pytest

BASE_URL = 'https://restful-booker.herokuapp.com/booking'
STATUS_OK = 200
def test_get_all_booking():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    key = 'Connection'
    assert key in response.headers

def test_get_booking_with_id():
    response = requests.get(f'{BASE_URL}/1')
    print(len(response.json()))
    response_data = response.json()
    expected_keys = ['firstname', 'lastname', 'totalprice']
    assert response_data["firstname"] == 'Susan'
    for key in expected_keys:
        assert key in response_data.keys()
    print(f'\n{response_data}')