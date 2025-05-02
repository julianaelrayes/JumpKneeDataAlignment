# JumpKneeDataAlignment

This repository contains a collection of MATLAB and Python scripts developed for the project *Drop Vertical Jumps to Assess Risk for Knee Degeneration and Future Total Knee Arthroplasty*. The goal of this work is to synchronize surface electromyography (EMG) data with 3D motion capture recordings collected during drop vertical jump (DVJ) trials. By aligning muscle activation patterns with joint movement data, the project supports detailed analysis of knee biomechanics. This synchronization is a critical step toward identifying movement-related risk factors that may contribute to knee degeneration and the eventual need for surgical intervention.

## Repository Structure

```
JumpKneeDataAlignment/
├── Final Deliverables.pdf       # Full project report  
├── Final Presentation.pptx      # Final presentation slides  
├── README.md                    # This file  
├── OutcomeFiles/  
│   ├── EMG_Plots/               # PNG images generated from EMG CSV files  
│   └── EMG_utc_hpf.csv          # Extracted UTC start times from EMG .hpf files  
└── Scripts/  
    ├── align_all_subject_trials.py  # Aligns EMG and motion files by time  
    ├── emg_viewer.mlx               # Interactive MATLAB viewer for EMG signal  
    ├── extract_utc.py               # Extracts UTC timestamps from EMG .hpf files  
    └── plot_emg_batch.m             # Batch plots EMG CSV files for visual inspection  
```

## File Descriptions

- **Final Deliverables.pdf** – Comprehensive project report detailing objectives, methodology, results, and team contributions.  
- **plot_emg_batch.m** – MATLAB script that processes a batch of EMG CSV files to generate high-resolution plots for visual inspection.  
- **emg_viewer.mlx** – MATLAB live script for detailed examination of individual EMG signals, including zoomed-in views.  
- **extract_utc.py** – Python script that extracts UTC start times from EMG `.hpf` files and compiles them into a CSV file.  
- **align_all_subject_trials.py** – Python script that aligns EMG data with 3D motion capture data using UTC timestamps.  
- **EMG/CSV/** – Directory containing raw EMG data in CSV format.  
- **EMG/Plots/** – Directory where the `plot_emg_batch.m` script saves generated EMG plots.  
- **EMG_utc_hpf.csv** – CSV with UTC timestamps extracted from `.hpf` files.  
- **Raw Files/EMG/EMG_hpf_files/** – Directory containing raw `.hpf` EMG files.  
- **aligned_subject_trials/** – Output folder for aligned EMG and motion data.  

## Usage Instructions

1. **Extract UTC Timestamps**  
   - Run `extract_utc.py` to extract UTC times from `.hpf` files.  
   - Output: `EMG_utc_hpf.csv`

2. **Generate EMG Plots**  
   - Run `plot_emg_batch.m` to generate plots from EMG CSVs.  
   - Output: Saved in `EMG_Plots/`

3. **View Individual EMG Signals**  
   - Open `emg_viewer.mlx` in MATLAB for detailed inspection.

4. **Align EMG and Motion Data**  
   - Run `align_all_subject_trials.py` to align EMG with motion capture data.  
   - Output: Saved in `aligned_subject_trials/`

## Development Environment

- MATLAB R2023b  
- Python 3.11  