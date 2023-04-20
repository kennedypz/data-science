import pandas
import plotly.express as px

data_frame = pandas.read_csv('data/netflix.csv')

# getting only the tv shows from the data frame
tv_shows = data_frame[data_frame['type'] == 'TV Show']

# created a bar graph that shows the amount of tv shows (value_counts())
# of each genre (listed_in)
barplot = px.bar(tv_shows['listed_in'].value_counts())
barplot.update_layout(
    title_text='Number of TV shows of each genre', yaxis=dict(title_text='Quantity'))
barplot.write_html(
    file='graphic_representation/barplot/tv_shows_genres.html')

# the previous graph has a lot of data and can be a bit confusing
# so we can define a smaller sample to build the graph, in this case
# the graph is only going to show the genres that have at least 15
# tv shows in it;
genre_15 = tv_shows['listed_in'].value_counts(
)[tv_shows['listed_in'].value_counts() >= 15]

# the text=genre_15.values indicated that the bar title will be the values
# of the genre, in this case, how many cases are there.
barplot = px.bar(genre_15, text=genre_15.values)
barplot.update_layout(
    title_text='Number of TV shows of each genre', yaxis=dict(title_text='Quantity'))

# here we format the text we specified in line 26 so it shows outside de bar
barplot.update_traces(texttemplate='%{text:.2s}', textposition='outside')
barplot.write_html(
    file='graphic_representation/barplot/tv_shows_genres_15.html')
