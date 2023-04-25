from viz import get_elements, get_single_element
from components import (
    social_footer,
    make_lifecycle,
    header,
    services,
    notes,
    lifecycle_label,
)
from utils import parse_elements
import dash_bootstrap_components as dbc


def display_node_info(node_data):
    if node_data is None:
        return None
    else:

        elements = get_elements(get_single_element(node_data["label"]))
        o, l, s, lc = parse_elements(elements)

        node_info_contents = dbc.Card(
            [
                header(o),
                notes(o),
                lifecycle_label(),
                services(s),
                make_lifecycle(lc),
                social_footer(o),
            ],
            id="node-info",
            style={"border": "1px solid #ddd"},
        )
        return node_info_contents
