import matplotlib.pyplot as plt
import numpy as np

with open("position4.txt", "r") as f:
	lines = f.readlines()
	timestep = [int(line.split(",")[0]) for line in lines]
	EncoderPosition = [int(line.split(",")[1]) for line in lines]
	#EncoderVelocity = [int(line.split(",")[3]) for line in lines]
	CurrentCartPosition =[int(line.split(",")[3]) for line in lines]
	CurrentCartVelocity = [int(line.split(",")[2]) for line in lines]
	#CurrentCartAcceleration =[int(line.split(",")[6]) for line in lines]
	cpuTime =  [float(line.split(",")[4]) for line in lines]
	cpuTimeDiff = np.diff(cpuTime)
	#Add an element to the end of the array to make the sizes equal for plotting
	np.append(cpuTimeDiff,[0])

	print(cpuTimeDiff)
	
#print(lines)
plt.figure(1)
plt.plot(timestep,EncoderPosition)
plt.ylabel('Position [2400 Counts/Rev]')
plt.xlabel('Time')
plt.title('Pendulum Angular Position')


plt.figure(2)
plt.plot(timestep,CurrentCartVelocity)
plt.ylabel('Velocity [mm/min]')
plt.xlabel('Time')
plt.title('Velocity of Cart')

plt.figure(3)
plt.plot(cpuTimeDiff,linestyle="None", marker='o')
plt.ylabel('cpuTimeDiff [seconds]')
plt.xlabel('TimeStep')
plt.title('Difference between Python CPU Timestamps')

plt.figure(4)
plt.plot(timestep,CurrentCartPosition)
plt.ylabel('Cart Position [Counts]')
plt.xlabel('timestep')
plt.title('Cart Position')
plt.show()

