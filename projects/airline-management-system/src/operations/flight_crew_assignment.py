class FlightCrewAssignment:
    def __init__(self, assignment_id, flight):
        self.__assignment_id = assignment_id
        self.__flight = flight
        self.__pilots = []
        self.__flight_attendants = []

    def get_assignment_id(self):
        return self.__assignment_id
    
    def get_flight(self):
        return self.__flight

    def add_pilot(self, pilot):
        self.__pilots.append(pilot)
        print("Pilot added successfully.")

    def add_flight_attendant(self, flight_attendant):
        self.__flight_attendants.append(flight_attendant)
        print("Flight attendant added successfully.")

    def show_crew(self):
        print(f"Assignment ID: {self.__assignment_id}")
        print(f"Flight: {self.__flight}")
        
        print("\nPilots:")
        if not self.__pilots:
            print("No pilots added.")
        else:
            for pilot in self.__pilots:
                pilot.show_info()
                print()

        print("Flight Attendants:")
        if not self.__flight_attendants:
            print("No flight attendants added.")
        else:
            for flight_attendant in self.__flight_attendants:
                flight_attendant.show_info()
                print()