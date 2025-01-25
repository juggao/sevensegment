# Define the segment patterns for each digit (0-9)
segments = {
    '0': ['a', 'b', 'c', 'd', 'e', 'f'],
    '1': ['b', 'c'],
    '2': ['a', 'b', 'g', 'e', 'd'],
    '3': ['a', 'b', 'g', 'c', 'd'],
    '4': ['f', 'g', 'b', 'c'],
    '5': ['a', 'f', 'g', 'c', 'd'],
    '6': ['a', 'f', 'g', 'c', 'd', 'e'],
    '7': ['a', 'b', 'c'],
    '8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    '9': ['a', 'b', 'c', 'd', 'f', 'g']
}

# Function to display a single digit
def display_digit(digit):
    # Define the representation of each segment
    segment_map = {
        'a': ' -- ',
        'b': '|  ',
        'c': '|  ',
        'd': ' -- ',
        'e': '|  ',
        'f': '|  ',
        'g': ' -- '
    }

    # Create a 5-line representation of the digit
    lines = [
        ' ' + ('a' in segments[digit] and segment_map['a'] or '    '),
        ('f' in segments[digit] and segment_map['f'] or ' ') + ('b' in segments[digit] and segment_map['b'] or '  '),
        ' ' + ('g' in segments[digit] and segment_map['g'] or '    '),
        ('e' in segments[digit] and segment_map['e'] or ' ') + ('c' in segments[digit] and segment_map['c'] or '  '),
        ' ' + ('d' in segments[digit] and segment_map['d'] or '    ')
    ]

    # Print the digit
    for line in lines:
        print(line)

# Function to display two digits side by side
def display_two_digits(digit1, digit2):
    # Get the segment representations for both digits
    lines1 = [
        ' ' + ('a' in segments[digit1] and '--' or '  '),
        ('f' in segments[digit1] and '|' or ' ') + ('b' in segments[digit1] and '  |' or '   '),
        ' ' + ('g' in segments[digit1] and '--' or '  '),
        ('e' in segments[digit1] and '|' or ' ') + ('c' in segments[digit1] and '  |' or '   '),
        ' ' + ('d' in segments[digit1] and '--' or '  ')
    ]

    lines2 = [
        ' ' + ('a' in segments[digit2] and '--' or '  '),
        ('f' in segments[digit2] and '|' or ' ') + ('b' in segments[digit2] and '  |' or '   '),
        ' ' + ('g' in segments[digit2] and '--' or '  '),
        ('e' in segments[digit2] and '|' or ' ') + ('c' in segments[digit2] and '  |' or '   '),
        ' ' + ('d' in segments[digit2] and '--' or '  ')
    ]

    # Print the two digits side by side
    for l1, l2 in zip(lines1, lines2):
        print(l1 + '   ' + l2)

# Display the numbers 6 and 8
print("Displaying 6 and 8:")
display_two_digits('6', '8')