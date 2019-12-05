import argparse
from natsort import natsorted


def check_positive_float(value, none_allowed=True):
    """
    Used in argparse to enforce positive floats
    FromL https://stackoverflow.com/questions/14117415
    :param value: Input value
    :param none_allowed: If false, throw an error for None values
    :return: Input value, if it's positive
    """
    ivalue = value
    if ivalue is not None:
        ivalue = float(ivalue)
        if ivalue < 0:
            raise argparse.ArgumentTypeError(
                "%s is an invalid positive value" % value
            )
    else:
        if not none_allowed:
            raise argparse.ArgumentTypeError("%s is an invalid value." % value)

    return ivalue


def check_positive_int(value, none_allowed=True):
    """
    Used in argparse to enforce positive ints
    FromL https://stackoverflow.com/questions/14117415
    :param value: Input value
    :param none_allowed: If false, throw an error for None values
    :return: Input value, if it's positive
    """
    ivalue = value
    if ivalue is not None:
        ivalue = int(ivalue)
        if ivalue < 0:
            raise argparse.ArgumentTypeError(
                "%s is an invalid positive value" % value
            )
    else:
        if not none_allowed:
            raise argparse.ArgumentTypeError("%s is an invalid value." % value)

    return ivalue


def remove_empty_string_list(str_list):
    """
    Removes any empty strings from a list of strings
    :param str_list: List of strings
    :return: List of strings without the empty strings
    """
    return list(filter(None, str_list))


def get_text_lines(
    file, return_lines=None, rstrip=True, sort=False, remove_empty_lines=True
):
    """
    Return only the nth line of a text file
    :param file: Any text file
    :param return_lines: Which specific line/lines to read
    :param rstrip: Remove trailing characters
    :param sort: If true, naturally sort the data
    :param remove_empty_lines: If True, ignore empty lines
    :return: The nth line
    """
    with open(file) as f:
        lines = f.readlines()
    if rstrip:
        lines = [line.strip() for line in lines]
    if remove_empty_lines:
        lines = remove_empty_string_list(lines)
    if sort:
        lines = natsorted(lines)
    if return_lines is not None:
        lines = lines[return_lines]
    return lines
