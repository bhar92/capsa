CAPSA using Python


Basic tips:
	For general statements (like for, range, len, if and others) I would suggest searching on the web for their basic usage. They are quite straightforward.

	An elementary thing in python is the indentation. Notice that after for and if, the blocks that come under it is always, and i mean always indented. This is because indentations is compulsary in python, as opposed to C and C++. If you dont indent after statmenets like if, elif, else, for, while, and function definitions, python will throw up errors.

Specific Tips:

	Executing Program2:

		Just run the python scripts. You could use an IDE like IDLE, or directly through a command line. In a command line it would be like:
			python name_of_the_file.py
		Feel free to make changes wherever needed for inputs. 
		Note that complex numebers in python are used as '1j'. Make sure you put that 1 before the j. 
		Also, you dont have the option of using 1i in python (as far as i know)

	Executing Program3:

		This program reads the input from a text file. Hence make sure that the file name mentioned in the following 
		line matches exactly with the input data file.

			data = np.loadtxt('NAME_OF_FILE.txt')

		Further, make sure that the input file is in the same folder as the python file Program3.py.
		Once all of this is ensured, you can run the python file in the same manner as in Program2.
