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

# data frame, y = column from which I want the box
graphDuration = px.box(movies, y='duration_minutes')

# defines the graph title and y value name
graphDuration.update_layout(title_text='Movies duration\'s boxplot',
                            yaxis=dict(title_text='Duration (min)'))

# creates a html file containing the graph
graphDuration.write_html(
    file='graphic_representation/boxplot/movie_duration_boxplot.html')

graphDurationByCountry = px.box(movies, x='country', y='duration_minutes')

graphDurationByCountry = graphDurationByCountry.update_layout(title_text='Movies duration\'s by country boxplot', yaxis=dict(
    title_text='Duration (min)'), xaxis=dict(title_text='Country'))

graphDurationByCountry.write_html(
    file='graphic_representation/boxplot/movie_duration_by_country_boxplot.html')
