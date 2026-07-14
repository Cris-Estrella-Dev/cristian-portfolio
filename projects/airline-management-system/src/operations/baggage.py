class Baggage:
    def __init__(self,bag_id, bag_type):

        if not bag_id or not bag_id.strip():
            raise ValueError("Bag id cannot be empty.")
        
        if not bag_type or not bag_type.strip():
            raise ValueError("Bag type cannot be empty.")



        self.__bag_id = bag_id.strip()
        self.__bag_type = bag_type.strip()
    
    def get_bag_id(self):
        return self.__bag_id
    
    def get_bag_type(self):
        return self.__bag_type
    
    def show_info(self):
        print(f"Bag ID: {self.__bag_id}")
        print(f"Bag type: {self.__bag_type}")

    def __str__(self):
        return f"{self.get_bag_id()} - {self.get_bag_type()}"
    
    def to_dict(self):
        return{
            "bag_id": self.__bag_id,
            "bag_type": self.__bag_type
        }
    
    @staticmethod
    def from_dict(data):
        return Baggage(
            data["bag_id"],
            data["bag_type"]
        )