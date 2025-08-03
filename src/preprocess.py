import csv
import random
import os

def generate_fake_landmark_data(label, num_samples=150, frames_per_sample=50, noise_level=0.5, base_path="data/raw"):
    """Generate and save fake iris landmark data for testing."""
    jitter = 0.5 if label == 'mtbi' else 0.1  # mTBI = more unstable

    os.makedirs(base_path, exist_ok=True)

    filepath = os.path.join(base_path, f"{label}_sample.csv")
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "left_mid_x", "left_mid_y",
            "left_inner_x", "left_inner_y",
            "left_outer_x", "left_outer_y",
            "right_mid_x", "right_mid_y",
            "right_inner_x", "right_inner_y",
            "right_outer_x", "right_outer_y"
        ])

        for _ in range(num_samples * frames_per_sample):
            # LEFT eye
            lm_x = 100 + random.gauss(0, jitter)
            lm_y = 100 + random.gauss(0, jitter)
            li_x = lm_x - 5 + random.gauss(0, 0.1)
            li_y = lm_y
            lo_x = lm_x + 5 + random.gauss(0, 0.1)
            lo_y = lm_y

            # RIGHT eye
            rm_x = 150 + random.gauss(0, jitter)
            rm_y = 100 + random.gauss(0, jitter)
            ri_x = rm_x - 5 + random.gauss(0, 0.1)
            ri_y = rm_y
            ro_x = rm_x + 5 + random.gauss(0, 0.1)
            ro_y = rm_y

            writer.writerow([
                lm_x, lm_y, li_x, li_y, lo_x, lo_y,
                rm_x, rm_y, ri_x, ri_y, ro_x, ro_y
            ])

    print(f"✅ Saved {num_samples} '{label}' samples ({frames_per_sample} frames each) to: {filepath}")

# Run it
generate_fake_landmark_data("control")
generate_fake_landmark_data("mtbi")
