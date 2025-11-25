# Smart heater agent: based on temp, season, time

def control_heater(temp, season, hour, winter_temp_threshold=20, winter_night_start=18, winter_morning_end=9):
    season = season.lower()
    is_winter = (season == "winter")
    is_winter_hours = (hour >= winter_night_start) or (hour < winter_morning_end)

    if is_winter and is_winter_hours and temp < winter_temp_threshold:
        return "HEATER: ON"
    else:
        return "HEATER: OFF"

def main():
    temp = float(input("Enter temperature (°C): "))
    season = input("Enter season (summer/winter/other): ")
    hour = int(input("Enter hour (0-23): "))

    print(control_heater(temp, season, hour))

if __name__ == "__main__":
    main()
