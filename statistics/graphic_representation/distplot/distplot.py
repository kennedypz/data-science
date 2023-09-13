import pandas
import plotly.express as px
import plotly.figure_factory as ff

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

distplot = ff.create_distplot([movies['duration_minutes']], [
                              'Duration (min)'], show_rug=True, bin_size=2, show_hist=True)
distplot.update_layout(title_text='Movie\'s duration')
distplot.write_html(
    file='graphic_representation/distplot/movie_duration_distplot.html')

# now let's compare the duration of the 4 most popular genres
# movies['listed_in'].value_counts().head(4)

drama = movies[movies['listed_in'] ==
               'Dramas, International Movies']['duration_minutes']
documentaries = movies[movies['listed_in']
                       == 'Documentaries']['duration_minutes']
stand_up = movies[movies['listed_in'] == 'Stand-Up Comedy']['duration_minutes']
comedies = movies[movies['listed_in'] ==
                  'Comedies, Dramas, International Movies']['duration_minutes']

data = [drama, documentaries, stand_up, comedies]
labels = ['Dramas, International Movies', 'Documentaries',
          'Stand-Up Comedy', 'Comedies, Dramas, International Movies']

distplot = ff.create_distplot(data, labels, show_rug=False, show_hist=False)
distplot.update_layout(title_text='Top 4 Movies duration by genre')
distplot.write_html(
    file='graphic_representation/distplot/movie_duration_distplot_by_genre.html')
