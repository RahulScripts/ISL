# Smart home agent: fan + lights

def control_fan(temp, fan_on_threshold=28):
    if temp >= fan_on_threshold:
        return "FAN: ON"
    else:
        return "FAN: OFF"

def control_light(time_of_day, light_intensity, night_start=18, night_end=6, low_light_threshold=30):
    # time_of_day in 0–23, light_intensity 0–100
    is_night = (time_of_day >= night_start) or (time_of_day < night_end)
    if is_night and light_intensity < low_light_threshold:
        return "LIGHT: ON"
    else:
        return "LIGHT: OFF"

def main():
    temp = float(input("Enter temperature (°C): "))
    light_intensity = int(input("Enter light intensity (0-100): "))
    time_of_day = int(input("Enter time of day (0-23): "))

    print(control_fan(temp))
    print(control_light(time_of_day, light_intensity))

if __name__ == "__main__":
    main()
