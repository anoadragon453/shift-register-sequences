#!/usr/bin/env python3

lfsr = 0xACE1
bit = 0
period = 0
cycle_set = []

# Iterate through lsfr periods until we loop back to the same seed (starting value)
while True:
    # taps: 16 14 13 11; characteristic polynomial: x^16 + x^14 + x^13 + x^11 + 1
    bit = ((lfsr >> 0) ^ (lfsr >> 2) ^ (lfsr >> 3) ^ (lfsr >> 5)) & 1
    lfsr = (lfsr >> 1) | (bit << 15)
    period += 1
    cycle_set.append(str(bit))
    if lfsr == 0xACE1:
        break

# Print out the cycle set
print(''.join(cycle_set))
