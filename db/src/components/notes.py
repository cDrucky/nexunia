import dash_bootstrap_components as dbc
from dash import html


def notes(o):
    return dbc.CardBody(o["notes"])