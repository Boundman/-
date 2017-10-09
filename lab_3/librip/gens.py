import random


def gen_random(min, max, num_count):
    for x in range(num_count):
        yield random.randint(min, max)

#def gen_random(min, max, num_count):
    #arr = [random.randint(min, max) for i in range(num_count)]
    #return [random.randint(min, max) for i in range(num_count)]


def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        for item in items:
            if args[0] in item:
                yield item[args[0]]
    elif len(args) > 1:
        for item in items:
            dict = {}
            for arg in args:
                if arg in item:
                    dict[arg] = item[arg]
            if dict:
                yield dict


