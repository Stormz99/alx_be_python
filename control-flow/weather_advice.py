weather = input("Enter the current weather (sunny, rainy, snowy, cloudy): ").strip().lower()
if weather == "sunny":
    print(f"Wear a t-shirt and sunglasses.")
elif weather== "rainy":
    print(f"Don't forget your umberella and raincoat.")
elif weather == "cold":
    print(f"Make sire to wear a warm coat and scarf.")
else:
    print(f"Sorry, I don't have recommendations for this weather.")