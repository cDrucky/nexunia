import dash_bootstrap_components as dbc
from dash import html


twitter = 'static/twitter.svg'
linkedin = 'static/linkedin.svg'
facebook = 'static/facebook.svg'
instagram = 'static/instagram.svg'
tiktok = 'static/tiktok.svg'
info = 'static/info.svg'


def social_footer():
    return dbc.CardFooter([
                        html.Img(src=linkedin, style={'width': '16px', 'height': '16px',}, className="mx-2"),
                        html.Img(src=twitter, style={'width': '16px', 'height': '16px',}, className="mx-2"),
                        html.Img(src=facebook, style={'width': '16px', 'height': '16px',}, className="mx-2"),
                        html.Img(src=instagram, style={'width': '16px', 'height': '16px',}, className="mx-2"),
                        html.Img(src=tiktok, style={'width': '16px', 'height': '16px', }, className="mx-2"),

                    ]
                )