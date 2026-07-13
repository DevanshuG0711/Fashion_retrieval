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
        "hoodie",
        "blazer",
        "jacket",
        "coat",
        "raincoat",
        "sweater",
        "jeans",
        "trousers",
        "pants",
        "shorts",
        "skirt",
        "dress",
        "tie",
    ]

    SCENES = [
        "office",
        "park",
        "street",
        "home",
        "room",
        "city",
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

        for st in self.STYLES:
            if st in caption:
                style = st
                break

        return {

            "clothing": clothing,

            "style": style,

            "scene": scene,

            "activity": activity,

        }