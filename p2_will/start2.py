import csvReader

r = csvReader.csvHandler('zachbraff.csv')
t = r['times']

def zahle(h):
    result = {}
    for hs in h:
        if len(hs) > 2:
            if hs in result.keys():
                altval = result[hs]
                result[hs] = altval + 1
            else:
                result[hs] = 1
    return result
    
def zahleTime(timeList):
    result = {}
    zD = {}
    zM = {}
    zY = {}
    for time in timeList:
        if time != "":
            time = time[:-6]
            day = time
            time = time.split(".")
            month = time[1]
            year = time[2]
            month = str(year) + str(month)
            if year in zY.keys():
                altval = zY[year]
                zY[year] = altval + 1
            else:
                zY[year] = 1
            if month in zM.keys():
                altval = zM[month]
                zM[month] = altval + 1
            else:
                zM[month] = 1
            if day in zD.keys():
                altval = zD[day]
                zD[day] = altval + 1
            else:
                zD[day] = 1
    result['zy'] = zY
    result['zm'] = zM
    result['zd'] = zD
    return result  