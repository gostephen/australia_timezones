import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import datetime
import pytz

app = dash.Dash(__name__)

# Define the three main Australian time zones
time_zones = {
    'Sydney': 'Australia/Sydney',
    'Adelaide': 'Australia/Adelaide',
    'Perth': 'Australia/Perth',
}

app.layout = html.Div([
    html.H1("Current Time and Date in Australian Time Zones",
            style={'textAlign': 'center'}),
    html.Div(id='clocks', style={
             'display': 'flex', 'justifyContent': 'space-around', 'alignItems': 'center'}),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds, update every second
        n_intervals=0
    )
], style={'height': '100vh', 'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'center'})


@app.callback(
    Output('clocks', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_clocks(n):
    clocks = []
    for city, tz in time_zones.items():
        now = datetime.datetime.now(pytz.timezone(tz))
        formatted_time = now.strftime('%H:%M:%S')
        formatted_date = now.strftime('%Y-%m-%d')
        clocks.append(html.Div([
            html.Div(children=[
                html.Div(f"{city}", style={
                         'fontSize': '24px', 'fontWeight': 'bold'}),
                html.Div(f"Date: {formatted_date}",
                         style={'fontSize': '16px'}),
                html.Div(f"Time: {formatted_time}", style={
                         'fontSize': '24px', 'fontWeight': 'bold'}),
            ], style={'textAlign': 'center', 'padding': '20px', 'background': 'lightgrey', 'borderRadius': '10px', 'margin': '10px'})
        ]))
    return clocks


if __name__ == '__main__':
    app.run_server(debug=True)
