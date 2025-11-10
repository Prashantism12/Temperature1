import sys


if len(sys.argv) != 2:
    print("No temperature provided — using default temperature of 25°C.")
    temp = 25
else:
    temp = float(sys.argv[1])

# Classify temperature
if temp < 15:
    condition = "Cold"
elif 15 <= temp <= 30:
    condition = "Normal"
else:
    condition = "Hot"

# Display results
print(f"Temperature: {temp:.2f}°C")
print(f"Condition: {condition}")
