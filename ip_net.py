#!/usr/bin/env python3

# convert network address to bin

network = input('Type network in format 10.1.1.0/24: ')

ip, mask = network.split('/')

ip_ad = ip.split('.')

bin_mask = '1' * int(mask) + '0' * (32 - int(mask))

net_output = '''
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''

mask_output = '''
Mask:
/{0}
{1:<8}  {2:<8}  {3:<8}  {4:<8}
{1:<08b}  {2:<08b}  {3:<08b}  {4:<08b}
'''

print(net_output.format(int(ip_ad[0]), int(ip_ad[1]), int(ip_ad[2]), int(ip_ad[3])))
print(mask_output.format(mask, int(bin_mask[0:8], 2), int(bin_mask[8:16], 2), int(bin_mask[16:24], 2), int(bin_mask[24:32], 2),))
