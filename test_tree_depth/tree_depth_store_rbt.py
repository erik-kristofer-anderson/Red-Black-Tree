from Tree import Tree
from Node import Node
import random
import matplotlib.pyplot as plt
import datetime

print("creating trees")
tree_height_dict = {}
repetitions = 200
num_elements_start = 5
num_elements_stop = 100
num_elements_step = 5
save = True
show_plot = False
plot_point_size_factor = 1

for num_elements in range(num_elements_start, num_elements_stop, num_elements_step):
    print(f"num_elements = {num_elements}")
    tree_height_dict[num_elements] = []
    for _ in range(repetitions):
        red_black_tree_1 = Tree()
        for i in range(num_elements):
            x = random.randint(1, num_elements * 5)
            red_black_tree_1.add_red_black_node(Node(x))
        y = red_black_tree_1.find_tree_depth()
        tree_height_dict[num_elements].append(y)

print("crunching numbers")
list_of_tuples_of_num_elements_and_heights_histograms = []
for num_elements, list_of_heights in tree_height_dict.items():
    print(f"num_elements = {num_elements}")
    heights_histogram = dict()
    for height in list_of_heights:
        if height in heights_histogram:
            heights_histogram[height] += 1
        else:
            heights_histogram[height] = 1
    # for height in heights_histogram:
    # print(f'num elements: {num_elements}, height: {height}, count: {round(heights_histogram[height] / repetitions * 100, 1)}%')
    tuple_of_num_elements_and_heights_histogram = (num_elements, heights_histogram)
    list_of_tuples_of_num_elements_and_heights_histograms.append(tuple_of_num_elements_and_heights_histogram)
    print()

list_n_values = []  # num elements
list_h_values = []  # tree height
list_z_values = []  # relative weight of that height

for heights_histogram in list_of_tuples_of_num_elements_and_heights_histograms:

    for tuple_of_num_elements_and_heights_histogram in list_of_tuples_of_num_elements_and_heights_histograms:
        n = tuple_of_num_elements_and_heights_histogram[0]
        heights_histogram = tuple_of_num_elements_and_heights_histogram[1]
        for height, percentage in heights_histogram.items():
            list_n_values.append(n)
            list_h_values.append(height)
            list_z_values.append(percentage * plot_point_size_factor)

x = list_n_values
y = list_h_values
z = list_z_values




if save:
    with open(f"data_rbt/depth_results_{datetime.datetime.now()}_metadata.txt", 'w') as file:
        s = ""
        s += f"num_elements range: {num_elements_start, num_elements_stop, num_elements_step}\n"
        s += f"repetitions per each num_elements: {repetitions}\n"
        file.write(s)
        file.close()

    with open(f"data_rbt/depth_results_{datetime.datetime.now()}.txt", 'w') as file:
        for i in range(len(list_n_values)):
            file.write(f"{list_n_values[i]},{list_h_values[i]},{list_z_values[i]}\n")
        file.close()

plt.scatter(x, y, z)
plt.xlabel('number of elements in tree')
plt.ylabel('height of tree')
plt.title("Tree Height vs Number of Elements in Red Black Tree")
s = ""
s += f"num_elements range: {num_elements_start, num_elements_stop, num_elements_step}\n"
s += f"repetitions per each num_elements: {repetitions}\n"
s += "(circle size corresponds to relative occurrence)"
plt.annotate(s, xy=(int(num_elements_stop * .3), 2), xycoords='data')
plt.grid(axis='x')
if save:
    plt.savefig(f"data_rbt/depth_results_{datetime.datetime.now()}_plot.pdf")
if show_plot:
    plt.show()
