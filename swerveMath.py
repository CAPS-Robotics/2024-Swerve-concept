import math

# For a single wheel (Ex. Front)

# Values you get
r = 15*1.41 # numerical distance from corner to center on 30x30, r variable is dist. from robot center to pivot
wb = 30 # wheelbase
wt = 30 # wheeltrack

da = 10 # change in angle, sensor
dt = 10 # change in time, sensor

# angular velocity of the wheel
wz = da/dt 

# linear velocity
speed = 10 # speed of the bot, In RPM, sensor
angle = 10 # angle of the bot, gyro sensor
v = 0 # linear velocity vector
v = (v * math.cos(angle), v * math.sin(angle))

# resultant velocity
vw = v + wz

vx = 0 # x-component
vy = 1 # y-component

rx = wb/2
ry = wt/2

# components
vfrx = vx + rx*wz
vfry = vy + ry*wz
wheel_r = 10 # wheel radius

steer_angle = math.atan(vfry/vfrx)
wheel_angular = (vfrx**2+vfry**2)**0.5/wheel_r

# optimal wheel steering
# make an angle in the lowest amount of movement possible
# if at -90, one can move to -60/60 by moving -30deg rather than moving 150deg

# wheel odometry
# relative change in position over time
# two steps, compute drift from joint states, update pose over time

# computing the xy changes for wheels
wfr = 0 # wheel angular velocity
vfrx = wfr * wheel_r * math.cos(steer_angle)
vfry = wfr * wheel_r * math.sin(steer_angle)

# the pose update

# start by zeroing the pose
x = 0 # x update
y = 0 # y update
a = 0 # angle theta
Dt = 10 # change in time, arbitrary here, but measured real time

# update the values
x = x + (vx*math.cos(a)-vy*math.sin(a))*Dt
y = y + (vx*math.cos(a)+vy*math.sin(a))*Dt
a = a + wz*Dt

# multiply all velocities for scaling factors for safety

max_m = 50 # max speed a motor can be, arb. value
max_a = 10 # max ang. vel. a motor can be, arb. value

scale_f = max_m/max_a