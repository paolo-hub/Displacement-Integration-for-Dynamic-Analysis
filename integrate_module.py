'''
INTEGRATE MODULE:
This module contains Python functions to perform the integration of an accelerogram into a time history of velocities and displacements.

The following is a list of the functions included in the module:   
    
    * integrate_wilson: Integrate an accelerogram using the Wilson method to determine the history of velocity and displacements
                        based on boundary conditions.
    * integrate_rk4: Integrate an accelerogram using the fourth-order Runge-Kutta method to determine the history of velocity and displacements
                     based on boundary conditions.
    * baseline: Performs a baseline function that linearly corrects the passed function while preserving the initial conditions.

'''

import numpy as np

def integrate_wilson(a, t, dt, y0, v0):
    '''
    Integrate an accelerogram using the Wilson method.
    Reference: https://wiki.csiamerica.com/display/kb/Displacement+time-history+record

    Args:
        * a: Accelerations.
        * t: Time.
        * y0: Initial displacement.
        * v0: Initial velocity.

    Returns:
    Temporal history of velocity and displacements.

    '''

    # Create empty arrays

    y = np.zeros_like(t)
    v = np.zeros_like(t)
    a_0 = np.zeros_like(t)
    a_1 = np.zeros_like(t)

    # Initialize initial displacement

    y[0] = y0

    # Initialize initial velocity

    v[0] = v0

    # Iterate through time points

    for i in range(len(t) - 1):

        # Compute the derivative of acceleration

        a_1[i + 1] = (a[i + 1] - a[i]) / dt

        # Calculate the acceleration at time t_i

        a_0[i + 1] = a[i] + a_1[i + 1] * dt

        # Calculate velocity at time t_i + dt

        v[i + 1] = v[i] + dt * a_0[i + 1] + ((dt**2)/2) * a_1[i + 1]

        # Calculate displacement at time t_i + dt

        y[i + 1] = y[i] + dt * v[i + 1] + ((dt**2)/2) * a_0[i + 1] + ((dt**3)/6) * a_1[i + 1]

    return y,v

  
def integrate_rk4(a, t, dt, y0, v0):

    '''
    Integrate an accelerogram using the fourth-order Runge-Kutta method.

    Args:
        * a: Accelerations.
        * t: Time.
        * y0: Initial displacement.
        * v0: Initial velocity.

    Returns:
    Temporal history of velocity and displacements.
    '''

    # Initialize initial displacement

    y = [y0]

    # Initialize initial velocity

    v = [v0]

    # Iterate through time points

    for i in range(len(t) - 1):
        k1 = a[i - 1]
        k2 = a[i - 1] + 0.5 * k1 * dt
        k3 = a[i - 1] + 0.5 * k2 * dt
        k4 = a[i] + k3 * dt

        v_n = v[-1] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4) * dt
        v.append(v_n)

        # Integrazione RK4 per lo spostamento
        k1 = v_n
        k2 = v_n + 0.5 * k1 * dt
        k3 = v_n + 0.5 * k2 * dt
        k4 = v_n + k3 * dt

        y_n = y[-1] + (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4) * dt
        y.append(y_n)        

    return y, v


def basline(s, t, s0): 
    '''
    Performs a baseline function that linearly corrects the passed function while preserving the initial conditions.

    Args:
    s: Temporal history to be scaled
    t: Time
    s0: Initial condition

    Returns:
    Scaled temporal history
    '''

    # The straight line passing through the first and last points
    m, q = np.polyfit([t[0], t[-1]], [s[0], s[-1]], 1)

    # Baseline Correction
    scaled_s = s - (m * t + q) + s0

    return scaled_s
