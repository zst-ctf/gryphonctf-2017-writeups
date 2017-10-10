
# https://en.wikipedia.org/wiki/Scientific_pitch_notation
text = '''
G7 B7 B2 G2 G4 D4
G7 B7 B2 G2
B7 G7 D7 D2
G7 B7 B2 B5 G5
E7 C7 C5 B5 C5 C2 E2
F5 C5 C2 F2
C5 C2 C4 E4 E2
C6 E6 E4 C4 E4 E2 C2
B6 B4 D6 B4 D2 B4 B2
B2 E2
D6 D3
D6 B6 B4 D4 D2 B2
C2 F2
B2 B5 D5 D2 D5 F5 F2
E7 C7 C5 E5 E3 C3 C5 E5 E7
D7 F7 F5 G5 F5 F2 D2
'''
music = text.strip().replace('\n', '\n ').split(' ')

print (music)
NOTES = 'C#D#EF#G#A#B'
flag = ''
for pitch in music:
	note = NOTES.index(pitch[0])
	octave = int(pitch[1])
	numb = note + ((octave + 1)  * 12)
	#print(note, octave, numb, chr(numb))
	flag += chr(numb) + (pitch[2] if len(pitch) == 3 else '')

print(flag)
