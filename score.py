def calcScore(item, currWeather, currOccasion):
    score = 0
    
    #Calculate score based on rotation
    score += item.days_since_worn * 5
    

    # Calculate score based on weather
    if item.weather == currWeather:
        score += 15

    # Calculate score based on occasion
    if item.occasion == currOccasion:
        score += 20
        
    
    #Calculate score based on favorite level    
    if item.favorite_level == "high":
        score += 10
    elif item.favorite_level == "medium":
        score += 5

    return score

