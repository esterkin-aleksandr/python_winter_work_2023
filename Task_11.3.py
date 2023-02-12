def rimska(arab):
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thous = ["", "M", "MM", "MMM", "MMMM"]

    t = thous[arab // 1000]
    h = hunds[arab // 100 % 10]
    te = tens[arab // 10 % 10]
    o = ones[arab % 10]

    return t + h + te + o


arab = int(input('Введите год: '))
print('По-римски:', rimska(arab))