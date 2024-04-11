attendees = int (input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)


choice = input("Do you want vegetarian catering? ")
catering = "vege delight catering" if choice == "yes" else "gourmet catering"
print("Recommended catering service:", catering)
