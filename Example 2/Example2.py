from integrate_module import integrate_rk4, basline
import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt


'''
EXEMPLE 2

    Integrate an accelerogram derived from a dynamic analysis of a moored ship.
    This accelerogram relates to the ship's sway motion.
    The initial conditions for displacement and velocity are non-zero and taken from the dynamic analysis of the ship.
    The sampling rate is the same as the dynamic analysis, set at 1/100 of a second, with a total duration of 340 seconds.
    
    The integration is performed using the fourth-order Runge-Kutta algorithm.

    Input:
        A txt file containing time in the first column and acceleration in m/s2 in the second column.
        The separator to be used is ";" (semicolon).
    Output:
        The comparative graphical representation of acceleration, velocity, and displacement.
        Save a CSV file containing the history of displacements.
'''

# ===========================================================================================
# INITIAL SETTINGS:

# Define the file path containing the accelerogram
file_path = 'vessel_accelerogram.txt'

# Set the initial conditions:

y0 = 0.021491332862909 # Displacement
v0 = 0.0176782812923192 # Velocity

# Set the desired time step for the output

dt = 0.01

# ===========================================================================================

# Read the accelerogram from a txt file:
with open(file_path, "r") as f:
    data = np.loadtxt(f, skiprows=0, delimiter=";")

# Split the data into time and acceleration:
t = data[:, 0]
a = data[:, 1]

# Create an interpolated time vector:
t_interp = np.arange(t[0], t[-1]+dt, dt)

# Create an interpolator object:
interpolator = scipy.interpolate.interp1d(t, a, kind="linear")

# Interpolate the acceleration for the sampled time interval dt:
a_interp = interpolator(t_interp)

# Numerical integration using the RK4 method at a specific time step:
y, v = integrate_rk4(a_interp, t_interp, dt, y0, v0)

# Baseline Correction
scaled_v = basline(v, t_interp, v0)
scaled_y = basline(y, t_interp, y0)

# Combine time and displacement data
data_to_save = np.column_stack((t_interp, scaled_y))

# Write results to a CSV file with time and displacement
output_file = 'displacement_record.csv'
np.savetxt(output_file, data_to_save, delimiter=';', header='Time;Displacement', comments='')

# Visual representation
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))

# Accelerogram graph
ax1.plot(t, a, color='red', linewidth=1, linestyle='-', label='Accelerogram')
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Acceleration [$m/s^{2}$]')
ax1.legend()
ax1.grid(True)

# velocity over time graph with the new interval
ax2.plot(t_interp, scaled_v, color='blue', linewidth=1, linestyle='-', label='Velocity')
ax2.set_xlabel('Time [s]')
ax2.set_ylabel('Velocity [m/s]')
ax2.legend()
ax2.grid(True)

# Displacement over time graph with the new interval
ax3.plot(t_interp, scaled_y, color='black', linewidth=1, linestyle='-', label='Displacement')
ax3.set_xlabel('Time [s]')
ax3.set_ylabel('Displacement [m]')
ax3.legend()
ax3.grid(True)

plt.tight_layout()
plt.show()