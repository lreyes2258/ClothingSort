class ClothingItem:

    def __init__(self,
                 item_type,
                category,
                color,
                occasion,
                style,
                weather,
                days_since_worn,
                material,
                favorite_level,
                fit):
        self.item_type = item_type
        self.category = category
        self.color = color
        self.occasion = occasion
        self.style = style
        self.weather = weather
        self.days_since_worn = days_since_worn
        self.material = material
        self.favorite_level = favorite_level
        self.fit = fit
        
    def __str__(self):
        return f"Category: {self.category}, Color: {self.color}, Style: {self.style}, Weather: {self.weather}, Days Since Worn: {self.days_since_worn}, Material: {self.material}, Favorite Level: {self.favorite_level}, Fit: {self.fit}"
        