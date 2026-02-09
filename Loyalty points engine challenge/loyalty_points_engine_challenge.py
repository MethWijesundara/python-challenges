def earn_points(price):
    """ Calculates 3 points per whole dollar spent. """
    whole_dollar=int(price)
    return whole_dollar*3

def tier_label(points):
    """Return the loyalty tier name based on total points."""
    if points >=500:
        return "Gold"
    elif points >= 100:
        return "Silver"
    else: 
        return "Bronze"

def main():
    purchases = [12.50,34.20,299.99]
    total_spent = 0.0
    total_points = 0 

    for amount in purchases:
        total_spent += amount
        total_points += earn_points(amount)

    final_tier=tier_label(total_points)

    print("===== Loyalty Summary =====")
    print(f"Total spend: ${total_spent:.2f}")
    print(f"Total points: {total_points}")
    print(f"Tier achieved {final_tier}")

if __name__== "__main__": 
    main()

