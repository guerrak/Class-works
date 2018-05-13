
str = 'X-DSPAM-Confidence:0.8475'
atpos = str.find(':')
host = str[atpos + 1:]
host = host.lstrip()
host = float(host)
print(host)
