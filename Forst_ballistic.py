# Marcus Forst
# Python Ballistic Motion


# Inputs: Gravitational constant, initial velocity, velocity angle, height, time step
import math as ma

g= float(input("What is the gravitational acceleration?"))
v0=float(input('What is the initial velocity magnitude?'))
phi0=float(input('What is the initial velocity angle, in degrees?'))
y0=float(input('What is the initial height?'))
dt=float(input('What is the time step?'))

x=0.0 #Initial x value
y=y0 #Initial y value
vx=v0*ma.cos(ma.pi*phi0/180) #X-velocity, will be constant because gravity only acts in y direction
vy=v0*ma.sin(ma.pi*phi0/180) #y velocity, will change over time
xlist= [x] #makes a list with the x velocities
ylist= [y] #^^ y velocities

while y>=0: #iterates only when y>=0, when the projectile has yet to hit the ground.
	vy=vy-g*dt #modifies y velocity
	x=x+vx*dt #modifies x position
	y=y+vy*dt #modifies y position
	xlist.append(x) #adds new x position to xlist
	ylist.append(y) #adds new y position to ylist

High= max(ylist) #finds the max height
ftime= round(max(xlist)/vx,3) #finds the flight time. 

# print ("The x values are", xlist)
# print ("The y values are", ylist,". This is the distance to the ground.")
print ("The Highest point is", High, "meters.")
print ("The flight time is", ftime, "seconds.")
print ("The distance traveled along the ground is", x, "meters.")
# Outputs: Highest point, distance to ground, flight time, plot of xy (optional)


