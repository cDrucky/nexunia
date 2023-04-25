from dash import html, register_page
import dash_bootstrap_components as dbc
from viz import get_elements, full_params_query
from dataclasses import dataclass


def create_organization_objects(elements):
    organizations = []
    service_mapping = {}
    for result in elements:
        node_data = result.get("data")
        node_type = node_data.get("node_type")
        node_id = node_data.get("id")
        if node_type == "Organization":
            name = node_data.get("label")
            notes = node_data.get("notes")
            website = node_data.get("website")
            address = node_data.get("address")
            phone = node_data.get("phone")
            org_services = []
            org_id = node_data.get("id")
            organizations.append(Organization(
                id=org_id,
                name=name,
                services=org_services,
                notes=notes,
                website=website,
                phone=phone,
                address=address)
            )
        elif node_type == "Service":
            service_mapping[node_data.get("id")] = node_data.get("label")
        elif "HANDLES" in node_id:
            org_id = result.get("data").get("source")
            org_services = [service_mapping[result.get("data").get("target")]]
            for org in organizations:
                if org_id == org.id:
                    org.services.extend(org_services)
    organizations = list(set(organizations))
    return organizations


@dataclass
class Organization:
    id: int
    name: str
    services: list
    notes: str
    website: str
    phone: str
    address: str

    def __hash__(self):
        return hash((self.id, self.name, tuple(self.services), self.notes, self.website, self.phone, self.address))


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


def create_services_pills(services, notes):
    pills = [dbc.Badge(s, pill=True, color="warning", className="m-2") for s in services]
    pills.append(html.P(notes))
    return pills


def create_org_cards(organizations):
    cards = []
    for o in organizations:
        footer_children = []
        if o.website:
            footer_children.append(html.Span(f"Website: {o.website}"))
        if o.phone:
            footer_children.append(html.Span(f"Phone Number: {o.phone}"))

        footer = dbc.CardFooter(footer_children)

        card = dbc.Card([
            dbc.CardHeader(o.name),
            dbc.CardBody(
                create_services_pills(o.services, o.notes),
            ),
            footer
        ])

        cards.append(dbc.Col(card, width=3, className="mb-4"))

    return dbc.Row(cards, className="mx-auto")


def layout(location=None, lifecycle=None, services=None, **other_unknown_query_strings):
    if location and lifecycle and services:
        query = full_params_query([location], [lifecycle], [services])
        elements = get_elements(query)
        organizations = create_organization_objects(elements)
        return html.Div([
            dbc.Container([
                html.Div(className="text-end", children=[
                    html.Img(
                        width="10%",
                        src="https://ouryorkmedia.com/wp-content/uploads/2021/08/wrv.png",
                        className="img-fluid"
                    )
                ]),
                html.Span("Location: Harrisburg"),
                html.Br(),
                html.Span("Service: Funding"),
                dbc.Row(
                    create_org_cards(organizations)
                )

            ])
        ])
