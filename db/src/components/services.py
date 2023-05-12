import dash_bootstrap_components as dbc
from dash import html


def services(items):
    serv = html.Div([
        html.H6("Services", className="card-subtitle ml-3"),
        html.Span([dbc.Badge(str(service), pill=True, color="#F7D162", className="m-2") for service in items])
    ])
    return serv
