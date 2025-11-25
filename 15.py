import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
import matplotlib.pyplot as plt

def ac_sim():
    # INPUT: Temperature (0–50°C)
    temperature = ctrl.Antecedent(np.arange(0, 51, 1), 'temperature')

    # OUTPUT: AC speed from 0–5
    ac_speed = ctrl.Consequent(np.arange(0, 6, 1), 'ac_speed')

    # --- Define membership functions for TEMP ---
    temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 22])
    temperature['comfortable'] = fuzz.trimf(temperature.universe, [18, 25, 32])
    temperature['hot'] = fuzz.trimf(temperature.universe, [28, 50, 50])

    # --- Define membership functions for AC SPEED ---
    ac_speed['speed_0'] = fuzz.trimf(ac_speed.universe, [0, 0, 1])
    ac_speed['speed_1'] = fuzz.trimf(ac_speed.universe, [0, 1, 2])
    ac_speed['speed_2'] = fuzz.trimf(ac_speed.universe, [1, 2, 3])
    ac_speed['speed_3'] = fuzz.trimf(ac_speed.universe, [2, 3, 4])
    ac_speed['speed_4'] = fuzz.trimf(ac_speed.universe, [3, 4, 5])
    ac_speed['speed_5'] = fuzz.trimf(ac_speed.universe, [4, 5, 5])

    # --- Fuzzy rules ---
    rule1 = ctrl.Rule(temperature['cold'], ac_speed['speed_0'])
    rule2 = ctrl.Rule(temperature['comfortable'], ac_speed['speed_2'])
    rule3 = ctrl.Rule(temperature['hot'], ac_speed['speed_5'])

    ac_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
    ac_simulation = ctrl.ControlSystemSimulation(ac_ctrl)

    return temperature, ac_speed, ac_simulation

    temperature, ac_speed, ac_simulation = ac_sim()

    temperature.view()
    ac_speed.view()
    plt.show()

temp = float(input("Enter room temperature: "))

ac_simulation.input['temperature'] = temp
ac_simulation.compute()

print("AC speed output:", ac_simulation.output['ac_speed'])
ac_speed.view(sim=ac_simulation)
plt.show()

