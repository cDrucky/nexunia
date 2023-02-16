from dataclasses import dataclass


@dataclass
class Organization:
    id: int
    name: str
    address: str
    location: str
    notes: str
    website: str
    parent_organization: str
    industry: list
    service: list
    lifecycle_stage: list
    serviced_locations: list
    services_rendered: list

