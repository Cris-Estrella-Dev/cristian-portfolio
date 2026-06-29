class Baggage:
    def __init__(self,bag_id, bag_type):
        self.__bag_id = bag_id
        self.__bag_type = bag_type
    
    def get_bag_id(self):
        return self.__bag_id
    
    def get_bag_type(self):
        return self.__bag_type
    
    def show_info(self):
        print(f"Bag ID: {self.__bag_id}")
        print(f"Bag type: {self.__bag_type}")

    def __str__(self):
        return f"{self.get_bag_id()} - {self.get_bag_type()}"