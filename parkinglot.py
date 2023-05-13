# write code for parking lot system which have park
class ParkingLot():
    def __init__(self):
        self.level_a = {i: None for i in range(1, 21)}
        self.level_b = {i: None for i in range(21, 41)}

    # assign_spot function for alotment of parking spot and it will return the parking spot number
    def assign_spot(self, vehicle_number):
        try:
            if None in self.level_a.values():
                for spot, value in self.level_a.items():
                    if value == None:
                        self.level_a[spot] = vehicle_number
                        return spot
            if None in self.level_b.values():
                for spot, value in self.level_b.items():
                    if value == None:
                        self.level_b[spot] = vehicle_number
                        return spot
        except Exception as e:
            return (f"Exception Type : '{type(e).__name__}', Exception Message: {e}")

    # retrive_spot function is to retrieve or get the spot information using vehicle number
    def retrieve_spot(self, vehicle_number):
        try:
            for spot, veh_num in self.level_a.items():
                if veh_num == vehicle_number:
                    return {"level": "A", "spot": spot}
            for spot, veh_num in self.level_b.items():
                if veh_num == vehicle_number:
                    return {"level": "B", "spot": spot}
        except Exception as e:
            return (f"Exception Type : '{type(e).__name__}', Exception Message: {e}")

    # available_spots function for checking availbility of parking lot
    def available_spots(self):
        try:
            available_spots_a = []
            available_spots_b = []
            if None in self.level_a.values():
                for key, value in self.level_a.items():
                    if value == None:
                        available_spots_a.append(key)
            if None in self.level_b.values():
                for key, value in self.level_b.items():
                    if value == None:
                        available_spots_b.append(key)
            if len(available_spots_a) > 0 and len(available_spots_b) > 0:
                response = f"available spots in level A {available_spots_a} and available spots in level B {available_spots_b}"
            elif len(available_spots_a) > 0:
                response = f"available spots in level A are: {available_spots_a}"
            elif len(available_spots_b) > 0:
                response = f"available spots in level B are: {available_spots_b}"
            else:
                response = "We are sorry, Parking lot is full"
            return response
        except Exception as e:
            return (f"Exception Type : '{type(e).__name__}', Exception Message: {e}")


def main():
    parking_lot = ParkingLot()

    while True:
        print("1. Assign a parking spot to a new vehicle")
        print("2. Retrieve parking spot number for a vehicle")
        print("3. availble parking spots")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            vehicle_number = input("Enter vehicle number: ")
            spot = parking_lot.assign_spot(vehicle_number)
            if spot:
                print(f"Assigned spot: {spot}")
            else:
                print("No available spots.")

        elif choice == "2":
            vehicle_number = input("Enter vehicle number: ")
            spot = parking_lot.retrieve_spot(vehicle_number)
            if spot:
                print(f"parked at : {spot}")
            else:
                print("Vehicle not found in the parking lot")

        elif choice == "3":
            available_spots = parking_lot.available_spots()
            print(available_spots)

        elif choice == "4":
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
