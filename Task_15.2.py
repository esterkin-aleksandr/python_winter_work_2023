import re
st=' И123BC78  У321ТХ78  У223ОХ78  Р220ОО178  A123BC99  П123BC56'
print(re.findall(r'\b[А, В, Е, К, М, Н, О, Р, С, Т, У, Х, A, B, E, K, M, H, O, H, C, T, Y, X]\d\d\d[А, В, Е, К, М, Н, О, Р, С, Т, У, Х, A, B, E, K, M, H, O, H, C, T, Y, X]{2}1?78\b',st))