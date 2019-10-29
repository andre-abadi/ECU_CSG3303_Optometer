# Introduction
This program generates a text file of random vehicle registration plate combinations that are valid in Western Australia. The scope of generation is limited to standard aluminium plates with the blue Western Australia top-bar. Plates are either custom, which is between 3 and 7 characters with the leading character not being a space, or a standard plate. Standard plates are generated according to contsraints known at the time of this program being made, and commented accordingly. Global variables are used to limit number of combinations generated, specify output file and define the maximum possible length of a combination.

# Installation
1. `sudo apt install python3 git`

# Usage
1. Execute `python3 generator.py`
2.  Enter the number of plates to be generated. `How many plates? Default is 5:`
3.  Enter the desired file to be written by the program. `Which file to write to? Default is output.txt:`
4.  Enter the plate type to be generated. `Plate type to generate? Default is 1:`

## Plate Types
At this time the interactivity of plate type selection is rudimentary. The user should read `generator.py` but a summary is provided below:
1. Standard WA plate in the format 1ABC123
    - Number 1
    - Letter A-G
    - 2 random letters
    - 3 random numbers
2. Custom WA plate in the format ABCDEFG
    - Minimum length of 3 alphanumeric characters
    - Spaces do not count towards minimum characters
    - Maximum of 7 alphanumeric characters
    - May not start with a space
3. First half of standard WA plate in the format 1ABC
4. Second half of standard WA plate in the format 123
