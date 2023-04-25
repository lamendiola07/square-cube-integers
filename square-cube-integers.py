# Mendiola, Logie A. | BSCPE 1-5 | Object-Oriented Programming | Assignment #4: P-4

# Write a method in python that will create two separate text files after reading the source text file named integers.txt that contains 20 integers
# The first output file will be named double.txt containing the square of all even integers found in integers.txt
# The second file will be named triple.txt containing the cube of all odd numbers found in the integers.txt.

 # create method to open text files: integers.txt, double.txt , and triple.txt
with open("integers.txt") as integer_file, open("double.txt", "a") as square_even_integers, open("triple.txt", "a") as cube_odd_integers:

# read integerss.txt to determine integer placement
    for line in integer_file:
        line_placement = int(line)

        # if integer line placement is even,
        if line_placement % 2 == 0:
            even_integers = line_placement

            #squaring even integers
            even_integers = even_integers * even_integers

            # overwrites to double.txt
            square_even_integers.write(str(even_integers) + '\n')
        
        # if integer line placement is odd,
        else:
            odd_integers = line_placement

            #cubing odd integers
            odd_integers = odd_integers * odd_integers * odd_integers

            #overwrites to triple.txt
            cube_odd_integers.write(str(odd_integers) + '\n')