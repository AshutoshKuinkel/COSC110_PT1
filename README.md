<h1 style="text-align: center;">Name: Ash Kuinkel</h1>

## Purpose/Summary : 
The purpose of this assingment is to solve the client's problem, i.e. Codetown Public Pool requires a text-based point-of-sale system written in Python. The system should incorporate a main loop that runs continuously until the user indicates they wish to exit (by pressing Enter/entering an empty string at the start of a sale).

## How to Run:
Let's dive into how this program can be run. 

The program has been packaged in the form of a tarball, preserving all the current files, directories including structures, file permissions etc.
This was done using the command:

```bash
tar -zc readme.md pool.py > pt1.tgz
```

where z - puts archive through gzip & c - creates archive

To load the archived directory, files etc., run the command:

```bash
tar -zxf pt1.tgz 
```
where z - puts archive through gzip, x - extracts from archive (into current directory) & f - refers to name of archive i.e. pt1.tgz

The readme.md & pool.py will now be available in your current directory with the appropriate permissions to execute and read.

The next step is to confirm that you have python3 installed. Assuming our program is being tested on turing, we should already
have python 3 interpreter installed. To verify that python is installed, run the following command:

```bash
python --version
```

You should see an output similar to: ```Python 3.14.3```

NOTE : If for some reason you do not have python installed, then you will see an error message similar to this: ```bash: python: command not found```
In that case, you may need to install Python 3 (if you sudo privileges on your system), by running the command (assuming we are on fedora):

```bash
sudo dnf install python3
```

Now to read our program ```pool.py```, we are simply able to use:
``` bash
cat pool.py
```

To execute, run:
``` bash
python3 pool.py
```

To view readme.md file, run:
```bash
cat readme.md
```


## How Proposed solution adheres to marking criteria/client requirements:
The marking criteria/client requirements of this problem specifically require us:
 - Ensure we have adequate documentation (including comments in source)
 - Program running without hanging/crashing
 - Program handling valid input correctly
 - Program handling incorrect input gracefully
 - Program correctly calculating values
 - Program producing all required output 

Let's dive through how each of the following requirements listed have been accomplished through my proposed solution. 

1) Our entire program is well documented. It includes a module docstring, docstring for functions, and of course comments in source code. Comments in source code are meaningful, they are not written to explain what a peice of code is doing, as that is evident from the code itself, but rather the approach we have taken/ why the peice of code is doing what it's doing.

2) Indeed, the program runs without any hanging or crashing. Even when user enters unexpected input, the program alerts user that the input is not valid without crashing and prompts for a valid input to be entered. This was a deliberate choice to match the requirements/marking criteria.

3) The program handles valid input correctly. This is reinforced through the testing process in which valid inputs always result in valid outputs.

4) As mentioned above, the program handles incorrect input gracefully. We don't hang or crash on incorrect output, we simply alert the user letting them know what they entered was not a valid input and we prompt them to enter the input again. This repeats until the input we receive is valid.

5) We can be very confident that the program correctly calulates the correct values. We have tested the program with boundary value inputs, valid inputs and invalid inputs, whilst making sure all the actual outputs match the expected values. E.g. we would expect if we had 3 adults & 3 children to receive either a Family Pass A or a Family Pass B and pay the remaining for an adult and child, bringing our cheapest cost to $25, as compared to paying for 3 adults and 3 children to total $29.00.

6) The program does indeed produce all required output within the specified receipt format. The output format has been replicated closely to the original specified examples given in the task description. This includes error messages, input messages etc..

## References:
- https://www.w3schools.com/python/python_args_kwargs.asp
- https://www.w3schools.com/python/python_dictionaries.asp
- https://www.geeksforgeeks.org/python/python-docstrings/
- https://www.geeksforgeeks.org/python/python-find-minimum-pair-sum-in-list/
- https://computing.help.inf.ed.ac.uk/FAQ/whats-tarball-or-how-do-i-unpack-or-create-tgz-or-targz-file