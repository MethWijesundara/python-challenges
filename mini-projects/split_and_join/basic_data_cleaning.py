# The raw data with mixed delimiters (, : ;)
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'

# Standardizing delimiters and splitting into a list
friends_list=csv.replace(':',',').replace(';',',').split(',')

# Printing the final result
print(f"Final Friends List: {friends_list}")


