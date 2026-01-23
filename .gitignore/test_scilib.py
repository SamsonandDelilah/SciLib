from scilib import config, deg_to_rad
import sys

print(f"Python: {sys.version}")
print(f"Mode: {config.errors.mode}")

print(f"✓ Angle: {deg_to_rad('180°')}")
print(f"✓ Constant: {config.physical_constants('speed_of_light')}")

data_path = config._get_data_path()
print(f"Data path: {data_path}")
print(f"Data exists: {data_path.exists()}")
print(f"speed_of_light.json: {(data_path / 'constants/speed_of_light.json').exists()}")
