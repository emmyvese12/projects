# displays the bar graph for the total dollars each Broadway show made in the first week of January

# using seaborn
import csv
import matplotlib.pyplot as plt
import seaborn as sns


def gross_dollars_each_show_week1(filename):
    reader = csv.reader(open(filename))
    new_list = []
    for line in reader:
        if line[0] == "4":
            line.pop()  
            new_list.append(line[4])
            new_list.append(line[9])
    end = len(new_list)
    keys = new_list[0:end:2] #start, end, step
    values = new_list[1:end:2]
    a_dict = {key:value for key,value in zip(keys,values)}
    return a_dict

dict = gross_dollars_each_show_week1("broadway.csv")

# get all the values fo the bar graph
guide = dict.get("A Gentleman'S Guide To Love And Murder")
aladdin = dict.get("Aladdin")
beautiful = dict.get("Beautiful")
car = dict.get("Cabaret '14")
chicago = dict.get("Chicago")
cinderella = dict.get("Cinderella")
cons = dict.get("Constellations")
dis = dict.get("Disgraced")
hed = dict.get("Hedwig And The Angry Inch")
vegas = dict.get("Honeymoon In Vegas")
if_t = dict.get("If/Then")
play = dict.get("It'S Only A Play")
jersey = dict.get("Jersey Boys")
boots = dict.get("Kinky Boots")
les = dict.get("Les Miserables '14")
mia = dict.get("Mamma Mia!")
mat = dict.get("Matilda")
motown = dict.get("Motown The Musical")
town = dict.get("On The Town 2014")
once = dict.get("Once")
pip = dict.get("Pippin")
rock = dict.get("Rock Of Ages")
show = dict.get("Side Show 2014")
book = dict.get("The Book Of Mormon")
curious = dict.get("The Curious Incident Of The Dog In The Night-Time")
elep = dict.get("The Elephant Man 2014")
illusion = dict.get("The Illusionists - Witness The Impossible")
ship = dict.get("The Last Ship")
king = dict.get("The Lion King")
opera = dict.get("The Phantom Of The Opera")
real = dict.get("The Real Thing 2014")
river = dict.get("The River")
tempt = dict.get("The Temptations And The Four Tops On Broadway")
youth = dict.get("This Is Our Youth")
wicked = dict.get("Wicked")
you = dict.get("You Can'T Take It With You")


def create_graph():
    sns.set_style("darkgrid")
    x = ["A Gentleman'S Guide To Love And Murder", "Aladdin", "Beautiful", "Cabaret '14", "Chicago", "Cinderella", "Constellations",
     "Disgraced", "Hedwig And The Angry Inch", "Honeymoon In Vegas", "If/Then", "It'S Only A Play", "Jersey Boys", "Kinky Boots",
     "Les Miserables '14", "Mamma Mia!", "Matilda", "Motown The Musical", "On The Town 2014", "Once", "Pippin", "Rock Of Ages",
     "Side Show 2014", "The Book Of Mormon", "The Curious Incident Of The Dog In The Night-Time", "The Elephant Man 2014",
     "The Illusionists - Witness The Impossible", "The Last Ship", "The Lion King", "The Phantom Of The Opera", "The Real Thing 2014",
     "The River", "The Temptations And The Four Tops On Broadway", "This Is Our Youth", "Wicked", "You Can'T Take It With You"]
     
    y = [int(guide), int(aladdin), int(beautiful), int(car), int(chicago), int(cinderella), int(cons), int(dis), int(hed), int(vegas),
     int(if_t), int(play), int(jersey), int(boots), int(les), int(mia), int(mat), int(motown), int(town), int(once), int(pip),
     int(rock), int(show), int(book), int(curious), int(elep), int(illusion), int(ship), int(king), int(opera), int(real), int(river),
     int(tempt), int(youth), int(wicked), int(you)]
     
    sns.barplot(y, x)
    return plt.show()
    
create_graph()
