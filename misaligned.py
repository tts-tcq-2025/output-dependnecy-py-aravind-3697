
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    return len(major_colors) * len(minor_colors)


def test_total_combinations():
    result = print_color_map()
    assert(result == 25)
    
def test_duplicate_colors():
    major = ["White", "Red", "Black", "Yellow", "Violet"]
    minor = ["Blue", "Orange", "Green", "Brown", "Slate"]
    assert len(set(major)) == len(major)
    assert len(set(minor)) == len(minor)
    assert set(major).isdisjoint(set(minor))


if __name__ == "__main__":
    test_total_combinations()
    test_duplicate_colors()
    print("All is well (maybe!)")
