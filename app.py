# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from sklearn.externals import joblib
import plotly.graph_objs as go

app = dash.Dash(__name__)

if __name__ == '__main__':
   app.run_server(debug=True)
    
app.layout = html.Div(children=[
    html.H1(children='Movie Recommendation', style={'textAlign': 'center'}),

    html.Div(children=[
        html.Label('Enter a movie title: '),
    ], style={'textAlign': 'center'}),
])
    
dcc.Input(id='title', placeholder='Movie title', type='text')

if __name__ == '__main__':
   model = joblib.load("D:\\Python\\Spyder\\prediction_model.pkl")
   app.run_server(debug=True)
    
@app.callback(
    Output(component_id='result', component_property='children'),
    [Input(component_id='title', component_property='value')])
def update_title_input(title):
    if title != None and title != '':
        try:
            other_titles = model.get_recommendations(str(title))[0]
            return 'Movies similar to {} are ${:,.2f}'.                format(title, other_titles, 2)
        except ValueError:
            return 'Unable to predict any similar movies'
        