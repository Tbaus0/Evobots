import numpy
import matplotlib.pyplot as plt

# backLegSensorValues = numpy.load("data/backLegSensorValues.npy")

# frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")

# plt.plot(backLegSensorValues,label='Back Leg',linewidth=5)

# plt.plot(frontLegSensorValues,label="Front Leg")

backLeg_targetAngles = numpy.load("data/backLeg_targetAngles.npy")
frontLeg_targetAngles = numpy.load("data/frontLeg_targetAngles.npy")

plt.plot(backLeg_targetAngles)
plt.plot(frontLeg_targetAngles)
plt.legend()
plt.show()
