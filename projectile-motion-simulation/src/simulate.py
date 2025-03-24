import numpy as np
import pandas as pd
import os

def euler_projectile(v0, angle_deg, dt, total_time, g=9.81, save_path=None):
    """
    Simulates projectile motion using Euler’s method.

    Parameters:
    - v0: Initial speed in m/s
    - angle_deg: Launch angle in degrees
    - dt: Time step (e.g., 0.01)
    - total_time: Total simulation time in seconds
    - g: Gravitational acceleration
    - save_path: Path to save CSV (optional)

    Returns:
    - Pandas DataFrame with time, x, y, vx, vy
    """
    angle_rad = np.radians(angle_deg)
    vx = float(v0 * np.cos(angle_rad))
    vy = float(v0 * np.sin(angle_rad))
    x = y = t = 0.0
    data = []

    while y >= 0 and t <= total_time:
        row = [float(t), float(x), float(y), float(vx), float(vy)]
        data.append(row)

        x += vx * dt
        vy -= g * dt
        y += vy * dt
        t += dt

    df = pd.DataFrame(data, columns=["time", "x", "y", "vx", "vy"])

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        df.to_csv(save_path, index=False)

    return df
