from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_calculate_monthly_payment():
    # Test case 1: Minimum down payment, no interest
    car_price = 100000
    down_payment = 20000
    monthly_payment = calculate_monthly_payment(car_price, down_payment)
    assert monthly_payment == 6666.67

    # Test case 2: Minimum down payment, with interest
    car_price = 80000
    down_payment = 16000
    interest_rate = 0.05
    monthly_payment = calculate_monthly_payment(car_price, down_payment, interest_rate)
    assert monthly_payment == 5786.67

    # Test case 3: Down payment less than 20%
    car_price = 90000
    down_payment = 15000
    with pytest.raises(ValueError):
        monthly_payment = calculate_monthly_payment(car_price, down_payment)

def test_calculate_total_payment():
    # Test case 1: Minimum down payment, no interest
    car_price = 100000
    down_payment = 20000
    total_payment = calculate_total_payment(car_price, down_payment)
    assert total_payment == 100000

    # Test case 2: Minimum down payment, with interest
    car_price = 80000
    down_payment = 16000
    interest_rate = 0.05
    total_payment = calculate_total_payment(car_price, down_payment, interest_rate)
    assert total_payment == 84000

    # Test case 3: Down payment less than 20%
    car_price = 90000
    down_payment = 15000
    with pytest.raises(ValueError):
        total_payment = calculate_total_payment(car_price, down_payment)
