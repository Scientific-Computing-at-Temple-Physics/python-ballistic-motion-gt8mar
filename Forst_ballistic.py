# Marcus Forst
# Python Ballistic Motion


# Inputs: Gravitational constant, initial velocity, velocity angle, height, time step
import math as ma

g= float(input("What is the gravitational acceleration?"))
v0=float(input('What is the initial velocity magnitude?'))
phi0=float(input('What is the initial velocity angle, in degrees?'))
y0=float(input('What is the initial height?'))
dt=float(input('What is the time step?'))

x=0.0
y=y0
vx=v0*ma.cos(ma.pi*phi0/180)
vy=v0*ma.sin(ma.pi*phi0/180)
xlist= [x]
ylist= [y]
ftime=0.0
while y>=0:
	vy=vy-g*dt
	x=x+vx*dt
	y=y+vy*dt
	xlist.append(x)
	ylist.append(y)

High= max(ylist)
ftime= round(max(xlist)/vx,3)

# print ("The x values are", xlist)
# print ("The y values are", ylist,". This is the distance to the ground.")
print ("The Highest point is", High)
print ("The flight time is", ftime, "seconds")
# Outputs: Highest point, distance to ground, flight time, plot of xy (optional)


