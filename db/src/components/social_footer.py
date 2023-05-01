import dash_bootstrap_components as dbc
from dash import html


twitter = 'static/twitter.svg'
linkedin = 'static/linkedin.svg'
facebook = 'static/facebook.svg'
instagram = 'static/instagram.svg'
tiktok = 'static/tiktok.svg'
info = 'static/info.svg'


def parse_socials(o):
    socials = []
    if isinstance(o['linkedin'], str):
        socials.append(html.A(html.Img(src=linkedin, style={'width': '16px', 'height': '16px',}, className="mx-2"), href=o['linkedin']))
    if isinstance(o['twitter'], str):
        socials.append(html.A(html.Img(src=twitter, style={'width': '16px', 'height': '16px',}, className="mx-2"), href=o['twitter']))
    if isinstance(o['facebook'], str):
        socials.append(html.A(html.Img(src=facebook, style={'width': '16px', 'height': '16px',}, className="mx-2"), href=o['facebook']))
    if isinstance(o['instagram'], str):
        socials.append(html.A(html.Img(src=instagram, style={'width': '16px', 'height': '16px',}, className="mx-2"), href=o['instagram']))
    if isinstance(o['tiktok'], str):
        socials.append(html.A(html.Img(src=tiktok, style={'width': '16px', 'height': '16px', }, className="mx-2"), href=o['tiktok']))
    return socials


def social_footer(o):
    return dbc.CardFooter(parse_socials(o))
