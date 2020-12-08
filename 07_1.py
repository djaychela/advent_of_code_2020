import pathlib

file_name = "07_test.txt"
current_dir = pathlib.Path(__file__).parent.absolute()
file_path = pathlib.Path(current_dir / "data" / file_name)

with open(file_path, "r") as file:
    bags = file.readlines()

bag_colours = {}
for bag in bags:
    outer, inner = bag.split("contain")
    outer = ' '.join(outer.split()[:2])
    inner_dict = {}
    inner_contents = inner.split(',')
    for content in inner_contents:
        try:
            number = int(content.split()[0])
        except ValueError:
            number = 0
        colour = ' '.join(content.split()[1:3])
        inner_dict[colour]=number
    if outer not in bag_colours.keys():
        bag_colours[outer] = inner_dict


def replace_contents(bag):
    bag_contents = bag_colours[bag].items()
    for content in bag


for bag in bag_colours.keys():
    print(bag, bag_colours[bag])
    new_bag_contents = {}
    for bag_colour, amount in bag_colours[bag].items():
        print(bag_colour, amount)
        print(bag_colours[bag_colour])
        # present_new_contents = bag_colours[bag_colour].keys()
        # present_new_amount = bag_colours[bag_colour].values() * amount
        # print(present_new_contents, present_new_amount)
