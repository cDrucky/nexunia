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
    if o['linkedin']:
        socials.append(html.Img(src=linkedin, style={'width': '16px', 'height': '16px',}, className="mx-2"))
    if o['twitter']:
        socials.append(html.Img(src=twitter, style={'width': '16px', 'height': '16px',}, className="mx-2"))
    if o['facebook']:
        socials.append(html.Img(src=facebook, style={'width': '16px', 'height': '16px',}, className="mx-2"))
    if o['instagram']:
        socials.append(html.Img(src=instagram, style={'width': '16px', 'height': '16px',}, className="mx-2"))
    if o['tiktok']:
        socials.append(html.Img(src=tiktok, style={'width': '16px', 'height': '16px', }, className="mx-2"))
    return socials


def social_footer(o):
    return dbc.CardFooter(parse_socials(o))
