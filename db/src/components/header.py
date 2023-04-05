import dash_bootstrap_components as dbc
from dash import html


def header(o):
    return dbc.CardHeader([
        html.H3(html.A(o['label'], href=o["website"])),
    ])