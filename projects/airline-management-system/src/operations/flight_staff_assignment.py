-assignment_id: str
-flight: Flight
-ops_agents: list[OpsAgent]
-ramp_agents: list[RampAgent]



class FlightStaffAssignment:
    def __init__(self,assignment_id,flight):
        self.__assignment_id = assignment_id
        self.__flight = flight
        self.__ops_agents = []
        self.__ramp_agents = []


    def add_ops_agent(self):
        pass

    def add_ramp_agent(self):
        pass

    def show_staff(self):
        pass
        
    