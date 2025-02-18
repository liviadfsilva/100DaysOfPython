sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list_of_words = sentence.split()
result = {key: len(key) for key in list_of_words}
print(result)