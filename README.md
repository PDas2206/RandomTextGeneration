# RandomTextGeneration
In this project, we reimplement the "Dissociated Press" system that was developed by MIT students in the 1970s (see Wikipedia). The purpose of this system is to generate random text from an n-gram model over a corpus. We train an instance of the n-gram class (sourced from piazza) using the corpus text2 (the novel *Sense and Sensibility* by Jane Austen) in *nltk.book* and name it **ngram**. We then use *ngram[context]* to determine the probability distribution for the next word given the previous *n-1* words. Given this distribution, we use the method *generate* from the NLTK class **ProbDistI** to generate the next random word. We vary *n* from 2 to 4.
## Getting Started:
The programs in this repo have been coded using Python 3. To run the files one has to have Python 3 or above installed in their systems. For zipfs_stemming.py to perform stemming, we have used the PorterStemmer method in nltk. Additionally you need the following packages to be installed: \
nltk \
random 
## Running the programs:
To execute the programs from the command shell, do the following steps: \
		> 1. Change the directory to this folder in your system. \
		> 2. To now execute the programs, type the following after the prompt appears: \
			>> python \<filename\>.py \
    > 3. Some of the programs are interactive in nature, so input from the user is expected, the nature of which is clearly explained to the user.
    > 4. *ngram_2_3_4.py* asks the user to give the value of "n" between 2 and 4 to create the "n"-gram model. This program uses *text2* from *nltk.book* as the corpus,  which can be imported using the following statement: \
				>> from nltk.book import * \
					>> or \
				>> from nltk.book import text2 \

		
