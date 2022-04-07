# Garmin CSV Reformatter

This project is intended to be used in combination with the FitCSVTool released by Garmin, available as part of the Garmin SDK (https://developer.garmin.com/fit/fitcsvtool/).
The Garmin FitCSVTool converts an activity from their `.fit` formatted files to `.csv`. Which is a better - but still far from readable format - given the loss-less representation the tool outputs.
This project reformats the output-CSV from the FitCSVTool to be more human readable, removing all unneccesary and non relevant data, leaving just the activity metrics in a simple `.csv` format.
See the `sample_input/..` directory for an example of what the original `.fit` from Garmin looks like, as well as what the format of the output from the FitCSVTool looks like.

### How to use
1. Locate a `.fit` file from an activity on your Garmin device
2. Download the FitCSVTool: https://developer.garmin.com/fit/fitcsvtool/
3. Format your `.fit` file using the FitCSVTool
4. Generate a reformatted CSV using the following command in the terminal:

    `reformat_garmin_csv.py -i <inputpath> -o <outputpath>`

**Requires: Pandas & Python**

**Note:** Per default most Garmin devices are set to 'Smart' data recording, which means data isn't recorded every second. If you require consistent data in 1 second intervals go to the settings of your Garmin device: Settings > System > Data Recording, and select 'Every Second'.

### Sample Output
| timestamp [s] | position_lat [degrees] | position_long [degrees] | distance [m] | enhanced_speed [m/s] | enhanced_altitude [m] | heart_rate [bpm] | cadence [rpm] | temperature [C] | fractional_cadence [rpm] |
| ------------- | -------------------------- | --------------------------- | ------------ | -------------------- | --------------------- | ---------------- | ------------- | --------------- | ------------------------ |
| 0             | 55.74739946052432          | 12.55748150870204           | 0.0          | 1.596                | 13.6    | 88               | 60            | 27              | 0.0                      |
| 1             | 55.74740331619978          | 12.557498775422573          | 1.13         | 1.596                | 13.6    | 88               | 60            | 27              | 0.0                      |
| 2             | 55.747411865741014         | 12.557509420439601          | 2.28         | 1.614                | 13.6    | 88               | 60            | 27              | 0.0                      |
| 5             | 55.74747271835804          | 12.557492488995194          | 9.01         | 1.698                | 13.6    | 88               | 85            | 27              | 0.5                      |
| 12            | 55.747640021145344         | 12.557495925575495          | 27.71        | 2.631                | 13.4    | 92               | 80            | 27              | 0.5                      |
| 13            | 55.7476697769016           | 12.557490393519402          | 31.02        | 2.641                | 13.4    | 91               | 79            | 27              | 0.5                      |
| 15            | 55.74770716018975          | 12.557477317750454          | 35.26        | 2.781                | 13.4    | 96               | 79            | 27              | 0.5                      |
| 17            | 55.74775694869459          | 12.557455943897367          | 40.94        | 2.837                | 13.6    | 100              | 78            | 27              | 0.0                      |
