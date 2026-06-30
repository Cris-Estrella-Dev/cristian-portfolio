class FlightStaffAssignment:
    def __init__(self,assignment_id,flight):
        self.__assignment_id = assignment_id
        self.__flight = flight
        self.__ops_agents = []
        self.__ramp_agents = []


    def get_assignment_id(self):
        return self.__assignment_id
    
    def get_flight(self):
        return self.__flight

    def add_ops_agent(self,ops_agent):
        self.__ops_agents.append(ops_agent)
        print("Ops agent added succesfully!")

    def add_ramp_agent(self,ramp_agent):
        self.__ramp_agents.append(ramp_agent)
        print("Ramp agent added succesfully!")

    def show_staff(self):
        print(f"Assignment ID: {self.__assignment_id}")
        print(f"Flight: {self.__flight}")

        if not self.__ops_agents:
            print("There are no Ops Agents added")
        else:
            print("-------------------------------------------\n")
            for ops_agent in self.__ops_agents:
                ops_agent.show_info()
            print("-------------------------------------------\n")
        if not self.__ramp_agents:
            print("There are no Ramp Agents added")
        else:

            for ramp_agent in self.__ramp_agents:
                ramp_agent.show_info()

        
    