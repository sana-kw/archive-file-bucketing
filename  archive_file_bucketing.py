from collections import defaultdict
import json
import random


def generate_test_data(num_folders=500, target_files=50000):
    """Task 1: Generates >= 500 folder IDs and >= 50,000 JPEG filenames."""
    folders = []

    # Generate 500 unique folder identifiers (MS-011_a_b_c_d)
    a, b, c, d = 1, 1, 1, 1
    for _ in range(num_folders):
        folders.append(f"MS-011_{a}_{b}_{c}_{d}")
        d += 1
        if d > 10:
            d, c = 1, c + 1
        if c > 10:
            c, b = 1, b + 1
        if b > 10:
            b, a = 1, a + 1

    # Generate ~50,000 JPEG filenames mapped across the folders
    jpeg_files = []
    base_files_per_folder = target_files // num_folders

    for folder_id in folders:
        # Introduce slight natural variation in file count per folder
        count = base_files_per_folder + random.randint(-5, 5)
        for seq in range(1, count + 1):
            jpeg_files.append(f"{folder_id}_J_{seq:04d}.jpg")

    return folders, jpeg_files


def bucket_jpeg_files(folders, jpeg_files):
    """Task 2: Buckets JPEG files against their corresponding folder identifiers."""
    folder_set = set(folders)
    bucketed_data = defaultdict(list)
    unmatched_files = []

    for filename in jpeg_files:
        # Extract folder identifier prefix before the '_J_' sequence marker
        if "_J_" in filename:
            folder_id = filename.rsplit("_J_", 1)[0]
            if folder_id in folder_set:
                bucketed_data[folder_id].append(filename)
            else:
                unmatched_files.append(filename)
        else:
            unmatched_files.append(filename)

    return bucketed_data, unmatched_files


if __name__ == "__main__":
    # Task 1: Generate Dataset
    folders, jpeg_files = generate_test_data(
        num_folders=500, target_files=50000
    )
    print(f"Dataset Generated:")
    print(f" - Folders: {len(folders)}")
    print(f" - JPEG Files: {len(jpeg_files)}\n")

    # Task 2: Bucket Files
    bucketed_results, unmatched = bucket_jpeg_files(folders, jpeg_files)

    print(f"Bucketing Complete:")
    print(f" - Unique Folders Matched: {len(bucketed_results)}")
    print(
        f" - Total Files Bucketed: {sum(len(files) for files in bucketed_results.values())}"
    )
    print(f" - Unmatched Files: {len(unmatched)}\n")