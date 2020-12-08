from aocd import data
import re

def parse_rules(data):
    bags = {} # Maps bag type to contents; contents are dict mapping bag type to quantity
    rules = data.split('\n')
    for r in rules:
        contents = {}
        m = re.match('(.*) bags contain', r)
        bag_type = m.group(1)
        if 'no other bags' not in r:
            m = re.match(r'.*contain (.*?)\.$', r)
            insides = m.group(1).split(', ')

            for e in insides:
                m = re.match(r'(\d+) (.*?) bag', e)
                num = int(m.group(1))
                inside_type = m.group(2)
                contents[inside_type] = num

        bags[bag_type] = contents
    return bags

def check_valid(have_bag_type, check_bag_type, bag_rules):
    """Check if have_bag_type can be held in check_bag_type, recursively"""
    valid = False

    check_contents = bag_rules[check_bag_type]
    if have_bag_type == check_bag_type:
        pass
    elif have_bag_type in check_contents.keys():
        valid = True
#        print("{} can be held directly in {}".format(have_bag_type, check_bag_type))
    else:
        for check_contents_bag_type in (check_contents.keys() - have_bag_type):
            valid = check_valid(have_bag_type, check_contents_bag_type, bag_rules)
            if valid:
#                print("{} can be held indirectly in {} through {}".format(have_bag_type, check_bag_type, check_contents_bag_type))
                break

    return valid

def part_a(data):
    bag_rules = parse_rules(data)

    valid = []
    for check_bag_type in bag_rules.keys():
        is_valid = check_valid('shiny gold', check_bag_type, bag_rules)
        if is_valid:
            valid.append(check_bag_type)

    return str(len(valid))

def count_bags(bag_type, bag_rules):
    """Given a bag type, recursively count how many bags it has to contain"""
    bag_sum = 0

    contents = bag_rules[bag_type]
    if contents:
        #print("{} should have {}".format(bag_type, contents))
        bag_sum = sum( [v * (1 + count_bags(k, bag_rules)) for k,v in contents.items()] )

    #print("{} holds {} bags".format(bag_type, bag_sum))

    return bag_sum

def part_b(data):
    bag_rules = parse_rules(data)
    return str(count_bags('shiny gold', bag_rules))

test_data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

test_data_b = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

if __name__ == "__main__":
    assert part_a(test_data) == "4"
    assert part_b(test_data) == "32"
    assert part_b(test_data_b) == "126"
    print(part_a(data))
    print(part_b(data))
