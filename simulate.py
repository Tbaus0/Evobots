from simulation import SIMULATION

# file_path = os.path.join("data", "backLeg_targetAngles.npy")
# np.save(file_path, backLeg_targetAngles)

# # file_path = os.path.join("data", "frontLeg_targetAngles.npy")
# # np.save(file_path, frontLeg_targetAngles)



# file_path = os.path.join("data", "backLegSensorValues.npy")
# np.save(file_path, backLegSensorValues)

# file_path = os.path.join("data", "frontLegSensorValues.npy")
# np.save(file_path, frontLegSensorValues)

# p.disconnect()
simulation = SIMULATION()
simulation.Run()