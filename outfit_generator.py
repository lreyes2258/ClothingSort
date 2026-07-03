from score import calcScore
from coordination import clothing_coordination

def outfit_generator(items, currWeather, currOccasion, top_n):
    #Generates outfit reccomendations based on clothing score, weather, and occasion
    #It returns the top n outfits to give you a variety to choose from

    
    scored_outfits = []
    for item in items:
        score = calcScore(item, currWeather, currOccasion)
        scored_outfits.append((item, score))
    
    scored_outfits.sort(key=lambda x: x[1], reverse=True)
    
    outfit_recommendations = []

    # Iterate through all combinations of items
    for i in range(len(scored_outfits)):
        item1, score1 = scored_outfits[i]
        
        for j in range(i + 1, len(scored_outfits)):
            item2, score2 = scored_outfits[j]

            # Calculate the score for the coordination of the two items
            coordination_score = clothing_coordination(item1, item2)

            # Calculate the individual scores for each item
    

            #Total score is the sum of individual scores and coordination score
            total_score = score1 + score2 + coordination_score
            
            #Gives a bonus based on weather
            if item1.weather == currWeather and item2.weather == currWeather:
                total_score += 5
                
            #Gives a bonus based on occasion
            if item1.occasion == currOccasion and item2.occasion == currOccasion:
                total_score += 10
            # Update the best outfit if the current total score is higher
            outfit_recommendations.append({
                "items": (item1, item2),
                "score": total_score
            })

    # Sorts outfits by best score
    outfit_recommendations.sort(key=lambda x: x["score"], reverse=True)

    #Returns top 5 outfits
    return outfit_recommendations[:top_n]