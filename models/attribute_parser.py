import re


class AttributeParser:

    COLORS = [
        "black",
        "white",
        "blue",
        "red",
        "green",
        "yellow",
        "pink",
        "purple",
        "brown",
        "grey",
        "gray",
        "orange",
        "beige",
    ]

    CLOTHING = [

        "shirt",
        "t-shirt",
        "tshirt",
        "button-down",
        "button down",
        "blazer",
        "hoodie",
        "jacket",
        "coat",
        "raincoat",
        "sweater",
        "tie",
        "dress",
        "blouse",
        "jeans",
        "trousers",
        "pants",
        "shorts",
        "skirt",
        "suit",
        "shoes",
        "boots",
        "sneakers"

    ]

    SCENES = [
        "office",
        "park",
        "street",
        "home",
        "room",
        "city",
        "bench",
        "runway",
        "building"
    ]

    ACTIVITIES = [
        "standing",
        "walking",
        "sitting",
        "running",
    ]

    STYLES = [
        "formal",
        "casual",
        "professional",
        "sporty",
    ]

    def parse(self, caption: str):

        caption = caption.lower()

        clothing = []

        for color in self.COLORS:
            for item in self.CLOTHING:

                pattern = rf"{color}\s+{item}"

                if re.search(pattern, caption):

                    clothing.append(
                        {
                            "type": item,
                            "color": color,
                        }
                    )

        scene = None

        for s in self.SCENES:
            if s in caption:
                scene = s
                break

        activity = None

        for a in self.ACTIVITIES:
            if a in caption:
                activity = a
                break

        style = None

        if "suit" in caption:

            style = "formal"

        if "tie" in caption:

            style = "formal"

        if "blazer" in caption:

            style = "formal"

        if "jeans" in caption or "hoodie" in caption:

            style = "casual"

        if any(word in caption for word in [

            "formal",

            "business",

            "business attire",

            "office wear",

            "professional",

            "blazer",

            "suit",

            "tie"

        ]):

            style = "formal"

        elif any(word in caption for word in [

            "casual",

            "weekend",

            "hoodie",

            "jeans",

            "t-shirt",

            "tshirt",

            "sneakers"

        ]):

            style = "casual"

        elif "sport" in caption:

            style = "sporty"

        return {

            "clothing": clothing,

            "style": style,

            "scene": scene,

            "activity": activity,

        }