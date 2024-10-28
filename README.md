# LANGUAGE FLASHCARDS

These flashcards are intended for german, but simple modification of the source code can change the language. This script is nice, but requires a bash or equalivent terminal. 

The instance varaible way changes which way the flashcards go based on the relevant CSV file. 0 means left to right, and 1 means right to left. 

This does have the occasional problem with an indexOutOfBounds error, but restarting the script (up arrow + enter) fixes it.

In the same directory as the script, place a CSV file with the same name as the python file. (other names are fine but will be prompted upon every startup of the program.)

The csv file is to be formatted like so:

englishWord,article germanWord

For example, a csv file would be:

invention,die Erfindung

discovery,die Entdeckung

automobile,das Automobil

helicopter,der Hubschrauber

letterpress,der Buchdruck

eyeglass,das Brillenglas

lightweight,leichtgewichtig

this does have automatic color coding based on article. Der is blue, das is green, and die is red. 
