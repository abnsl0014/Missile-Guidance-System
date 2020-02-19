#Let Missile Location Coordinates
traj_x = 108
traj_y = 106
traj_z = 105

#Let prediction Location Coordinates
traj1_x = 0
traj1_y = 1
traj1_z = 2

#let Actual Cordinates of Air Object
traj_currx = 9
traj_curry = 8
traj_currz = 12

#Let Velocity of Target Shooting Missile

initial_velocity = 120

distance_x = traj_x - traj1_x
distance_y = traj_y - traj1_y
distance_z = traj_x - traj1_z

theta = math.atan(distance_x / distance_y)
phi = math.atan(distance_z / distance_x)

#Let Acceleration Due To Gravity is
g = 9.8

#Time needed by Object to move at predicted Position

Time_needed = 5

#if (Time_needed_to reach predicted point == Time Needed by MIssile to hit the object) therfore we can shoot at that point of time.

Distance = sqrt((traj1_x - traj_x)**2 + (traj1_y - traj_y)**2 + (traj1_z - traj_z)**2)
print(Distance)   
if abs(Distance - (initial_velocity * math.cos(theta)*math.sin(phi)*Time_needed - (0.5*g*((Time_needed)**2)))) <= 5:
    print("We can shoot")
else:
    print("Wait For the Next Interception")
    print(initial_velocity * math.cos(theta)*math.sin(phi)*Time_needed - (0.5*g*((Time_needed)**2)))
