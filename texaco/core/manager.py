from .exception import ValidateFileLinesFormatException


def line_is_valid(line):
    """
    Validate each column of the param line.

    The line param must be in the format: ['N', 'N:N', 'N:N',...]

    Return True if the line is valid, else, return False
    """
    if not line:
        return False
    qty = None
    try:
        qty = int(line.pop(0))
        assert qty > 0
    except Exception:
        return False
    if len(line) != qty:
        return False
    for column in line:
        try:
            n1, n2 = column.split(':')
            assert int(n1) > -1
            assert int(n2) > -1
        except Exception:
            return False
    return True


def validate_file_reader(reader):
    """
    Convert the reader into a list and validate each line.

    If we found errors, raise ValidateFileLinesFormatException.

    If there are no errors, return the list of data.
    """
    lines = list(reader)
    errors = []
    for idx, line in enumerate(lines):
        if not line_is_valid(line):
            errors.append(idx + 1)
    if errors:
        raise ValidateFileLinesFormatException(errors)
    return lines


def follow_path(points, start_idx):
    """
    Reorder points order based on start_idx and check if can follow the path.

    If in some point the sum of the galons is less than the need to go forward,
    return False. If we pass for all the points, return True.
    """
    f = start_idx - len(points)
    r_points = points[start_idx:] + points[:f]
    sum_g = sum_c = 0
    for g, c in r_points:
        sum_g += g
        sum_c += c
        if sum_g < sum_c:
            return False
    return True


def get_best_route(data):
    """Sum the points and iterate over searching for the good one"""
    # turn the list of strings into a list of int pair tuples
    # eg: ['1:5', '3:2'] is turned into [(1,5), (3,2)]
    points = [[int(x), int(y)] for x, y in [i.split(':') for i in data]]
    # zip tuples to sum the values
    has, spend = zip(*points)
    # if spend is less than has, so it is an invalid point
    if sum(has) >= sum(spend):
        # iterate over the points to follow based on indexes
        for idx in range(len(points)):
            if follow_path(points, idx):
                # if found, return the first index ocurred
                return str(idx + 1)
    return 'impossible'


def get_routes_results(reader):
    """
    Iterate over the reader and return the best route for each data.

    Can raise ValidateFileLinesFormatException on validating the reader.
    """
    valid_data = validate_file_reader(reader)
    routes = []

    # fill routes list with best route for each valid data
    for data in valid_data:
        routes.append(get_best_route(data))

    return routes
