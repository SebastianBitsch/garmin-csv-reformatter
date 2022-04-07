# Garmin CSV Reformatter

This project is intended to be used in combination with the FitCSVTool released by Garmin, available as part of the Garmin SDK (https://developer.garmin.com/fit/fitcsvtool/).
The Garmin FitCSVTool converts an activity from their `.fit` formatted files to `.csv`. Which is a better - but still far from readable format - given the loss-less representation the tool outputs.
This project reformats the output-CSV from the FitCSVTool to be more human readable, removing all unneccesary and non relevant data, leaving just the activity metrics in a simple `.csv` format.
See the `sample_input/..` directory for an example of what the original `.fit` from Garmin looks like, as well as what the format of the output from the FitCSVTool looks like.

#### How to use
1. Locate a `.fit` file from an activity on your Garmin device
2. Download the FitCSVTool: https://developer.garmin.com/fit/fitcsvtool/
3. Format your `.fit` file using the FitCSVTool
4. Generate a reformatted CSV using the following command in the terminal:

    `reformat_garmin_csv.py -i <inputpath> -o <outputpath>`

**Requires: Pandas, Python**
