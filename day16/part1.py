with open('input.txt') as f:
	lines = f.read().splitlines()

# parse the first packet (where packet is packet1||packet2||packet3);
# return remaining packets (packet2||packet3) and the total version for the first packet

def recur(packet):
	global total
	version = int(packet[:3], 2)
	type_id = int(packet[3:6], 2)
	packet = packet[6:]

	if type_id == 4:
		while packet[0] == '1':
			packet = packet[5:]
		packet = packet[5:]
		return packet, version

	length_id = packet[0]
	packet = packet[1:]
	if length_id == '0':
		total_length = int(packet[:15], 2)
		subpacket = packet[15:15 + total_length]
		packet = packet[15 + total_length:]
		# For each subpacket inside the current packet, update the total version count
		while len(subpacket) != 0:
			subpacket, subversion = recur(subpacket)
			version += subversion
	else:
		num_packets = int(packet[:11], 2)
		packet = packet[11:]
		# For each subpacket inside the current packet, update the total version count
		for i in range(num_packets):
			packet, subversion = recur(packet)
			version += subversion

	return packet, version

init = ''

for i in lines[0]:
	init += bin(int(i, 16))[2:].zfill(4)

print(recur(init)[1])