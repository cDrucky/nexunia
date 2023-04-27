from dataclasses import dataclass


@dataclass
class Organization:
    name: str
    serviced_locations: list
    parent_organization_1: str
    parent_organization_2: str
    parent_organization_3: str
    address: str
    website: str
    notes: str
    lifecycle_stage: list
    # industry: list
    services: list
    linkedin: str
    twitter: str
    instagram: str
    facebook: str
    tiktok: str

