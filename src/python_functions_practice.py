def return_10():
    return 10

# def add (needs 2 parameters):

def add(int1, int2):
    return int1 + int2

def subtract(int1, int2):
    return int1 - int2

def multiply(int1, int2):
    return int1 * int2

def divide(int1, int2):
    return int1 / int2

def length_of_string(string):
    return len(string)

def join_string (string1, string2):
    return string1 + string2

def add_string_as_number (str1, str2):
    return int(str1) + int(str2)

def number_to_full_month_name (num): 
    calendar = {
        1 : 'January',
        2 : 'February',
        3 : 'March',
        4 : 'April',
        5 : 'May',
        6 : 'June',
        7 : 'July',
        8 : 'August' ,
        9 : 'September',
        10 : 'October',
        11 : 'November',
        12 : 'December'
    }
    return calendar[num]

def number_to_short_month_name (num): 
    calendar = {
        1 : 'Jan',
        2 : 'Feb',
        3 : 'Mar',
        4 : 'Apr',
        5 : 'May',
        6 : 'Jun',
        7 : 'Jul',
        8 : 'Aug' ,
        9 : 'Sep',
        10 : 'Oct',
        11 : 'Nov',
        12 : 'Dec'
    }
    return calendar[num]

def calculate_cube_volume(side_length):
    return side_length * side_length * side_length

def reverse_string(string):
    return string[::-1]

def convert_farenheit_to_celsius(integer):
    return (integer - 32) * 5 / 9