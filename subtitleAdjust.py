subtitleFilePath = 'D:/Downloads/The Martian (2015) [3D] [HSBS] [YTS.AG]/The.Martian.2015.3D.HSBS.BluRay.x264-[YTS.AG]-tur.srt'
secondsToShift = '+1'
newString = ''

def adjustTime(timeLine, seconds):
    newList = []
    for timeunit in timeLine.split(':'):
        if ',' in timeunit:
            splittedTimeunit = timeunit.split(',')
            newSeconds = str(int(float(splittedTimeunit[0])+float(seconds)))
            if len(newSeconds) < 2:
                newSeconds = '0'+newSeconds
            newList.append(newSeconds+','+splittedTimeunit[1])
        else:
            newList.append(timeunit)
    return ':'.join(newList)


with open(subtitleFilePath, encoding="ISO-8859-1") as f:
    subtitleLines = f.readlines()

for line in subtitleLines:
    if '-->' in line:
        newString += adjustTime(line, secondsToShift)
    else:
        newString += line

with open(subtitleFilePath[:-4]+'(shifted).srt', 'w', encoding="ISO-8859-1") as f:
    f.write(newString)