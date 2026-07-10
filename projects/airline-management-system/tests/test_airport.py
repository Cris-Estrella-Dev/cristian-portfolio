from src.operations.airport import Airport

def test_airport_to_dict():

    #Arrange
    origin_airport_data = Airport(
        "LGA",
        "LaGuardia Airport",
        "Queens - NYC",
        "NY",
        "USA"
    )

    destination_aiport_data = Airport(
        "BNA",
        "Nashville International Airport",
        "Nashville",
        "TN",
        "USA"
    )

    expected_origin_airport = {
        "airport_code": "LGA",
        "name": "LaGuardia Airport",
        "city": "Queens - NYC",
        "state": "NY",
        "country": "USA"
    }

    expected_destination_airport = {
        "airport_code": "BNA",
        "name": "Nashville International Airport",
        "city": "Nashville",
        "state": "TN",
        "country": "USA"
    }

    #Act
    origin_airport = Airport.to_dict(origin_airport_data)
    destination_aiport = Airport.to_dict(destination_aiport_data)


    assert origin_airport == expected_origin_airport
    assert destination_aiport == expected_destination_airport

def test_airport_from_dict():
    
    origin_airport_data = {
        "airport_code": "LGA",
        "name": "LaGuardia Airport",
        "city": "Queens - NYC",
        "state": "NY",
        "country": "USA"
    }

    destination_airport_data = {
        "airport_code": "BNA",
        "name": "Nashville International Airport",
        "city": "Nashville",
        "state": "TN",
        "country": "USA"
    }



    origin_airport = Airport.from_dict(origin_airport_data)
    destination_airport = Airport.from_dict(destination_airport_data)


    #Origin Airport
    assert origin_airport.get_airport_code() == 'LGA'
    assert origin_airport.get_name() == 'LaGuardia Airport'
    assert origin_airport.get_city() == 'Queens - NYC'
    assert origin_airport.get_state() == 'NY'
    assert origin_airport.get_country() == 'USA'

    #Destination Airport
    assert destination_airport.get_airport_code() == 'BNA'
    assert destination_airport.get_name() == 'Nashville International Airport'
    assert destination_airport.get_city() == 'Nashville'
    assert destination_airport.get_state() == 'TN'
    assert destination_airport.get_country() == 'USA'