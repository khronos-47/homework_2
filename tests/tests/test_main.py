import pytest
from fastapi.testclient import TestClient
from cart_validation_service.app import app

client = TestClient(app)


def test_check_cart_valid_common_item():
    response = client.get("/check?user_id=12&item_id=common_25")
    assert response.status_code == 200
    assert response.json() == []

def test_check_cart_invalid_category():
    response = client.get("/check?user_id=123&item_id=invalid_25")
    assert response.status_code == 200
    assert response.json() == [{"item_id": "invalid_25", "problem": "WRONG_CATEGORY"}]

def test_check_cart_invalid_item_id():
    response = client.get("/check?user_id=123&item_id=common_abc")
    assert response.status_code == 200
    assert response.json() == [{"item_id": "common_abc", "problem": "INCORRECT_ITEM_ID"}]

def test_check_cart_item_not_found():
    response = client.get("/check?user_id=12&item_id=common_199")
    assert response.status_code == 200
    assert response.json() == [{"item_id": "common_199", "problem": "ITEM_NOT_FOUND"}]

def test_check_cart_no_user_no_receipt():
    response = client.get("/check?user_id=999&item_id=receipt_27")
    assert response.status_code == 200
    assert response.json() == [{"item_id": "receipt_27", "problem": "NO_USER_NO_RECEIPT"}]

def test_check_cart_no_user_special_item():
    response = client.get("/check?user_id=999&item_id=special_26")
    assert response.status_code == 200
    assert response.json() == [{"item_id": "special_26", "problem": "NO_USER_SPECIAL_ITEM"}]

def test_check_cart_no_user_common_item():
    response = client.get("/check?user_id=999&item_id=common_25")
    assert response.status_code == 200
    assert response.json() == [{"item_id": "common_25", "problem": "NO_USER"}]

def test_check_cart_special_wrong_spec():
    response = client.get("/check?user_id=61&item_id=special_26")
    assert response.status_code == 200
    assert response.json() == [{"item_id": "special_26", "problem": "ITEM_SPECIAL_WRONG_SPECIFIC"}]

def test_check_cart_no_receipt():
    response = client.get("/check?user_id=12&item_id=receipt_27")
    assert response.status_code == 200
    assert response.json() == [{"item_id": "receipt_27", "problem": "NO_RECEIPT"}]
def test_check_cart_special_with_user():
    response = client.get("/check?user_id=11&item_id=special_26")
    assert response.status_code == 200
    assert response.json() == [{"item_id": "special_26", "problem": "ITEM_IS_SPECIAL"}]