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

### Exemple 1


### Exemple 2
