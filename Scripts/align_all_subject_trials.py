import os
import pandas as pd
from datetime import datetime

def align_all_subject_trials(emg_folder, emg_utc_file, tak_utc_file, output_folder="aligned_subject_trials"):
    os.makedirs(output_folder, exist_ok=True)

    # Load UTC reference data
    emg_utc_df = pd.read_csv(emg_utc_file)
    tak_df = pd.read_csv(tak_utc_file)

    # Loop through each EMG file in the folder
    for file in os.listdir(emg_folder):
        if not file.endswith(".csv"):
            continue

        subject_id = file.split("_")[1].split("-")[0]  # Extract '019' from FM_019...
        full_subject_id = f"FM_{subject_id}"

        try:
            # Get EMG start time from .hpf UTC CSV
            emg_start_str = emg_utc_df[emg_utc_df["File Name"].str.contains(full_subject_id, na=False)]["Start Time"].iloc[0][:26]
            emg_start = datetime.strptime(emg_start_str, "%Y/%m/%d %H:%M:%S.%f")

            # Filter motion trials for this subject from .tak UTC CSV
            subject_trials = tak_df[tak_df["Filename"].str.contains(full_subject_id, na=False)]

            # Load full EMG file
            emg_path = os.path.join(emg_folder, file)
            emg_df = pd.read_csv(emg_path)
            sampling_rate = 156
            time_step = 1 / sampling_rate  # ≈ 0.006410256

            # Output folder per subject
            subject_out_dir = os.path.join(output_folder, full_subject_id)
            os.makedirs(subject_out_dir, exist_ok=True)

            # Loop through each trial (.tak row)
            for _, row in subject_trials.iterrows():
                trial_name = row["Filename"].split(".")[0]
                tak_time_str = row["EasternTime"]
                num_frames = int(row["Frames"]) if "Frames" in row else 280

                try:
                    tak_time = datetime.strptime(tak_time_str, "%m/%d/%Y %H:%M")
                    offset_sec = (tak_time - emg_start).total_seconds()
                    start_index = int(offset_sec * sampling_rate)

                    # Extract EMG segment for this trial
                    segment_df = emg_df.iloc[start_index:start_index + num_frames].copy()

                    # Drop any existing time columns like Time_sec or X [s]
                    for col in ["Time_sec", "X [s]"]:
                        if col in segment_df.columns:
                            segment_df.drop(columns=[col], inplace=True)

                    # Reset index and insert X [s] column: 0.000, 0.006, 0.012, ...
                    segment_df.reset_index(drop=True, inplace=True)
                    segment_df.insert(0, "X [s]", [round(i * 0.006, 3) for i in range(len(segment_df))])

                    # Save aligned trial CSV
                    output_path = os.path.join(subject_out_dir, f"{trial_name}.csv")
                    segment_df.to_csv(output_path, index=False)
                    print(f"✅ {trial_name} saved to {subject_out_dir}")
                except Exception as trial_error:
                    print(f"⚠️ Skipped trial {trial_name}: {trial_error}")

        except Exception as subject_error:
            print(f"❌ Failed to align subject {full_subject_id}: {subject_error}")

if __name__ == "__main__":
    align_all_subject_trials(
        emg_folder="C:/Users/Eswar/OneDrive/Desktop/EMG_data/downsampled_156hz",
        emg_utc_file="C:/Users/Eswar/OneDrive/Desktop/EMG_data/UTC/EMG_utc_hpf.csv",
        tak_utc_file="C:/Users/Eswar/OneDrive/Desktop/EMG_data/UTC/File_UTC_UNIX_Eastern_Timestamps.csv"
    )
