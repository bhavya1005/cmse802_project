from src.simulate import euler_projectile
import pandas as pd
import os

# Ensure results directory exists
os.makedirs("results", exist_ok=True)

# Try small range first to confirm functionality
speeds = [20, 40]
angles = [30, 60]

all_data = []

for v0 in speeds:
    for angle in angles:
        print(f"Simulating v0 = {v0} m/s, angle = {angle}°")
        df = euler_projectile(
            v0=v0,
            angle_deg=angle,
            dt=0.01,
            total_time=10,
            save_path=None  # Not saving individual simulations
        )
        df["v0"] = v0
        df["angle"] = angle
        all_data.append(df)

# Combine all simulation outputs into one CSV
combined_df = pd.concat(all_data, ignore_index=True)
combined_df.to_csv("results/large_projectile_dataset.csv", index=False)
print("✅ Saved to results/large_projectile_dataset.csv")
