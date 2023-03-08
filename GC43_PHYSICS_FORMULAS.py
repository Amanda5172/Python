import math
p=["speed, distance, time", "density, mass, volume", "pressure, force, area", "momentum, mass, velocity", "weight, mass, gravity", "potential energy, mass, gravity, height", "kinetic energy, mass, velocity", "moment, force, perpendicular distance", "acceleration, final velocity, initial velocity, time"]

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

def wmg():
    weight=int(input("Weight: "))
    mass=int(input("Mass: "))
    gravity=int(input("Gravity: "))
    if mass==0:
        mass = weight/gravity
        return mass
    elif weight==0:
        weight=mass*gravity
        return weight
    elif gravity==0:
        gravity=weight/mass
        return gravity

def gpe():
    pe=int(input("Potential Energy: "))
    height=int(input("Height: "))
    mass=int(input("Mass: "))
    gravity=int(input("Gravity: "))
    if pe==0:
        pe = mass*height*gravity
        return pe
    elif height==0:
        height = pe/(mass*gravity)
        return height
    elif mass==0:
        mass=pe/(height*gravity)
        return mass
    elif gravity==0:
        gravity=pe/(mass*height)
        return gravity

def ke():
    ke=int(input("Kinetic energy: "))
    mass=int(input("Mass: "))
    velocity=int(input("Velocity: "))
    if ke==0:
        ke = mass*(velocity**2)/2
        return ke
    elif mass==0:
        mass=2*ke/(velocity**2)
        return mass
    elif velocity==0:
        velocity=math.sqrt(2*ke/mass)
        return velocity

def mfd():
    moment=int(input("Moment: "))
    force=int(input("Force: "))
    distance=int(input("Perpendicular distance: "))
    if moment==0:
        moment = force*distance
        return moment
    elif force==0:
        force=moment/distance
        return force
    elif distance==0:
        distance=moment/force
        return distance

def uvat():
    acceleration=int(input("Acceleration: "))
    initial=int(input("Initial velocity: "))
    final=int(input("Final velocity: "))
    time=int(input("Time: "))
    if acceleration==0:
        acceleration = (final-initial)/time
        return acceleration
    elif initial==0:
        initial=final - (acceleration*time)
        return initial
    elif final==0:
        final=initial + (acceleration*time)
        return final
    elif time==0:
        time = (final-initial)/acceleration
        return time
    
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
    print(wmg())
if i==5:
    print(gpe())
if i==6:
    print(ke())
if i==7:
    print(mfd())
if i==8:
    print(uvat())

