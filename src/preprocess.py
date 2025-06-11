import csv
import random
import os

def generate_fake_landmark_data(num_rows=100, noise_level=0.5, label='control'):
    """Generate and save fake iris landmark data for testing."""
    data = []
    for _ in range(num_rows):
        jitter = noise_level if label == 'mTBI' else noise_level * 0.25

        # Left iris
        lm_x = 100 + random.gauss(0, jitter)
        lm_y = 100 + random.gauss(0, jitter)
        li_x = lm_x - 5 + random.gauss(0, 0.1)
        li_y = lm_y
        lo_x = lm_x + 5 + random.gauss(0, 0.1)
        lo_y = lm_y

        # Right iris
        rm_x = 150 + random.gauss(0, jitter)
        rm_y = 100 + random.gauss(0, jitter)
        ri_x = rm_x - 5 + random.gauss(0, 0.1)
        ri_y = rm_y
        ro_x = rm_x + 5 + random.gauss(0, 0.1)
        ro_y = rm_y

        data.append([
            lm_x, lm_y, li_x, li_y, lo_x, lo_y,
            rm_x, rm_y, ri_x, ri_y, ro_x, ro_y
        ])

    # Create folder if it doesn't exist
    os.makedirs("data/raw", exist_ok=True)

    # Save to CSV
    with open(f"data/raw/{label}_sample.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "left_mid_x", "left_mid_y",
            "left_inner_x", "left_inner_y",
            "left_outer_x", "left_outer_y",
            "right_mid_x", "right_mid_y",
            "right_inner_x", "right_inner_y",
            "right_outer_x", "right_outer_y"
        ])
        writer.writerows(data)

    print(f"✅ Saved simulated {label} data to 'data/raw/{label}_sample.csv'")
    