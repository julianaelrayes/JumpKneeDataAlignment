import os
import re

def extract_first_start_time(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Find the first StartTime in the file
    start_time_match = re.search(r'<StartTime>(.*?)</StartTime>', content)
    return start_time_match.group(1) if start_time_match else 'Not found'

# Folder with .hpf files
folder_path = '/Users/julianaelrayes/Library/Mobile Documents/com~apple~CloudDocs/University/Spring 2025/Smart & Connected Health/Project/Raw Files/EMG_hpf_files'
hpf_files = [f for f in os.listdir(folder_path) if f.endswith('.hpf')]

# Collect filenam and start time pairs
results = []
for file in hpf_files:
    full_path = os.path.join(folder_path, file)
    try:
        start_time = extract_first_start_time(full_path)
        results.append((file, start_time))
    except Exception as e:
        results.append((file, f'Error: {e}'))

# Save to CSV
output_path = os.path.join(folder_path, 'simplified_utc_times.csv')
with open(output_path, 'w') as f:
    f.write("File Name,Start Time\n")
    for row in results:
        f.write(','.join(row) + '\n')

print(f"Results saved to:\n{output_path}")

