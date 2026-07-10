from src.operations.baggage import Baggage

def test_baggage_to_dict():

    #Arrange
    baggage_data = Baggage(
        "034",
        "Red hard shell bag"
    )

    
    expected = {
        "bag_id": "034",
        "bag_type": "Red hard shell bag"
    }

    #Act
    baggage = Baggage.to_dict(baggage_data)


    assert baggage == expected


def test_baggage_from_dict():


    
    baggage_data = {
        "bag_id": "034",
        "bag_type": "Red hard shell bag"
    }

    baggage = Baggage.from_dict(baggage_data)
    
    assert baggage.get_bag_id() == '034'
    assert baggage.get_bag_type() == 'Red hard shell bag'