import pandas
import plotly.express as px

data_frame = pandas.read_csv('data/netflix.csv')

# getting only the release years from the data frame
releases_year = data_frame['release_year'].value_counts().reset_index()

# renaming the columns so the graph looks better
releases_year.rename(
    columns={'release_year': 'year', 'count': 'releases'}, inplace=True)

# sorting the data by year in ascending order
releases_year = releases_year.sort_values(by='year')

line = px.line(releases_year, x='year', y='releases',
               title='Releases per year')
line.write_html(
    file='graphic_representation/line/movie_releases_per_year.html')
