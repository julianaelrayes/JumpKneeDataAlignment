% EMG Batch Plotting Script
% Loops through all CSV files in a folder,
% extracts Right and Left Vastus Lateralis EMG signals,
% creates a new 'Plots' folder, and saves all figures as PNGs.

% Path to the folder where the CSV files are located
% This can be changed to be able to run the code in another machine
folderPath = '/Users/julianaelrayes/Library/Mobile Documents/com~apple~CloudDocs/University/Spring 2025/Smart & Connected Health/Project/EMG/CSV';
filePattern = fullfile(folderPath, '*.csv');
files = dir(filePattern);

% Creates a new 'Plots' folder next to the CSV folder to store the images
plotsFolder = fullfile(folderPath, '..', 'Plots');
if ~exist(plotsFolder, 'dir')
    mkdir(plotsFolder);  % Create the folder if it doesn't already exist
end

% Loop through each CSV file
for k = 1:length(files)
    filename = fullfile(folderPath, files(k).name);
    disp(['Processing: ', files(k).name]);

    try
        % Load the table
        data = readtable(filename, 'NumHeaderLines', 11, 'VariableNamingRule', 'preserve');
        headers = data.Properties.VariableNames;  % Get the column names

        time_r_col = "X[s]";  % Time column for Right leg
        emg_r_col_options = ["R VASTUS LATERALIS (1): dEMG.A 1", "R VASTUS LATERALIS (3): dEMG.A 3"];
        time_l_col = "X[s]_4";  % Time column for Left leg
        emg_l_col_options = ["L VASTUS LATERALIS (2): dEMG.A 2", "L VASTUS LATERALIS (4): dEMG.A 4"];

        % Finds which version of the column is present in this file
        emg_r_col = emg_r_col_options(ismember(emg_r_col_options, headers));
        emg_l_col = emg_l_col_options(ismember(emg_l_col_options, headers));

        % Skip this file if either column is missing
        if isempty(emg_r_col) || isempty(emg_l_col)
            warning(['Could not find EMG columns in: ', files(k).name]);
            continue;
        end

        % Extract the data columns from the table
        time_r = data.(time_r_col);  % Time for Right leg
        emg_r = data.(emg_r_col{1});  % EMG signal for Right VL

        time_l = data.(time_l_col);  % Time for Left leg
        emg_l = data.(emg_l_col{1});  % EMG signal for Left VL

        % Create an invisible large high-resolution figure
        fig = figure('Visible', 'off', 'Name', files(k).name, 'NumberTitle', 'off', ...
                     'Units', 'pixels', 'Position', [100, 100, 1200, 600]);

        % Plot Right VL EMG
        subplot(2,1,1);
        plot(time_r, emg_r, 'LineWidth', 0.5);
        title(['Right VL EMG - ', files(k).name], 'Interpreter', 'none');
        xlabel('Time (s)');
        ylabel('Amplitude (V)');
        xlim([min(time_r), max(time_r)]);
        grid on;

        % Plot Left VL EMG
        subplot(2,1,2);
        plot(time_l, emg_l, 'LineWidth', 0.5); 
        title(['Left VL EMG - ', files(k).name], 'Interpreter', 'none');
        xlabel('Time (s)');
        ylabel('Amplitude (V)');
        xlim([min(time_l), max(time_l)])
        grid on;

        sgtitle('EMG Signals from Vastus Lateralis Muscles');

        % Save figure as PNG
        savePath = fullfile(plotsFolder, [files(k).name, '_emg_plot.png']);
        exportgraphics(fig, savePath, 'Resolution', 300);
        close(fig);

    catch ME
        % If anything goes wrong...
        warning(['Error processing file: ', files(k).name]);
        disp(getReport(ME));
    end

    disp('---------------------------');
end