# Marcus Forst
# Python Ballistic Motion


# Inputs: Gravitational constant, initial velocity, velocity angle, height, time step
import math as ma

g= float(input("What is the gravitational constant?"))
v0=float(input('What is the initial velocity magnitude?'))
phi0=float(input('What is the initial velocity angle, in degrees?'))
y0=float(input('What is the initial height?'))
dt=float(input('What is the time step?'))


for i:
	x(0)=0
	y(0)=y0
	xlist=list[x(0)]
	ylist=list[y(0)]
	vx=v0*ma.cos(ma.pi*phi0/180)
	vy(0)=v0*ma.sin(ma.pi*phi0/180)
	vy(i+1)=vy(i)-g*dt
	x(i+1)=x(i)+vx*dt
	y(i+1)=y(i)+vy(i)*dt-0.5*g*(dt^2)
	if y(i+1)==0:
		xlist.append(x(i+1))
		ylist.append(y(i+1))
		break
	else:
		xlist.append(x(i+1))
		ylist.append(y(i+1))
High= max(ylist)
ftime= max(xlist)/vx

print ("The x values are", xlist)
print ("The y values are", ylist,". This is the distance to the ground.")
print ("The Highest point is", High)
print ("The flight time is", ftime, "seconds")
# Outputs: Highest point, distance to ground, flight time, plot of xy (optional)


