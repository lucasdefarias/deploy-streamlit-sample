import streamlit 
import pandas
import numpy
# Make sure you've installed Streamlit. Pandas and numpy will be installed when you install streamlist.
# To run it, type: streamlit run https://gist.githubusercontent.com/nittin-shankar/a470595c8a8dfdb3ca0ecf3c33a753dc/raw/0bb333ed3f7153cf09bf32ff78de1398e30a4223/uber_pickups.py

streamlit.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@streamlit.cache # Caches the output if the output, arity and the bytecode that that make up the function is the same.
def load_data(nrows):
  data = pandas.read_csv(DATA_URL, nrows=nrows) # Converts csv to dataframe
  lowercase = lambda x: str(x).lower() # Anonymous function to lowercase strings
  data.rename(lowercase, axis=1, inplace=True) # Renames all column labels to lowercase. The inplace is true because we don't want it to return anything. We simply want it to change the data.
  data[DATE_COLUMN] = pandas.to_datetime(data[DATE_COLUMN]) # Changes the data of DATE_COLUMN to datetime from string in series. Then assigns is to DATE_COLUMN's data
  return data


data_load_state = streamlit.text('Loading data...') # Create a text element and let the reader know the data is loading.
# Load 5 rows into dataframe
data = load_data(10000)
# Notify the reader that the data is lodaded
data_load_state.text('Loading data...done! Yesss!')

if streamlit.checkbox('Show raw data'): # This is a checkbox widget. It returns true if selected and false if not
    streamlit.subheader('Raw data') # Subheader widget
    streamlit.dataframe(data) # Dataframe widget. Basically shows a table to the reader

streamlit.subheader('Bar Chart')
hist_values =  numpy.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24)) 
# Above variable contains a two element tuple with an array. 
# The first element is a list of values.
# The second element is a list of bins.
# For example it looks this [["Nittin", "Shankar", "Devy"], [1, 2, 3]]
streamlit.bar_chart(hist_values[0]) # We only need the values to create a bar chart it seems.
