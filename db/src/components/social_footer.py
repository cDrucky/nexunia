import dash_bootstrap_components as dbc
from dash import html


twitter = 'static/twitter.svg'
linkedin = 'static/linkedin.svg'
facebook = 'static/facebook.svg'
instagram = 'static/instagram.svg'
tiktok = 'static/tiktok.svg'
info = 'static/info.svg'


def parse_socials(o):
    socials = [html.A(html.Img(src=v, style={'width': '16px', 'height': '16px',}, className="mx-2"), href=o[k], target="_blank")
               for k, v in {'linkedin': linkedin, 'twitter': twitter, 'facebook': facebook, 'instagram': instagram, 'tiktok': tiktok}.items()
               if isinstance(o[k], str)]
    return socials



def social_footer(o):
    return dbc.CardFooter(parse_socials(o))
