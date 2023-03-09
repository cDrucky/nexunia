stylesheet = [
    {
        "selector": "node",
        "style": {
            "background-color": "data(node_color)",
            "label": "data(label)",
            "font-size": "14px",
        },
    },
    {"selector": "edge", "style": {"line-color": "gray", "curve-style": "bezier"}},
    {
        "selector": ".selected",
        "style": {"border-color": "black", "border-width": "2px"},
    },
]
