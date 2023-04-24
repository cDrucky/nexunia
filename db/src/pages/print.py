from dash import html, register_page
import dash_bootstrap_components as dbc


def title():
    return "Print Page"


def description():
    return "Print Page"


register_page(
    __name__,
    title=title,
    description=description,
    path_template="/print",
)


def create_services_pills(services):
    for s in services:
        yield dbc.Badge(s, pill=True, color="warning", className="m-2")


def create_org_cards(organizations):
    for o in organizations:
        yield dbc.Col([
            dbc.Card([
                dbc.CardHeader(o["name"]),
                dbc.CardBody([
                    create_services_pills(o["services"]),
                    html.P(o["notes"]),
                ]),
                dbc.CardFooter([
                    html.Span(f"Website: {o['website']}"),
                    html.Span(f"Phone Number: {o['phone']}"),
                ])
            ])
        ])


def layout():
    return html.Div([
        dbc.Container([
            html.Span(f"Location: Harrisburg"),
            html.Span(f"Service: Funding"),
            html.Div(className="text-end", children=[
                html.Img(
                    width="50%",
                    src="https://ouryorkmedia.com/wp-content/uploads/2021/08/wrv.png",
                    className="img-fluid"
                )
            ]),
            dbc.Row([
                # create_org_cards(organizations)
            ])

        ]),
    ])