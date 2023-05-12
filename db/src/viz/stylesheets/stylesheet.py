default_stylesheet = [
    {
        "selector": "node[node_color]",
        "style": {
            "label": "data(label)",
            "color": "black",
            "text-valign": "center",
            "text-halign": "center",
            "background-color": "data(node_color)",
            "opacity": 0.65,
            "font-size": 24,
            "z-index": 9999,
        },
    },
    {
        "selector": "node[!node_color]",
        "style": {
            "label": "data(label)",
            "color": "black",
            "text-valign": "center",
            "text-halign": "center",
            "background-color": "grey",
            "opacity": 0.65,
            "z-index": 9999,
        },
    },
    {
        "selector": "edge",
        "style": {"curve-style": "bezier", "opacity": 0.45, "z-index": 5000},
    },
    {"selector": ".followerNode", "style": {"background-color": "#0074D9"}},
    {
        "selector": ".followerEdge",
        "style": {
            "mid-target-arrow-color": "blue",
            "mid-target-arrow-shape": "vee",
            "line-color": "#0074D9",
        },
    },
    {"selector": ".followingNode", "style": {"background-color": "#FF4136"}},
    {
        "selector": ".followingEdge",
        "style": {
            "mid-target-arrow-color": "red",
            "mid-target-arrow-shape": "vee",
            "line-color": "#FF4136",
        },
    },
    {
        "selector": ":selected",
        "style": {
            "border-width": 2,
            "border-color": "black",
            "border-opacity": 1,
            "opacity": 1,
            "label": "data(label)",
            "color": "black",
            "font-size": 24,
            "z-index": 9999,
        },
    },
]
