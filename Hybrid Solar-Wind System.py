# Hybrid Solar-Wind Power System
# EEE Mini Project - Python

class HybridSolarWindSystem:

    def __init__(self, solar_efficiency, wind_efficiency):
        self.solar_efficiency = solar_efficiency
        self.wind_efficiency = wind_efficiency

    def solar_power(self, irradiance, panel_area):
        # Solar Power = Irradiance × Area × Efficiency
        power = irradiance * panel_area * self.solar_efficiency
        return power

    def wind_power(self, air_density, swept_area, wind_speed):
        # Wind Power = 0.5 × ρ × A × V³ × Efficiency
        power = (
            0.5
            * air_density
            * swept_area
            * (wind_speed ** 3)
            * self.wind_efficiency
        )
        return power

    def total_power(self, solar, wind):
        return solar + wind


# Main Program
print("======================================")
print("   HYBRID SOLAR-WIND POWER SYSTEM")
print("======================================")

# Input values
irradiance = float(input("Enter solar irradiance (W/m²): "))
panel_area = float(input("Enter solar panel area (m²): "))

wind_speed = float(input("Enter wind speed (m/s): "))
swept_area = float(input("Enter wind turbine swept area (m²): "))

# Typical simplified values
solar_efficiency = 0.20
wind_efficiency = 0.35
air_density = 1.225

# Create system
system = HybridSolarWindSystem(
    solar_efficiency,
    wind_efficiency
)

# Calculate power
solar = system.solar_power(
    irradiance,
    panel_area
)

wind = system.wind_power(
    air_density,
    swept_area,
    wind_speed
)

total = system.total_power(
    solar,
    wind
)

# Display results
print("\n----------- POWER OUTPUT -----------")
print(f"Solar Power : {solar:.2f} W")
print(f"Wind Power  : {wind:.2f} W")
print(f"Total Power : {total:.2f} W")

print("------------------------------------")

if total > 0:
    print("Hybrid System Status: POWER GENERATING")
else:
    print("Hybrid System Status: NO POWER")
