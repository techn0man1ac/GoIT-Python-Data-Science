for i in range(16):
    s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
    print(s)

'''
int: 0;  hex: 0x0;  oct: 0o0;  bin: 0b0
int: 1;  hex: 0x1;  oct: 0o1;  bin: 0b1
int: 2;  hex: 0x2;  oct: 0o2;  bin: 0b10
int: 3;  hex: 0x3;  oct: 0o3;  bin: 0b11
int: 4;  hex: 0x4;  oct: 0o4;  bin: 0b100
int: 5;  hex: 0x5;  oct: 0o5;  bin: 0b101
int: 6;  hex: 0x6;  oct: 0o6;  bin: 0b110
int: 7;  hex: 0x7;  oct: 0o7;  bin: 0b111
int: 8;  hex: 0x8;  oct: 0o10;  bin: 0b1000
int: 9;  hex: 0x9;  oct: 0o11;  bin: 0b1001
int: 10;  hex: 0xa;  oct: 0o12;  bin: 0b1010
int: 11;  hex: 0xb;  oct: 0o13;  bin: 0b1011
int: 12;  hex: 0xc;  oct: 0o14;  bin: 0b1100
int: 13;  hex: 0xd;  oct: 0o15;  bin: 0b1101
int: 14;  hex: 0xe;  oct: 0o16;  bin: 0b1110
int: 15;  hex: 0xf;  oct: 0o17;  bin: 0b1111
'''
width = 5
for num in range(12):
    print(f'{num:^10} {num**2:^10} {num**3:^10}')
'''
    0          0          0
    1          1          1
    2          4          8
    3          9          27
    4          16         64
    5          25        125
    6          36        216
    7          49        343
    8          64        512
    9          81        729
    10        100        1000
    11        121        1331
'''