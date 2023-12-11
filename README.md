# Displacement Integration for Dynamic Analysis

![alt text](https://badgen.net/badge/release/v.1.0/green?) ![alt text](https://badgen.net/badge/code/Python/blue?) ![alt text](https://badgen.net/badge/license/GPL-3.0/orange?)

This Python script allows for the integration of an accelerogram to obtain the temporal history of displacement.

## Table of contents
* [Description](#description)
* [Usage](#usage)
* [Exemples](#exemples)

  
## Description

In dynamic structural analyses, a very dense sampling of the accelerogram is typically used, in the order of hundredths of a second. When performing a dynamic analysis using a temporal history of displacements, the sampling interval must be denser. This script automatically generates a temporal history of displacements with a sampling interval one-fifth of that of the input accelerogram. It is also possible to specify initial boundary conditions in terms of displacement and velocity.

Temporal displacement histories are used for various purposes in structural engineering, such as seismic analyses that consider the effect of seismic motion propagation, typically in bridges. Other examples include analyses of moving components within the structure.

Here are two practical examples:

Example 1: Integrating an accelerogram derived from a dynamic analysis of a moored ship subjected to wind and waves, performed using Orcaflex. The displacement history derived from Orcaflex is compared to that derived from double integration executed with the script.

Example 2: Integrating a seismic accelerogram sampled at 1/100 seconds into displacement at 1/500 seconds.

## Usage

Txt

## Examples

### Exemple 1


### Exemple 2
