#!/usr/bin/env python3
import subprocess

# Shifts the state to the left and returns outputted number
def shift_state(state, new_num):
    num = state[0]
    state = [state[1], state[2], state[3], new_num]
    return num, state

def insert_zero(seq):
    l = len(seq)
    for i in range(l):
        if str(z2_sequence[i % l]) + str(z2_sequence[(i + 1) % l]) + str(z2_sequence[(i + 3) % l]) == '000':
            seq.insert(i, 0)
            break
    return seq

# State that Z_2 and Z_5 LSFRs with start at
start_state = [0,0,0,1]

# Generate Z_2
# Our P(x): 3*x^4 + x + 1
# Our C(x): x^4 + x^3 + 3
# Our taps are {0,1}
state = start_state
field = 2
period = 2**4 # Period = field size ^ degree
z2_sequence = []

# Generate our Z2 de bruijn sequence
while (len(z2_sequence) < period): 
    # Apply operations to our state
    new_num = (state[0] + state[1]) % field
    
    # Shift state and get next number in the sequence
    (seq_value, state) = shift_state(state, new_num)

    # Append number to the overall sequence
    z2_sequence.append(seq_value)

# Insert 0 into the Z2 sequence to achieve 0000 state
#z2_sequence = insert_zero(z2_sequence)
'''
for i in range(l):
    if str(z2_sequence[i % l]) + str(z2_sequence[(i + 1) % l]) + str(z2_sequence[(i + 3) % l]) == '000':
        z2_sequence.insert(i, 0)
        break
'''

# Print out our sequence
print("Z2 sequence:", z2_sequence)

# Print out possible values
l = len(z2_sequence)
values = []
for i in range(l):
    values.append("%d%d%d%d" % (z2_sequence[i % l], z2_sequence[(i+1) % l], z2_sequence[(i+2) % l], z2_sequence[(i+3) % l]))
values.sort()
print("All Z2 values:", values)

# Generate Z_5
# Our P(x): 3*x^4 + 3*x^3 + 2*x + 1
# Our C(x): x^4 + 2*x^3 + 3*x + 3
# Our taps are {0,2(1), 3(3)}
state = start_state
field = 5
period = 5**4 # 625
z5_sequence = []

while (len(z5_sequence) < period - 1):
    # Apply operations to our state
    new_num = (-3 * state[0] - 4 * state[1] - 4 * state[2] - state[3]) % field

    # Shift state and get next number in the sequence
    (seq_value, state) = shift_state(state, new_num)

    # Append number to the overall sequence
    z5_sequence.append(seq_value)

# Insert 0 into the Z5 sequence to achieve 0000 state
z5_sequence = insert_zero(z5_sequence)

# Print out our sequence
print("Z5 sequence:", z5_sequence)

# Print out possible values
l = len(z5_sequence)
values = []
for i in range(l):
    values.append("%d%d%d%d" % (z5_sequence[i%l], z5_sequence[(i+1) % l], z5_sequence[(i+2) % l], z5_sequence[(i+3) % l]))
values.sort()
print("All Z5 values:", values)

# Generate our Z10 de bruijn sequence
field = 10
z10_sequence = []
for i in range(10003):
    z2 = z2_sequence[i % len(z2_sequence)]
    z5 = z5_sequence[i % len(z5_sequence)]
    if z2 == 0:
        z10 = z5
    else:
        z10 = z5 + 5
    z10_sequence.append(z10)

print("Z10 sequence:", z10_sequence)

# Check if our sequence is correct
# Write sequence to file
with open('seq.txt', 'w+') as f:
    for bit in z10_sequence:
        f.write(str(bit))

# Print generated values
values = []
for i in range(len(z10_sequence) - 3):
    values.append("%d%d%d%d" % (z10_sequence[i], z10_sequence[i+1], z10_sequence[i+2], z10_sequence[i+3]))
values.sort()
print("All possible values:", values)

print()
subprocess.run(['./Check_LE4.exe'])
