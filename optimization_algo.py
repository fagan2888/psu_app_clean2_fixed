__author__ = 'zwhitman'

import csv

with open("C:\\Users\\zwhitman\\Documents\census\\optimization_algorithm\\test_shapefiles\\test_1_table.csv", 'rb') as csvfile:
    state_table = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in state_table:
        test = ', '.join(row)

# create dictionary or arrary (not sure yet) of neighboring counties pop and income
# dictionary to use key value as geoid
popvals = (900, -250, -800, 492, -1000)
popdict = {1: 900, 2: -250, 3: -800, 4: 492, 5: -1000}

# create variable for selected counties value
pop_county = 1050
pop_county_inverse = pop_county * -1
print pop_county_inverse

# identify geoid from dictionary that is the closest match
# print popdict.get(pop_county_inverse, popdict[min(popdict.keys(), key=lambda k: abs(k-pop_county_inverse))])
# print popdict.get(pop_county_inverse) or popdict[min(popdict.keys(), key=lambda k: abs(k-pop_county_inverse))]
f = lambda a, l: min(l, key=lambda x: abs(x-a))
num = pop_county_inverse
result1 = f(num, popvals)

diffmatch = abs(result1)-abs(pop_county_inverse)

# check if match is close enough
if abs(diffmatch) < 500:
    # do something
    print "all set"
else:
    # do something
    print sum(popvals[0:1])

# def info_check():
#     info_label = arcpy.SearchCursor(name1, fields="Name_1; ALANDSQM; POP; INCOME; POPULATION")
#     for row in info_label:
#         print("GEOID: {0}, County: {1}, Area: {2}, Pop. Density: {3}, Income: {4}, Population: {5}".format(
#             row.getValue("GEOID"),
#             row.getValue("Name_1"),
#             row.getValue("ALANDSQM"),
#             row.getValue("POP"),
#             row.getValue("INCOME"),
#             row.getValue("POPULATION")
#         ))
#     graph = arcpy.Graph()
#     graph.addSeriesScatterPlot(name1, fieldY="POP", fieldX="INCOME")
#     arcpy.MakeGraph_management(arcpy.GraphTemplate(), graph, out_graph_name="graph_output.grf")
