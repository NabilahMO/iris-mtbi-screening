# Iris-mTBI Screening

A biomedical tool that simulates and analyses eye-tracking data to detect signs of mild traumatic brain injury (mTBI), based on variability in inter-iris distance over time.

Subtle changes in pupil stability can be early signs of concussion. This tool simulates and tests a computational approach for low-cost, fast detection using only eye-tracking data — a concept with major implications for athlete safety, military screening, and digital health.

## What This Project Does

1. Simulates pupil tracking data using anatomical iris landmarks
2. Calculates normalised inter-iris distance at each frame
3. Measures variability (standard deviation) of that signal
4. Flags possible mTBI using a decision threshold

## Project Structure

1. ``` src ```                  (Custom Python functions (features + data generation))
2. ``` notebooks```            (Jupyter notebook for full pipeline)
3. ```data/raw    ```        (Simulated eye-tracking data (control sample))
4. ```tests    ```          (Space for test files)
5. ```requirements.txt  ```   (Python dependencies)


## Example Output

Standard deviation: 0.0342
No mTBI detected


## Next Features

1. Compare variability between control and mTBI cases
2. Plot time series of normalised distance
3. Train basic ML classifier to replace threshold rule

Built by Nabilah Muri-Okunola
