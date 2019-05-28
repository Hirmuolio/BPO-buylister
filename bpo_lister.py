#!/usr/bin/env python3

import csv

# Read owned BPO info
# Read NPC BPO info
# Write buylist of BPOs that are in NPC sheet but not in our own sheet

our_bpos = []

with open('our_BPOs.csv', newline='') as ours_csv:
	print( 'reading our BPOs' )
	reader = csv.reader(ours_csv)
	for row in reader:
		our_bpos.append( row[0] )

with open('npc_BPOs.csv', newline='') as npc_csv:
	reader = csv.reader(npc_csv)
	
	with open('output.csv', 'w', newline='') as csvfile:
		print( 'Comparing BPOs...' )
		writer = csv.writer(csvfile, delimiter=',' )
		for row in reader:
			if( not row[0] in our_bpos ):
				writer.writerow( row )
print( 'BPO buylist written to output.csv' )