#!/usr/bin/python3
import csv
from urllib.request import urlopen
import collections
from bokeh.plotting import figure, save, output_file
import codecs

colours = {'Rich':"yellow",
           'Harry':'blue',
           'Jack':'green',
           'Mike':'magenta',
           'Bekki':'red',
           'Jones':'black'}
full_distance = 4000

def get_csv():
    url = 'https://frrt.org/tcrno5/data/riders.csv'
    response = urlopen(url)
    csv_file = csv.reader(codecs.iterdecode(response, 'utf-8'))
    data = {}
    try:
        for split in csv_file:
            if '#' not in split:
                data[split[1]] = split
        return data
    except IndexError:
        return None

def draw_plot(distances):
    to_draw = []
    for name, riders in distances.items():
        for rider in riders:
            position, _, rider_name, _,_,dtf,next_control,nckm,trackkm,routekm,av_track,av_speed,_ = rider
            to_draw.append((name,rider_name,float(dtf)))
    sorted_draw = sorted(to_draw, key=lambda x:x[2],reverse=True)
    rider_names = [item[1] for item in sorted_draw]
    dot = figure(title="Leaderboard",tools="hover",y_range=rider_names,x_range=[0,full_distance])
    for idx,(name,rider,distance) in enumerate(sorted_draw):
        rider=idx+1
        draw_distance = full_distance - distance
        dot.segment(0,rider,draw_distance,rider,line_width=2, line_color=colours[name])
        dot.circle(draw_distance,rider,size=5,fill_color=colours[name], line_color=colours[name],line_width=3, legend=name)
    output_file("/home/ubuntu/leaderboard.html")
    save(dot)


def get_names_from_csv(csv):
    data = {'Rich':[230,59,139,204,216],
    'Jack':[52,155,137,4,86],
    'Bekki':[152,71,198,151,158],
    'Harry':[118,162,22,159,125],
    'Mike':[106,105,169,222,117],
    'Jones':[165,81,33,85,44]}

    actual_data = collections.defaultdict(list)
    for name,riders in data.items():
        for rider in riders:
            if str(rider) in csv.keys():
                actual_data[name].append(csv[str(rider)])
    return actual_data

csv = get_csv()
if csv:
    names = get_names_from_csv(csv)
    draw_plot(names)
else:
    draw_plot({})
