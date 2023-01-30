# importing library
import statistics

print("\nPark Run Timer\n~~~~~~~~~~~~~~\n\nLet's go!\n")
dic = dict()

# loop to take input and store data in variable called dic i.e dict with user input and error
while True:
	strng = input("> ")
	try:
		if strng == 'END':   
		    break
		else:
		    x = strng.split(" ")
		    for i in x:
		        k = i[:i.index(":")]
		        v = i[i.index(":")+2:]
		        dic[int(k)] = int(v)
			        
	except ValueError:
		print("Error in data stream. Ignorning. Carry on.")
# checking the condition and printing out the average fastest and slowest time with grammar
try:
	if len(dic) >= 1:

		print(f"Total Runner: {len(dic)}")

	def grammar_minute(minute):
		"""Managing the grammar for the minute/minutes."""
		if minute == 1:
		    return "minute"
		else:
		    return "minutes"

	def grammar_second(second):
		"""Managing the grammar for the second/seconds."""
		if second == 1:
		    return "second"
		else:
		    return "seconds"

	print(f"Average Time: {int(statistics.mean(dic.values())//60)} {grammar_minute(int(statistics.mean(dic.values())//60))}, {int(statistics.mean(dic.values())%60)} {grammar_second(int(statistics.mean(dic.values())%60))}")
	print(f"Fastest Time: {min(dic.values())//60} {grammar_minute(min(dic.values())//60)}, {min(dic.values())%60} {grammar_second(min(dic.values())%60)}")
	print(f"Slowest Time: {max(dic.values())//60} {grammar_minute(max(dic.values())//60)}, {max(dic.values())%60} {grammar_second(max(dic.values())%60)}")

	# Finding the best runner with min value's index
	Keys = list(dic.keys())
	Values = list(dic.values())
	indx = Values.index(min(dic.values()))
	runner = Keys[indx]

	print(f"\nBest Time Here: Runner #{runner}")
	
except:
	print("No data found. Nothing to do. What a pity.")
