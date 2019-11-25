# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:48:15 2019

@author: M64D946
"""

import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq
import pandas as pd
import plotly.graph_objs as go

#from app import app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#1e2130',
    'text': '#7FDBFF'
}

df = pd.read_excel('example7.xlsx')

if 'DYNO' in os.environ:
    app_name = os.environ['DASH_APP_NAME']
else:
    app_name = 'dash-barplot'




app.layout = html.Div(style={'backgroundColor': colors['background']}, children =[
    html.H1("SII-sensitivities", style={"fontWeight": "bold", "textAlign": "center", 'color' : 'orange'}),
    
    html.Div([
        html.Div([
        html.Div([html.Div([dcc.Dropdown(id='product-selected1',
                                         options=[{'label': i.title(), 'value': i} for i in df.Scenario.unique()],
                                         value="Equity -25% MTM")], className="six columns",
                           style={"width": "40%", "float": "right"}),
                  html.Div([dcc.Dropdown(id='product-selected2',
                                         options=[{'label': i.title(), 'value': i} for i in df.Period.unique()],
                                         value='2019 Q1')], className="six columns", style={"width": "40%", "float": "left"}),
                  ], className="row", style={"padding": 50, "width": "60%", "margin-left": "auto", "margin-right": "auto"}),
        dcc.Graph(id='my-graph')
        ],className = 'eight columns'),
        
        
        html.Div(
            id="card-2",
            children=[
                html.P("Current SII-ratio", style={"textAlign": "center", 'color' : 'orange'}),
                daq.Gauge(
                    id="progress-gauge",
                    max=300,
                    min=0,
                    style={"textAlign": "center"},
                    value = 211,
                    showCurrentValue=True,  # default size 200 pixel
                    color = 'orange',),],className = 'four columns', style = {'margin-top':200}),
    ],className = 'row')
         
    # dcc.Link('Go to Source Code', href='{}/code'.format(app_name))
], className="row")


@app.callback(
    dash.dependencies.Output('my-graph', 'figure'),
    [dash.dependencies.Input('product-selected1', 'value'),
    dash.dependencies.Input('product-selected2', 'value')])
def update_graph(selected_product1, selected_product2):
    #dff = df[(df[selected_product1] >= 2) & (df[selected_product2] >= 2)]
    df1 = df[((df.Period == selected_product2))]
    df2 = df1[((df1.Scenario == 'Reported figures'))]
    df3 = df1[((df1.Scenario == selected_product1))]
    text = [int(df2['SII-ratio'].values[0]*100), int(df3['SII-ratio'].values[0]*100)]
    dff = pd.concat([df2, df3])
    trace1 = go.Bar(x=dff['Scenario'], y=dff['EOF'], name='EOF', )
    trace2 = go.Bar(x=dff['Scenario'], y=dff['SCR'], name='SCR', )

    return {
        'data': [trace1, trace2],
        'layout': go.Layout(title=  f'SII-ratio changes from {text[0]}% to {text[1]}%',
                            colorway=["#EF963B", "#EF533B"], hovermode="closest",
                            plot_bgcolor = colors['background'],
                            paper_bgcolor = colors['background'],
                            font = {'color' : 'orange'},
                            xaxis={'title': "Scenario", 'titlefont': {'color': 'orange', 'size': 14},
                                   'tickfont': {'size': 9, 'color': 'orange'}},
                            yaxis={'title': "EUR (million)", 'titlefont': {'color': 'orange', 'size': 14, },
                                   'tickfont': {'color': 'orange'}})}


#app.css.append_css({
#    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
#})
    
if __name__ == '__main__':
    app.run_server(debug=True, host = '0.0.0.0', port = '80')
    
   