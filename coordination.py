def clothing_coordination(first_item, second_item):
    score = 0
    
    # Check if the two items are of the same type 
    if first_item.item_type == second_item.item_type:
        return 0

    # Check if the colors of the two items complement each other
    complementary_colors = {
        "red": ["green", "blue"],
        "green": ["red", "yellow"],
        "blue": ["orange", "yellow"],
        "yellow": ["purple", "blue"],
        "purple": ["yellow", "green"],
        "orange": ["blue", "green"]
    }


    #check if the styles of the two items are compatible
    compatible_styles = {
        "casual": ["sporty", "streetwear"],
        "fancy": ["party", "formal"],
        "streetwear": ["casual", "sporty"],
        "party": ["fancy", "formal"],
        "work": ["formal", "casual"],
        "formal": ["fancy", "work"],
        "sporty": ["casual", "streetwear"]
    }
    
    # Color compatibility
    if second_item.color in complementary_colors.get(first_item.color, []):
        score += 10

    # Style compatibility
    if second_item.style in compatible_styles.get(first_item.style, []):
        score += 15

    return score