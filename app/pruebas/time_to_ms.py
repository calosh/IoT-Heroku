from datetime import datetime

'''
d = datetime.strptime("20.12.2016 09:38:42,76", "%d.%m.%Y %H:%M:%S,%f").strftime('%s')
d_in_ms = int(d)*1000
print(d_in_ms)

print(datetime.fromtimestamp(float(d)))


# https://www.saltycrane.com/blog/2008/06/how-to-get-current-date-and-time-in/


# 2017-11-28
aux = '2017-11-28'
splitAux = aux.split("-")
splitAux = str('{0}.{1}.{2}').format(splitAux[2], splitAux[1],splitAux[0])
splitAux = splitAux+" 00:00:00,00"
print(splitAux)


d = datetime.strptime(splitAux, "%d.%m.%Y %H:%M:%S,%f").strftime('%s')
d_in_ms = int(d)*1000
print(d_in_ms)

'''
def time_to_ms(time):
    splitAux = time.split("-")
    splitAux = str('{0}.{1}.{2}').format(splitAux[2], splitAux[1], splitAux[0])
    splitAux = splitAux + " 00:00:00,00"
    d = datetime.strptime(splitAux, "%d.%m.%Y %H:%M:%S,%f").strftime('%s')
    d_in_ms = int(d) * 1000

    return d_in_ms


#print(time_to_ms('2018-1-1'))