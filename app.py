###reddit web scraper ###

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from helpers import *



########### Define a few variables ######

tabtitle = 'Reddit Shower Webscraper'
sourceurl = 'https://old.reddit.com/r/Showerthoughts?sort=top&t=week'
githublink = 'https://github.com/mirandaprasad/403-reddit-webscraper'
button_style = {'background-color': 'darkgreen',
                    'color': 'white',
                    'textAlign': 'center',
                }






########### Initiate the app
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = ['https://github.com/plotly/dash-app-stylesheets/blob/master/dash-uber-ride-demo.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Layout ###########

app.layout = html.Div(children=[
    html.H1('Webscraping posts from Reddit Shower Thoughts'),
    # Dropdowns
    html.Div(children=[
        html.Button('Lets Scrape Reddit!', id='submit-val', n_clicks=0, style=button_style),
        html.Div(id='message'),
        dcc.Graph(id='figure-1'),
    ], className='twelve columns'),

    # Footer
    html.Br(),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

########### Callback ###########

@app.callback(
    [Output('message', 'children'),
    Output('figure-1', 'figure')],
    [Input('submit-val', 'n_clicks')],
    )
def update_output(n_clicks):
    if n_clicks==0:
        message = f"Click the button"
        return message, base_fig()
    elif n_clicks==1:
        message = f"You've clicked that button {n_clicks} time!"
        return message, scrape_reddit()
    elif (n_clicks>1) & (n_clicks<5):
        message = f"You've clicked that button {n_clicks} times!"
        return message, error_fig()
    else:
        message = f"Seriously, stop clicking the button. You've clicked it {n_clicks} times. Nothing else is going to happen, punk!"
        return message, error_fig()


############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
