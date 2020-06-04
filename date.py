def convertGetDate(dateFormat):
    turkish={'ğ':'g','ş':'s','ı':'i','ü':'u'}
    for temp1,temp2 in turkish.items():
        dateFormat=dateFormat.replace(temp1,temp2)
    dictOfDates = {"Ocak":"01",
           "Şubat":"02",
           "Mart":"03",
           "Nisan":"04",
           "Mayıs":"05",
           "Haziran":"06",
           "Temmuz":"07",
           "Ağustos":"08",
           "Eylül":"09",
           "Ekim":"10",
           "Kasım":"11",
           "Aralik":"12"
            }
    return dictOfDates[dateFormat]