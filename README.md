# Displacement Integration for Dynamic Analysis

![alt text](https://badgen.net/badge/release/v.1.0/green?) ![alt text](https://badgen.net/badge/code/Python/blue?) ![alt text](https://badgen.net/badge/license/GPL-3.0/orange?)

This Python script allows for the integration of an accelerogram to obtain the temporal history of displacement.

## Table of contents
* [Description](#description)
* [Usage](#usage)
* [Exemples](#exemples)

  
## Description

In dynamic structural analyses, a very dense sampling of the accelerogram is typically used, in the order of hundredths of a second. When performing a dynamic analysis using a temporal history of displacements, the sampling interval must be denser. This script automatically generates a temporal history of displacements with a user defned sampling interval.
It is also possible to specify initial boundary conditions in terms of displacement and velocity.

This script allows performing integration using two methods:
 * Wilson algorithm [See the CSI Wiki](https://wiki.csiamerica.com/display/kb/Displacement+time-history+record)
 * Fourth-order Runge-Kutta algorithm [See the Wiki page](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods)

Additionally, it performs a linear baseline correction of the velocity and displacement output.

Temporal displacement histories are used for various purposes in structural engineering, such as seismic analyses that consider the effect of seismic motion propagation, typically in bridges. Other examples include analyses of moving components within the structure.

Here are two practical examples:

Example 1: Integrating a seismic accelerogram sampled at 1/100 seconds into displacement at 1/1000 seconds.

Example 2: Integrating an accelerogram derived from a dynamic analysis of a moored ship subjected to wind and waves, performed using Orcaflex. The displacement history derived from Orcaflex is compared to that derived from double integration executed with the script.

## Usage

The script consists of a main module named _integrate_module.py_ containing functions for performing double integration. The functions included are:

 * integrate_wilson: Integrates an accelerogram using the Wilson method to determine the history of velocity and displacements based on boundary conditions.
 * integrate_rk4: Integrates an accelerogram using the fourth-order Runge-Kutta method to determine the history of velocity and displacements based on boundary conditions.
 * baseline: Performs a baseline function that linearly corrects the passed function while preserving the initial conditions.

To use these functions, it's necessary to import them into the script performing the computation, for example:
```
from integrate_module import integrate_wilson, baseline
```
Two examples have been developed to test the script, which also serve as a reference for how to use it.

## Examples

### Example 1

The first example involves the integration of a seismic accelerogram spectrum-compatible generated using the Simqke algorithm developed at Berkeley. The accelerogram has a sampling interval of 1/100 of a second and a total duration of 30 seconds.

Subsequently, the integration is performed using the Wilson algorithm with an integration step of 1/1000 seconds. The result is compared with an integration executed through the finite element analysis software SAP2000 from CSI.

This is a classic example of creating a temporal history of displacements to perform a finite element dynamic analysis.

This example is set up in the script _Example1.py_.

At the beginning of the file _Exemple1.py_, the necessary functions are imported:
```
from integrate_module import integrate_wilson, baseline
```
And the parameters for integration are set:
```
Define the file path containing the accelerogram
file_path = 'seismic_accelerogram.txt'

Set the initial conditions:
y0 = 0  # Displacement
v0 = 0  # Velocity

Set the desired time step for the output
dt = 0.001
```

The output of the script is shown in the following figure, the numerical values of the temporal displacement history are saved in the CSV file named _displacement_record.csv_.

![alt text](https://github.com/paolo-hub/Displacement-Integration-for-Dynamic-Analysis/blob/main/Example%201/Example1-Graphical%20output.jpg?raw=true)

The displacement history is then compared with the one determined using the finite element software SAP2000.
The integration performed through SAP2000 has the same integration step of 1/1000, and the integration algorithm used is the Newmark method.
The result of the comparison is shown in the following figure.

![alt text](https://raw.githubusercontent.com/paolo-hub/Displacement-Integration-for-Dynamic-Analysis/main/Example%201/Example1-SAP2000%20Comparison.jpg)

To assess the discrepancy between the two temporal displacement histories, the root-mean-square error (RMSE) was calculated, resulting in 0.014%, indicating an excellent agreement between the two solutions.

### Example 2

This second example demonstrates the integration of an accelerogram derived from a dynamic analysis of a moored ship subjected to wind and waves, performed using Orcaflex.

It considers an acceleration history due to the sway of the ship.
For this simulation, both the acceleration and displacement histories are available, sampled at 1/100 seconds and lasting 340 seconds.

The displacement history obtained from Orcaflex is compared to that derived from double integration executed with the script.

The temporal history presents an initial condition of acceleration, velocity, and displacement that are not equal to zero.
The accelerogram is passed to the script as is, and initial conditions of velocity and displacement are set.
The time step for the displacement history remains the same as that of the accelerogram, allowing for a more precise comparison with the displacement history derived from the Orcaflex analysis.
For this example, the Runge-Kutta integration algorithm is used.

This example is set up in the script _Example2.py_.

At the beginning of the file _Exemple2.py_, the necessary functions are imported:
```
from integrate_module import integrate_rk4, baseline
```
And the parameters for integration are set:
```
Define the file path containing the accelerogram
file_path = 'vessel_accelerogram.txt'

Set the initial conditions:
y0 = 2  # Displacement
v0 = 2  # Velocity

Set the desired time step for the output
dt = 0.01
```