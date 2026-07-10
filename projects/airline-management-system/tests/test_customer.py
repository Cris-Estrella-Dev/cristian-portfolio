from src.customers.customer import Customer



def test_customer_to_dict():
    # Arrange
    customer = Customer(
        "C001",
        "Nawel",
        "Tavares",
        "nawel@example.com",
        "809-702-3396"
    )

    expected = {
        "customer_id": "C001",
        "first_name": "Nawel",
        "last_name": "Tavares",
        "email": "nawel@example.com",
        "phone_number": "809-702-3396"
    }

    # Act
    result = customer.to_dict()

    # Assert
    assert result == expected


def test_customer_from_dict():
    # Arrange
    customer_data = {
        "customer_id": "C001",
        "first_name": "Nawel",
        "last_name": "Tavares",
        "email": "nawel@example.com",
        "phone_number": "809-702-3396"
    }

    # Act
    customer = Customer.from_dict(customer_data)

    # Assert
    assert customer.get_customer_id() == "C001"
    assert customer.get_full_name() == "Nawel Tavares"
    assert customer.get_email() == "nawel@example.com"
    assert customer.get_phone_number() == "809-702-3396"


def test_customer_serialization_round_trip():
    # Arrange
    original_customer = Customer(
        "C001",
        "Nawel",
        "Tavares",
        "nawel@example.com",
        "809-702-3396"
    )

    # Act
    customer_data = original_customer.to_dict()
    reconstructed_customer = Customer.from_dict(customer_data)

    # Assert
    assert reconstructed_customer.to_dict() == original_customer.to_dict()





