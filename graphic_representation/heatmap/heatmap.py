import pandas
import plotly.figure_factory as ff

data_frame = pandas.read_csv('data/BigmacPriceJuly2022.csv')

# in order to use the heatmap we need to calculate the correlation
correlation = data_frame.corr(method='spearman', numeric_only=True)

heatmap = ff.create_annotated_heatmap(
    z=correlation.values,
    x=list(correlation.columns),
    y=list(correlation.index),
    colorscale='magenta',
    annotation_text=correlation.round(1).values,
    showscale=True
)

heatmap.update_layout(title_text='Spearman\'s correlation heatmap')
heatmap.write_html(
    file='graphic_representation/heatmap/spearmans_correlation_heatmap.html')
