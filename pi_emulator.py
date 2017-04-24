#emulate cards scanning

import random, time
import logic.dbStreamer as dbStreamer

cards = ["123456789", "987654321", "521346789", "752822764"]

"""
while True:
	#print(cards[random.randint(0, len(cards)-1)], str(random.randint(0, 23)) + ":" + str(random.randint(0,59)))	
	dbStreamer.save_iStream(cards[random.randint(0, len(cards)-1)])	
	print("new db Interaction")
	time.sleep(1)
"""
for x in range(4):
	for y in range(4): 
		dbStreamer.save_iStream(cards[y]) 
		print("new db Interaction for user" + str(x) + "time number: " + str(y))
