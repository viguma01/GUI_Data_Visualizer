# User Guide for IoT Data Generator

## Getting Started
- **Launch the Application**: Run the `wx_data_visualizer.py` script to start the application. This will open the main window of the IoT Data Generator.

## Generating IoT Data
- **Generate Data**: Navigate to the `File` menu and select `&Generate IoT`. This will generate a set of random IoT data consisting of personal and environmental information.
- **View Status**: The status bar at the bottom of the window will display 'Generating IoT Data...' while the data is being generated and will switch back to 'Ready' once the process is complete.

## Saving Data
- **Save as JSON**: To save the generated data as a JSON file, go to `File` > `&Save JSON`. Choose your desired save location and file name in the dialog box that appears.
- **Save as CSV**: To save the data as a CSV file, select `File` > `Save &CSV`. Just like with JSON, choose the save location and file name in the dialog box.

## Viewing and Analyzing Data
- **Show Statistics**: To view the generated data in a tabular format, click on `&Descriptive` under the `Statistics` menu.
- **Plotting Data**:
  - **Plot A (Histogram of Outside Temperature)**: Navigate to `Statistics` > `Plot &A` to view a histogram of the outside temperature data.
  - **Plot B (Room Temperature Over Time)**: Select `Statistics` > `Plot &B` to generate a line plot showing room temperature changes over time.
  - **Plot C (Scatter Plot of Temperature vs. Humidity)**: Choose `Statistics` > `Plot &C` to display a scatter plot comparing outside temperature with humidity.

## Exiting the Application
- Close the application window or select `Exit` from the `File` menu to close the IoT Data Generator.
This Markdown guide is structured with headers, bullet poin