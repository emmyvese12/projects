"""
Emmy Veselinov
Project 3: Working with CSV file
"""
# extracted data on Broadway shows over weeklong periods in January 2015

import csv

def find_total(filename):
    reader = csv.reader(open(filename))
    total = 0
    for line in reader:
        # each line has a list of all the data
        last_cat = len(line)-1 
        if line[last_cat] != "Statistics.Performances": # exclude the title of the category
            total = total + int(line[last_cat])
    return total

def diff_show_dict(filename):
    reader = csv.reader(open(filename))
    num_perf_per_week = {}
    l = []
    for line in reader:
        day_of_perf = line[0]
        if line[0] != "Date.Day":
            l.append(day_of_perf)
    # l contains the days for each performance
    # do a bag of words analysis to count the number of performances per week
    for day in l: # each day represents a different show
        num_perf_per_week.setdefault(day,0)
        num_perf_per_week[day] = num_perf_per_week[day] + 1
    return num_perf_per_week
        

def find_total_each_week(filename):
    reader = csv.reader(open(filename))
    week1 = 0
    week2 = 0
    week3 = 0
    week4 = 0
    for line in reader:
        if line[0] == "4": # line[0] is the day of the performance
            week1 = week1 + int(line[len(line)-1]) # the last category is the number of performances that occured that week
        elif line[0] == "11":
            week2 = week2 + int(line[len(line)-1])
        elif line[0] == "18":
            week3 = week3 + int(line[len(line)-1])
        elif line[0] == "25":
            week4 = week4 + int(line[len(line)-1])
        else:
            pass
    return week1, week2, week3, week4
        
        
def show_dict(filename, category):
    reader = csv.reader(open(filename))
    show_names_dict = {}
    l = []
    for line in reader:
        show_names = line[4]
        if show_names != category:
            l.append(show_names)
    for show in l: 
        show_names_dict.setdefault(show,0) # set the value to 0 for all shows
        show_names_dict[show] = show_names_dict[show] + 1 # then add one for each show 
    return show_names_dict

def unique_shows(filename, category):
    show_names_dict = show_dict(filename, category)
    unique = show_names_dict.keys()
    num_of_unique_shows = len(unique)
    return num_of_unique_shows
        
        
def sum_attend(filename): # total number of people who attended the performances in January
    reader = csv.DictReader(open(filename))
    result_l = []
    for row in reader:
        result_l.append(row)
    attendance = [ int(x["Statistics.Attendance"]) for x in result_l ]
    return sum(attendance)

def sum_attend_compare(filename1, filename2): # comparing two csv files together
    if sum_attend(filename1) > sum_attend(filename2):
        result = str(sum_attend(filename1)) + " people attended Broadway shows in January, which is greater than " + str(sum_attend(filename2)) + ", the attendance for February."
    else:
        result = str(sum_attend(filename2)) + " people attended Broadway shows in February, which is greater than ", str(sum_attend(filename1)) + ", the attendance for January."
    return result

        
if __name__ == "__main__":
    print("DATA ANALYSIS:")
    print("------------------------------------------------------------")
    print("The total number of Broadway performances in January were", str(find_total("broadway.csv")) + ".")
    print("The average number of Broadway performances in January were", find_total("broadway.csv")/4, "rounding to", str(round(find_total("broadway.csv")/4)) + ".")
    print("------------------------------------------------------------")
    print("The total number of Broadway performances in the first week of January were", str(find_total_each_week("broadway.csv")[0]) + ".")
    print("The total number of Broadway performances in the second week of January were", str(find_total_each_week("broadway.csv")[1])+ ".")
    print("The total number of Broadway performances in the third week of January were", str(find_total_each_week("broadway.csv")[2]) + ".")
    print("The total number of Broadway performances in the fourth week of January were", str(find_total_each_week("broadway.csv")[3]) + ".")
    print("------------------------------------------------------------")
    
    dictionary = diff_show_dict("broadway.csv")
    #print(dictionary.items())
    print("There were", dictionary.get("4"), "shows playing in the first week of January.")
    print("There were", dictionary.get("11"), "shows playing in the second week of January.")
    print("There were", dictionary.get("18"), "shows playing in the third week of January.")
    print("There were", dictionary.get("25"), "shows playing in the fourth week of January.")
    print("There were", unique_shows("broadway.csv", "Show.Name"), "different shows to choose from to attend in January.")
    print("------------------------------------------------------------")

    name_of_shows_dict = show_dict("broadway.csv", "Show.Name") #dictionary of the number of weeks each show was performed
    #print(name_of_show_dict.items())
    print("In the month of January, Motown The Musical was performed", str(name_of_shows_dict.get("Motown The Musical")) + "/4 weeks.") # out of the 4 weeks
    print("In the month of January, The Phantom Of The Opera was performed", str(name_of_shows_dict.get("The Phantom Of The Opera")) + "/4 weeks.")
    print(sum_attend_compare("broadway.csv", "broadway_feb.csv"))