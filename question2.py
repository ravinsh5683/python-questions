dict1 =	{
  "1": "name1",
  "2": "name2",
  "3": "name3",
  "4": "name1",
  "5": "name2",
  "6": "name3",
  "7": "name1",
  "8": "name2",
  "9": "name3",
  "10": "name1",
  "11": "name2",
  "12": "name3",
  "13": "name1",
  "14": "name2",
  "15": "name3",
  "16": "name1",
  "17": "name2",
  "18": "name3",
}
dict2= {
    "1" : 50,
    "2" : 60,
    "3" : 70,
    "4" : 500,
    "5" : 600,
    "6" : 700,
    "7" : 510,
    "8" : 601,
    "9" : 701,
    "10" : 504,
    "11" : 606,
    "12" : 707,
    "13" : 508,
    "14" : 606,
    "15" : 705,
    "16" : 5044,
    "17" : 6032,
    "18" : 7021,
}
key_max = max(dict2.keys(), key=(lambda k: dict2[k]))
print("maximum_value :",dict2[key_max])
