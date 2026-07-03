from clothing_item import ClothingItem
from coordination import clothing_coordination
from score import calcScore
from outfit_generator import outfit_generator


item1 = ClothingItem(
    item_type="shirt",
    category="tank-top",
    color="red",
    occasion="casual",
    style="streetwear",
    weather="sunny",
    days_since_worn=5,
    material="cotton",
    favorite_level="high",
    fit="tight"
)

print("Item 1 Color:", item1.color)
print(item1.style)

item2 = ClothingItem(
    item_type="pants",
    category="jeans",
    color="blue",
    occasion="casual",
    style="streetwear",
    weather="sunny",
    days_since_worn=3,
    material="denim",
    favorite_level="medium",
    fit="loose"
)

item3 = ClothingItem(
    item_type="shoes",
    category="sneakers",
    color="white",
    occasion="casual",
    style="sporty",
    weather="rainy",
    days_since_worn=10,
    material="mesh",
    favorite_level="medium",
    fit="normal"
)


#Score Tests:
print("Score for Item 1:", calcScore(item1, "sunny", "casual")) 
print("Score for Item 2:", calcScore(item2, "rainy", "casual"))  
print("Score for Item 3:", calcScore(item3, "rainy", "casual"))  

#Coordination Tests:
print("Coordination Score between Item 1 and Item 2:", clothing_coordination(item1, item2))  
print("Coordination Score between Item 1 and Item 3:", clothing_coordination(item1, item3))  
print("Coordination Score between Item 2 and Item 3:", clothing_coordination(item2, item3))

#Outfit Generator Test:
outfits = outfit_generator(
    [item1, item2, item3],
    currWeather="sunny",
    currOccasion="casual",
    top_n=5
)
for i, outfit in enumerate(outfits, 1):
    print(f"\nOUTFIT {i} (Score: {outfit['score']})")
    print("Item 1:", outfit["items"][0])
    print("Item 2:", outfit["items"][1])
