rimska = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
def to_arab(rom):
    arab = 0
    for i, r in rimska:
        while rom.startswith(r):
            arab += i
            rom = rom[(len(r)):]
    return arab
rom = input()
print(to_arab(rom))