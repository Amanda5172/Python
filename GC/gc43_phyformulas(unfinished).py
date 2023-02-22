p=["speed, distance, time", "density, mass, volume", "pressure, force, area", "momentum, mass, velocity", "weight, mass, gravity", "potenntial energy, mass, gravity, height", "kinetic energy, mass, velocity", "moment, force, perpendicular distance", "acceleration, final velocity, initial velocity, time"]

def sdt():
    speed=int(input("Speed: "))
    distance=int(input("Distance: "))
    time=int(input("Time: "))
    if speed==0:
        speed = distance/time
        return speed
    elif distance==0:
        distance=speed*time
        return distance
    elif time==0:
        time=distance/speed
        return time
    

def dmv():
    density=int(input("Density: "))
    mass=int(input("Mass: "))
    volume=int(input("Volume: "))
    if density==0:
        density = mass/volume
        return density
    elif mass==0:
        mass=density*volume
        return mass
    elif volume==0:
        volume=mass/density
        return volume

def pfa():
    pressure=int(input("Pressure: "))
    force=int(input("Force: "))
    area=int(input("Area: "))
    if pressure==0:
        pressure = force/area
        return pressure
    elif force==0:
        force=pressure*area
        return force
    elif area==0:
        area=force/pressure
        return area

def mmv():
    momentum=int(input("Momentum: "))
    mass=int(input("Mass: "))
    velocity=int(input("Velocity: "))
    if mass==0:
        mass = momentum/velocity
        return mass
    elif momentum==0:
        momentum=mass*velocity
        return momentum
    elif velocity==0:
        velocity=momentum/mass
        return velocity


    

for j in range(len(p)):
    print(j,p[j])
    
print()
i=int(input("Input which formula number you would like to use: "))
print("Input all values in their base units.")
print("Put 0 for the unknown value.")
print()

if i==0:
    print(sdt())
if i==1:
    print(dmv())
if i==2:
    print(pfa())
if i==3:
    print(mmv())
if i==4:
    print(dmv())




    
