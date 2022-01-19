This repository gives an overview of how we can design a basic parking lot in Python. It creates parking lot with given number of slots. The cars follow Greedy approach while being parked in the slots.
main.py = this is a input file you have to give required input here
interactive.py = there are lot of methods 
managing_parking-lot.py = here we have created a lots of command

there are few function 

create_parking_lot n - Given n number of slots, create a parking lot

park car_regno car_color - Parks a vehicle with given registration number and color in the nearest empty slot possible. If there are no more empty slots available, it shows a message "Sorry, parking lot is full".

status - Prints the slot number, registration number and color of the parked vehicles.

leave x - Removes vehicle from slot number x

I have added a feature by which you can extend the number of parking slot if you required at any instance of program.To perform this you will have to add a command in input file.(modify 10).This will add 10 more new slot.