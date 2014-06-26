#-*- coding: UTF-8 -*-
import json
import urllib
import sys
import re

def main():

    #check command line 
    if len( sys.argv ) != 5:
        print 'Argument Error!! please type TOC_HW3.py <url> <dist> <road> <year>'
        sys.exit(0)
    else:
        url, dist, road, year = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    web = urllib.urlopen(url)
    data = json.load(web)

    #change tpyein into unicode
    dist = unicode(dist, "utf-8")
    road = unicode(road, "utf-8")
    year = unicode(year, "utf-8")

    getDist = unicode("鄉鎮市區", "utf-8")
    getRoad = unicode("土地區段位置或建物區門牌", "utf-8")
    getYear = unicode("交易年月", "utf-8")
    getPrice = unicode("總價元", "utf-8")

    aim1 = re.compile(dist)
    aim2 = re.compile(road)

    count = 0
    totalMoney = 0

    for i in range(len(data)):
        matchDist = aim1.search(data[i][getDist])
        matchRoad = aim2.search(data[i][getRoad])

        aYear = str(data[i][getYear])
        if year <= int(aYear[:-2]):
            matchYear = True
        else:
            matchYear = False


        if matchDist and matchRoad and matchYear:
            print get
            count += 1
            aimDist = json.dumps(data[i][getDist], ensure_ascii = False).encode('utf-8')
            aimRoad = json.dumps(data[i][getRoad], ensure_ascii = False).encode('utf-8')
            aimYear = json.dumps(data[i][getYear], ensure_ascii = False).encode('utf-8')
            aimPrice = json.dumps(data[i][getPrice], ensure_ascii = False).encode('utf-8')
            totalMoney += data[i][getPrice]
            aimDist = re.sub('".*?"', r'\1', aimDist)
            aimRoad = re.sub('".*?"', r'\1', aimRoad)
            print aimDist + '   ' + aimRoad + '    ' + aimYear + aimPrice

    try:
        return int ( totalMoney / count ) 
    except ZeroDivisionError:
         print 0
         sys.exit(0)
    
    print 'avgMoney= ' + avgMoney


if __name__ == '__main__':
    main()
