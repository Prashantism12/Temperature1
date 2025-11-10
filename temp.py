import sys

if len(sys.argv) > 1:
    temperature = float(sys.argv[1])   
else:
    temperature = 25.0                 


if temperature < 15:
    print(f"Temperature: {temperature}°C → Cold")
elif 15 <= temperature <= 30:
    print(f"Temperature: {temperature}°C → Normal")
else:
    print(f"Temperature: {temperature}°C → Hot")
