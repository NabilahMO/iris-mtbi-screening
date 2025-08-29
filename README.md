# Iris-mTBI Screening Tool

A biomedical tool that simulates and analyses eye-tracking data to detect signs of mild traumatic brain injury (mTBI), based on variability in the inter-iris distance over time.

Subtle changes in pupil stability can be early indicators of concussion. This tool simulates a computational approach for low-cost, rapid detection using only eye-tracking data—a concept with major implications for athlete safety, military screening, and digital health.

## What This Project Does

1.  **Simulates** eye-tracking data for two groups: a healthy control group and a group with simulated mTBI characteristics.
2.  **Calculates** the normalised inter-iris distance for each frame of the simulated data.
3.  **Measures** the variability (standard deviation) of this signal over time.
4.  **Flags** possible mTBI using a decision threshold based on the calculated variability.
5.  **Visualizes** the distributions of the two samples to highlight the difference in signal variability.

Built by: Nabilah Muri-Okunola