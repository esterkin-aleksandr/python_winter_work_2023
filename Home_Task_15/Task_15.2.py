import re
st='И123BC78У321ТХ78 У223ОХ99В001ВВ178 УУ123В198 зы333ззз98 1111111198 131аНН78 аа223аа78 РР198РР78'
print(re.findall(r'[А, В, Е, К, М, Н, О, Р, С, Т, У, Х, A, B, E, K, M, H, O, H, C, T, Y, X]\d\d\d[А, В, Е, К, М, Н, О, Р, С, Т, У, Х, A, B, E, K, M, H, O, H, C, T, Y, X]{2}1?78',st))