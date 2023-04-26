import dash_bootstrap_components as dbc
from dash import html
from objects import Lifecycle, base

info = 'static/info.svg'


def label():
    return html.P("Lifecycle Stages", style={'margin-right': '5px', 'margin-left': '1vw'})

def lifecycle_label():
    i, i_info = popover()
    return html.Div([label(), i, i_info], style={
        'display': 'flex',
        'flex-direction': 'row',
        'align-items': 'center',
        'margin': '0px',
        'padding': '0px',
        'width': '100%',
        'height': '100%'
    })


def popover(pop_id="click-target"):
    try:
        text = Lifecycle[pop_id.upper()].value["DESCRIPTION"]
    except KeyError:
        text = base
    i = html.Img(src=info, id=pop_id, style={'width': '14px', 'height': '14px', 'margin-left': '3px'}, className="mb-3")

    i_info = dbc.Popover(
        text,
        target=pop_id,
        body=True,
        trigger="hover",
        placement="left",
        offset=150,
    )

    return i, i_info


def make_lifecycle(lifecycles):
    all_lifecycles = [member.value["NAME"] for member in Lifecycle.__members__.values()]

    lgi = []
    for lifecycle in all_lifecycles:
        if lifecycle in lifecycles:
            style = {}
        else:
            style = {"color": "lightgrey"}
        lifecycle_component = html.Span(lifecycle)
        i, i_info = popover(pop_id=lifecycle)
        lgi.append(dbc.ListGroupItem([lifecycle_component, i, i_info], style=style))
    lg = dbc.ListGroup(lgi, flush=True)

    return lg

