import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

def fan_sim():
    temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
    fan_speed = ctrl.Consequent(np.arange(0, 6, 1), 'fan_speed')

    # Membership functions for temperature
    temperature['low'] = fuzz.trimf(temperature.universe, [0, 0, 20])
    temperature['medium'] = fuzz.trimf(temperature.universe, [15, 25, 30])
    # Adjusted 'high' to start earlier to cover values around 30
    temperature['high'] = fuzz.trimf(temperature.universe, [25, 35, 40])


    # Membership functions for fan speed
    fan_speed['speed_0'] = fuzz.trimf(fan_speed.universe, [0, 0, 1])
    fan_speed['speed_1'] = fuzz.trimf(fan_speed.universe, [0, 1, 2])
    fan_speed['speed_2'] = fuzz.trimf(fan_speed.universe, [1, 2, 3])
    fan_speed['speed_3'] = fuzz.trimf(fan_speed.universe, [2, 3, 4])
    fan_speed['speed_4'] = fuzz.trimf(fan_speed.universe, [3, 4, 5])
    fan_speed['speed_5'] = fuzz.trimf(fan_speed.universe, [4, 5, 5])

    # Rules
    rule1 = ctrl.Rule(temperature['low'], fan_speed['speed_0'])
    rule2 = ctrl.Rule(temperature['medium'], fan_speed['speed_2'])
    rule3 = ctrl.Rule(temperature['high'], fan_speed['speed_5'])

    fan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
    fan_simulation = ctrl.ControlSystemSimulation(fan_ctrl)

    return temperature, fan_speed, fan_simulation

# =============================
# PLOT MEMBERSHIP FUNCTIONS
# =============================

temperature, fan_speed, fan_simulation = fan_sim()

# =============================
# RUN AN EXAMPLE
# =============================
temp_input = float(input("Enter temperature: "))
fan_simulation.input['temperature'] = temp_input
fan_simulation.compute()

print("Fan speed output:", round(fan_simulation.output['fan_speed']), "raw output: ", fan_simulation.output['fan_speed'])

fan_speed.view(sim=fan_simulation)
plt.show()