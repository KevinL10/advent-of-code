with open('input.txt') as f:
	lines = f.read().splitlines()

# parse the first packet (where packet is packet1||packet2||packet3);
# return remaining packets (packet2||packet3) and the total value for the first packet

def recur(packet):
	version = int(packet[:3], 2)
	type_id = int(packet[3:6], 2)
	packet = packet[6:]
	subvalues = []

	if type_id == 4:
		value = ''
		while packet[0] == '1':
			value += packet[1:5]
			packet = packet[5:]
		value += packet[1:5]	
		packet = packet[5:]		
		# Return the remaining subpackets and the value of the current one
		return packet, int(value, 2)

	length_id = packet[0]
	packet = packet[1:]
	if length_id == '0':
		total_length = int(packet[:15], 2)
		subpacket = packet[15:15 + total_length]
		packet = packet[15 + total_length:]

		while len(subpacket) != 0:
			# Add the values for each subpacket to the overall values
			subpacket, subvalue = recur(subpacket)
			subvalues.append(subvalue)
	else:
		num_packets = int(packet[:11], 2)
		packet = packet[11:]

		for i in range(num_packets):
			packet, subvalue = recur(packet)
			subvalues.append(subvalue)

	if type_id == 0:
		value = sum(subvalues)
	elif type_id == 1:
		value = 1
		for k in subvalues:
			value *= k
	elif type_id == 2:
		value = min(subvalues)
	elif type_id == 3:
		value = max(subvalues)
	elif type_id == 5:
		value = int(subvalues[0] > subvalues[1])
	elif type_id == 6:
		value = int(subvalues[0] < subvalues[1])
	elif type_id == 7:
		value = int(subvalues[0] == subvalues[1])

	return packet, value

init = ''

for i in lines[0]:
	init += bin(int(i, 16))[2:].zfill(4)

print(recur(init)[1])