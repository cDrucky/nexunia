from enum import Enum


base = "Businesses go through natural cycles of creation, growth and dissolution – not always in a straight " \
           "line. To better understand where you are in your own lifecycle, here is a snapshot of all the stages"


class Lifecycle(Enum):
    IDEA = {
        "NAME": "Idea",
        "DESCRIPTION": "You either have an idea or are looking for one. There’s a lot that can be done to vet an idea, "
                       "prepare for financial investment, and design the business before starting operations."
    }
    SEED = {
        "NAME": "Seed",
        "DESCRIPTION": "You have a product or service that requires investment to get started. You have all "
                       "documentation to accept financial investment from bank loans to venture funding. "
    }

    STARTUP = {
        "NAME": "Startup",
        "DESCRIPTION": "You have launched your product or service and are receiving and responding to feedback from "
                       "customers. You have revenue and may or may not be profitable. "
    }
    GROWTH = {
        "NAME": "Growth",
        "DESCRIPTION": "You have demonstrated product-market fit. You need to grow capacity to meet demand. You are "
                       "discovering competitors. You have revenue and may or may not be profitable."
    }
    MATURE = {
        "NAME": "Mature",
        "DESCRIPTION": "You have an established company with a clear portion of the market and devoted customers."
    }
    EXIT = {
        "NAME": "Exit",
        "DESCRIPTION": "You are looking to move on from your business via selling, a succession plan and/or simply "
                       "closing up shop. "
    }


