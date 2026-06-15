import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from scipy.fft import fft, fftfreq

# =====================================================
# FILE LOCATIONS
# =====================================================

folder = "/Users/Chelsea/Downloads/robotcode"

files = {
    "smooth": os.path.join(folder, "terrain_smooth.csv"),
    "rough": os.path.join(folder, "terrain_rough.csv"),
    "carpet": os.path.join(folder, "terrain_carpet.csv")
}

# =====================================================
# STORAGE
# =====================================================

summary_results = {}

# =====================================================
# PROCESS EACH TERRAIN
# =====================================================

for terrain, file in files.items():

    print("\n" + "="*50)
    print(f"Analyzing {terrain.upper()}")
    print("="*50)

    df = pd.read_csv(file)

    # -------------------------------------------------
    # RMS VALUES
    # -------------------------------------------------

    rms_ax = np.sqrt(np.mean(df['accel_x_g']**2))
    rms_ay = np.sqrt(np.mean(df['accel_y_g']**2))
    rms_az = np.sqrt(np.mean(df['accel_z_g']**2))

    rms_force = np.sqrt(np.mean(df['force_g']**2))

    # -------------------------------------------------
    # TOTAL VIBRATION MAGNITUDE
    # -------------------------------------------------

    vibration = np.sqrt(
        df['accel_x_g']**2 +
        df['accel_y_g']**2 +
        df['accel_z_g']**2
    )

    mean_vibration = vibration.mean()
    max_vibration = vibration.max()

    # -------------------------------------------------
    # SHOCK DETECTION
    # -------------------------------------------------

    shock_threshold = vibration.mean() + 3*vibration.std()

    shock_count = np.sum(
        vibration > shock_threshold
    )

    # -------------------------------------------------
    # ROUGHNESS INDEX
    # -------------------------------------------------

    roughness_index = (
        vibration.std()
        *
        vibration.max()
    )

    # -------------------------------------------------
    # COMFORT INDEX
    # -------------------------------------------------

    comfort_index = np.sqrt(
        np.mean(
            (df['accel_z_g'] - 1)**2
        )
    )

    # -------------------------------------------------
    # SLIP INDEX
    # -------------------------------------------------

    slip_index = np.sqrt(
        np.mean(
            df['accel_y_g']**2
        )
    )

    # -------------------------------------------------
    # FORCE STABILITY
    # -------------------------------------------------

    force_mean = df['force_g'].mean()

    force_std = df['force_g'].std()

    force_cv = force_std / force_mean

    peak_force = df['force_g'].max()

    # -------------------------------------------------
    # SAVE RESULTS
    # -------------------------------------------------

    summary_results[terrain] = {
        "RMS Force": rms_force,
        "RMS Ax": rms_ax,
        "RMS Ay": rms_ay,
        "RMS Az": rms_az,
        "Mean Vibration": mean_vibration,
        "Max Vibration": max_vibration,
        "Shock Count": shock_count,
        "Roughness Index": roughness_index,
        "Comfort Index": comfort_index,
        "Slip Index": slip_index,
        "Force CV": force_cv,
        "Peak Force": peak_force
    }

    # =================================================
    # VIBRATION PLOT
    # =================================================

    plt.figure(figsize=(10,4))

    plt.plot(vibration)

    plt.title(
        f'{terrain.upper()} Terrain - Vibration Magnitude'
    )

    plt.xlabel('Sample')

    plt.ylabel('Acceleration Magnitude (g)')

    plt.grid()

    plt.show()

    # =================================================
    # FORCE PLOT
    # =================================================

    plt.figure(figsize=(10,4))

    plt.plot(df['force_g'])

    plt.title(
        f'{terrain.upper()} Terrain - Force'
    )

    plt.xlabel('Sample')

    plt.ylabel('Force (g)')

    plt.grid()

    plt.show()

    # =================================================
    # FFT ANALYSIS
    # =================================================

    signal = df['accel_z_g'].values

    N = len(signal)

    sample_rate = 50

    dt = 1/sample_rate

    yf = fft(signal)

    xf = fftfreq(N, dt)

    plt.figure(figsize=(10,4))

    plt.plot(
        xf[:N//2],
        np.abs(yf[:N//2])
    )

    plt.title(
        f'{terrain.upper()} FFT Spectrum'
    )

    plt.xlabel('Frequency (Hz)')

    plt.ylabel('Amplitude')

    plt.grid()

    plt.show()

    # =================================================
    # PSD ANALYSIS
    # =================================================

    f, psd = welch(
        signal,
        fs=sample_rate
    )

    plt.figure(figsize=(10,4))

    plt.semilogy(f, psd)

    plt.title(
        f'{terrain.upper()} Power Spectral Density'
    )

    plt.xlabel('Frequency (Hz)')

    plt.ylabel('PSD')

    plt.grid()

    plt.show()

# =====================================================
# SUMMARY TABLE
# =====================================================

summary_df = pd.DataFrame(summary_results).T

print("\n")
print("="*80)
print("FINAL TERRAIN COMPARISON")
print("="*80)

print(summary_df.round(4))

# =====================================================
# BAR CHARTS
# =====================================================

metrics = [
    "RMS Force",
    "Roughness Index",
    "Comfort Index",
    "Slip Index",
    "Shock Count"
]

for metric in metrics:

    plt.figure(figsize=(7,4))

    plt.bar(
        summary_df.index,
        summary_df[metric]
    )

    plt.title(metric)

    plt.ylabel(metric)

    plt.grid(axis='y')

    plt.tight_layout()

    plt.show()

# =====================================================
# TERRAIN PERFORMANCE RADAR ALTERNATIVE
# =====================================================

plt.figure(figsize=(8,5))

plt.scatter(
    summary_df["Mean Vibration"],
    summary_df["Force CV"],
    s=200
)

for terrain in summary_df.index:

    plt.annotate(
        terrain,
        (
            summary_df.loc[terrain, "Mean Vibration"],
            summary_df.loc[terrain, "Force CV"]
        )
    )

plt.xlabel("Mean Vibration")

plt.ylabel("Force Coefficient of Variation")

plt.title("Terrain Comparison")

plt.grid()

plt.show()

print("\nAnalysis Complete.")