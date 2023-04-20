import pandas
import plotly.express as px

data_frame = pandas.read_csv('data/netflix.csv')

# getting only the movies from the data frame
movies = data_frame[data_frame['type'] == 'Movie']


def parse_duration(duration):
    duration_string_number = duration.split(' ')[0]
    parsed_duration = int(duration_string_number)
    return parsed_duration


# creates a new column called "duration_minutes" in the data frame
# the values from this new column is the parsed duration from the
# original duration column
movies['duration_minutes'] = movies['duration'].apply(parse_duration)

histogram = px.histogram(movies['duration_minutes'])
histogram.update_layout(title_text='Movie duration\'s histogram')
histogram.write_html(
    file='graphic_representation/histogram/movie_duration_histogram.html')
