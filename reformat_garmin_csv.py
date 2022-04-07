import sys, getopt
import pandas as pd

# Prompt to show users when help arg is given, or when they pass an invalid input
def prompt_input_format():
  print('reformat_garmin_csv.py -i <inputpath> -o <outputpath> -f <european-format:bool>')


# Get the paths to the input and output files from the arguments passed in the terminal
def get_files(args):
	european_format = False
	
	try:
		opts, args = getopt.getopt(args,"hi:o:",["ifile=","ofile=","european_format="])
	except getopt.GetoptError:
		prompt_input_format()
		sys.exit(2)

	# Loop over the args
	for opt, arg in opts:
		if opt == '-h':
			prompt_input_format()
			sys.exit()
		elif opt in ("-i", "--ifile"):
			ifile = arg
		elif opt in ("-o", "--ofile"):
			ofile = arg
		elif opt in ("-f", "--european_format"):
			european_format = arg

	return ifile, ofile, european_format

def cast_col(df, col_name: str, cast_to: type):
	df[col_name] = df[col_name].astype(cast_to)

if __name__=="__main__":
	ipath, opath, european_format = get_files(sys.argv[1:])
	sep = ';' if european_format else ','
	decimal = ',' if european_format else '.'

	# Read the file as a pd dataframe
	df = pd.read_csv(ipath,delimiter=sep,low_memory=False)

	# Get the name of the sport
	sport = df[(df.Message=='sport') & (df.Type == 'Data')]['Value 1'].iloc[0]

	# Remove everything but the record data
	df = df[(df.Message == 'record') & (df.Type == 'Data')]

	full_colnames = []
	new_df = pd.DataFrame()
	
	# Extract the new column names and populate them to form new df
	for i in range(1,len(df.columns)):
		col_name = 'Field {}'.format(i)
		unit_name = 'Units {}'.format(i)
		value_name = 'Value {}'.format(i)
		
		if not col_name in df.columns:
			continue
		
		field = df[col_name].iloc[0]
		unit = df[unit_name].iloc[0]

		if pd.isnull(field) or pd.isnull(unit):
			continue
		
		name = "{} [{}]".format(field, unit)
		full_colnames.append(name)
		new_df[field] = df[value_name]

	df = new_df

	# Reformat all the columns that make more sense to represent as ints
	int_cols = ['heart_rate','timestamp','cadence','temperature','timestamp','position_long','position_lat']
	for col in int_cols:
		if col in df.columns:
			cast_col(df, col, int)

	if 'enhanced_altitude' in df.columns:
		cast_col(df, 'enhanced_altitude', float)
		df['enhanced_altitude'] = df['enhanced_altitude'].apply(lambda x: round(x, 1))

	# Reformat from garmins semicircle format to a normal longitude latitude format.
	# For more info on semicircle coordinate unit see: https://gis.stackexchange.com/questions/156887/conversion-between-semicircles-and-latitude-units
	max_int = 2**31 
	if 'position_lat' in df.columns:
		df['position_lat'] = df['position_lat'].apply(lambda x: x * (180 / max_int))
		full_colnames[df.columns.get_loc('position_lat')] = 'position_lat [degrees]'

	if 'position_long' in df.columns:
		df['position_long'] = df['position_long'].apply(lambda x: x * (180 / max_int))
		full_colnames[df.columns.get_loc('position_long')] = 'position_long [degrees]'

	# Reformat timescale from unix to be time from activity start, e.g. 0, 1, ..  
	if 'timestamp' in df.columns:
		new_timestamps = []
		start_time = df['timestamp'].iloc[0]

		for i in range(len(df.timestamp)):
			step = df['timestamp'].iloc[i] - start_time
			new_timestamps.append(step)
		df['timestamp'] = new_timestamps

	# Change the columnnames to include the units
	df.columns = full_colnames

	# Write df to csv
	df.to_csv(opath, index=False,header=True, sep=sep,decimal=decimal)

