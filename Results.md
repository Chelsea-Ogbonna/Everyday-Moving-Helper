# Results and Discussion

## Overview

This experiment investigated the effect of terrain type on robotic motion using two sensing modalities: a force sensor and an MPU6050 inertial measurement unit (IMU). The force sensor measured changes in wheel-ground interaction forces, while the MPU6050 measured the resulting accelerations experienced by the robot body. Three terrain conditions were evaluated: smooth flooring, rough terrain, and carpet.
The combined sensor data provide insight into both the external forces acting on the robot and the robot's dynamic response to those forces. While the force sensor captures interactions occurring at the wheel-terrain interface, the MPU6050 quantifies how these interactions propagate through the robot structure as vibration and motion.

## Force Sensor Analysis
The RMS force values remained relatively similar across all terrain conditions, ranging from approximately 947.6 g to 952.9 g. This result indicates that the average load experienced by the robot remained nearly constant throughout testing.

Terrain | RMS Force (g)

Smooth  | 947.57

Rough   | 950.77

Carpet  | 952.87

The similarity in RMS force values is expected because the robot's mass does not change between trials. Consequently, the average force exerted on the terrain remains relatively constant regardless of surface type.
Although the average force remained stable, the force sensor revealed important differences when examining force variability and peak force measurements. Rough terrain produced the highest peak force (1068.3 g), followed by carpet (1050.9 g), while smooth terrain generated the lowest peak force (978.9 g).
These larger force peaks suggest that rough terrain introduces sudden loading events as the wheels encounter bumps, height variations, and discontinuities. Each impact causes a temporary increase in the normal force experienced by the wheel. Carpet also generated elevated peak forces, likely because the wheel periodically compresses and releases the carpet fibers, creating localized force fluctuations.
Smooth terrain generated the lowest peak force because the wheel maintains a relatively consistent contact condition throughout motion, minimizing sudden changes in loading.

## IMU Analysis
While the force sensor measured interactions at the ground contact point, the MPU6050 measured how these interactions affected the robot body.

### Longitudinal Vibrations (X-Axis)
Terrain | RMS Ax (g)

Smooth  | 0.0225

Rough   | 0.1226

Carpet  | 0.0519

The rough terrain generated the highest longitudinal acceleration, more than five times larger than the smooth terrain. This indicates that rough terrain causes significant forward-backward disturbances as the wheels repeatedly encounter obstacles and uneven surfaces.
Carpet generated moderate longitudinal accelerations. The compliant nature of the carpet likely absorbs some impact energy while simultaneously introducing rolling resistance that creates additional vibration.
Smooth terrain produced minimal longitudinal vibration, indicating stable motion and consistent wheel contact.

### Lateral Vibrations (Y-Axis)

Terrain | RMS Ay (g)

Smooth  | 0.0298

Rough   | 0.1076

Carpet  | 0.0551

A similar pattern was observed in the lateral direction. Rough terrain generated the largest side-to-side accelerations, suggesting uneven loading between wheels and increased directional instability.
When a wheel encounters a localized obstacle, the robot experiences a momentary shift in load distribution. These load redistributions manifest as lateral accelerations detected by the IMU. The elevated RMS Ay value on rough terrain therefore indicates greater instability and reduced directional smoothness.
Carpet again produced intermediate values, while smooth terrain exhibited the most stable behavior.

### Vertical Vibrations (Z-Axis)
Terrain | RMS Az (g)

Smooth  | 1.0016

Rough   | 1.0180

Carpet  | 1.0029

The vertical acceleration remained near 1 g for all terrains because gravity dominates the measurement. However, the slightly elevated RMS Az value observed on rough terrain indicates increased vertical oscillations caused by wheel impacts and surface height variations.
These oscillations represent the transfer of energy from terrain irregularities into the robot chassis.

## Relationship Between Force and Acceleration
The most significant finding of this experiment is the relationship between the force sensor measurements and the IMU measurements.
The force sensor indicates that rough terrain creates larger transient loading events. These loading events originate at the wheel-terrain interface and represent the mechanical disturbances introduced by the environment.
The MPU6050 demonstrates that these disturbances are subsequently transmitted into the robot body as vibration and acceleration.
This relationship can be observed by comparing peak force and RMS acceleration values:
Rough terrain produced the highest peak force and the highest acceleration values.
Smooth terrain produced the lowest peak force and the lowest acceleration values.
Carpet produced intermediate values for both metrics.
The agreement between the two sensors suggests that the observed vibrations are directly linked to wheel-ground interactions rather than measurement noise.
In essence, the force sensor identifies the source of the disturbance, while the MPU6050 measures the effect of that disturbance on the robot.

## Slip and Stability Analysis
The slip index was highest on rough terrain and lowest on smooth terrain.

Terrain | Slip Index

Smooth  | 0.0298

Rough   | 0.1076

Carpet  | 0.0551

Higher slip index values indicate greater deviations from ideal motion and increased instability. Rough terrain likely caused micro-slip events as wheels traversed uneven surfaces, requiring continual corrections in motion.
These corrections contribute to the elevated lateral accelerations observed by the MPU6050 and further support the conclusion that rough terrain produces the most challenging operating environment.
Carpet exhibited moderate slip behavior because the deformable surface alters wheel contact conditions. Although carpet absorbs some vibration energy, its compliant structure introduces additional rolling resistance and small-scale force fluctuations.

## Force Variability and Dynamic Loading
Force coefficient of variation (Force CV) provides a measure of loading consistency.

Terrain | Force CV

Smooth  | 0.0092

Rough   | 0.0612

Carpet  | 0.0284

The rough terrain exhibited nearly seven times more force variability than smooth terrain. This indicates that wheel loading changed frequently as the robot traversed the surface.
These force fluctuations are reflected in the acceleration measurements. Greater variability in wheel loading leads to greater variability in chassis motion, explaining the elevated vibration levels recorded by the MPU6050.
The strong correlation between force variability and acceleration magnitude demonstrates that terrain roughness affects both the contact mechanics of the wheels and the overall stability of the robot.
Engineering Implications
From an engineering perspective, rough terrain imposes the greatest mechanical demands on the robotic system. Increased force variability, larger impact loads, and elevated accelerations can contribute to sensor noise, decreased localization accuracy, higher power consumption, and accelerated mechanical wear.
The smooth terrain provides the most favorable operating conditions by minimizing vibration and maintaining consistent wheel-ground contact. Carpet represents an intermediate condition in which energy absorption reduces some impacts, but the compliant surface introduces additional resistance and moderate instability.
The combination of force sensing and inertial sensing provides a comprehensive characterization of terrain effects. The force sensor captures the interaction between the robot and the environment, while the MPU6050 quantifies the resulting dynamic response of the robot. Together, these measurements provide a more complete understanding of terrain-induced disturbances than either sensor could provide independently.

