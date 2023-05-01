import dash_bootstrap_components as dbc
from dash import html


def services(items):
    return html.Span([dbc.Badge(str(service), pill=True, color="#F7D162", className="m-2") for service in items])
