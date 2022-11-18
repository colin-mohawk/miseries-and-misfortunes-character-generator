# Miseries and Misfortunes Character Generator

This project intends to be a companion to be used with Miseries & Misfortunes Book 2: Les Fruits Malheureux
A role playing game set in France 1648 by Luke Crane


## Usage

This should work with any python 3.10 or newer installation.
To fully understand the results you should read and have in hand Miseries & Misfortunes Book 2: Les Fruits Malheureux and use it with the results of the Generator.
The script makes the random dice rolls for tables required for character generation. It will ask some questions, but you will be referred back to the book to complete character creation.
The character sheets can be found at https://www.burningwheel.com/miseries-misfortunes-playsheets/

to run:
```bash
python mAndM.py
```

it will also create a file locally called mycharacter.txt with the results



## Example



Bonjour, you are about to create a character for Miseries and Misfortunes RPG, Roleplaying in 1648 France.
You should have on hand Miseries & Misfortunes Book 2: Les Fruits Malheureux.
Following the book, Motif should already be established avec tes amis(with your Friends)
We will roll some dice on the tables and provide you with the results
This covers the Birth and Wealth Section to the start of Determine Languages section.
You will continue with the book to complete character creation
Once you run this there will be a file MyCharacter.txt created,
it will be replaced if you run this script again without copying it somewhere safe

How do you live your life? This choice will add to your Obligations but will later affect your reputation.
Choose one,
0)Natural
1)Bread Alone Obligations +1
2)Respectable Obligations +2
3)Fashionable Obligations +3
4)Lavish Obligations +5

7

Attention, s'il vous plaît; please enter a number 0-4

How do you live your life? This choice will add to your Obligations but will later affect your reputation.
Choose one,
0)Natural
1)Bread Alone Obligations +1
2)Respectable Obligations +2
3)Fashionable Obligations +3
4)Lavish Obligations +5

two

Attention, s'il vous plaît; please enter a number 0-4

How do you live your life? This choice will add to your Obligations but will later affect your reputation.
Choose one,
0)Natural
1)Bread Alone Obligations +1
2)Respectable Obligations +2
3)Fashionable Obligations +3
4)Lavish Obligations +5

2

Do your dependents match your lifestyle?
If you want them to be the same as you, simply press enter
If you want the fates to determine their collective lifestyle, roll for it. Input R to roll
r


You were born to the caste of Commoner: Printer, fish monger, passeur
Your Wealth comes from Labor
Home for you is Country Home  which has an Asset Value of 1
Wealth Rating is 1/6  and Income in Livres is ₶ 10s
Your Social Strata, those you may be seen pressing hands with; Beggars
 You chose to live in the Respectable Lifestyle
Your Dependents include; 'child related to you by in-law', 'younger cousin related to you by blood', 'nephew related to you by blood' and they live a Bread Alone lifestyle.
and you are in debt (+2 Obligations)
You have 10 total Obligations
Your Language is French, rating 3/6
Your Nationality is French, rating 1/6
Your Religion is Catholic, rating 1/6
Your Political Affiliation is Politically ignorant, rating 1/6
STATS
10      Strength
10      Intelligence
9       Wisdom
11      Dexterity
8       Constitution
9       Charisma

### contents of MyCharacter.txt

Below find all the details required to continue building your Miseries and Misfortunes character

Quality of birth	 Commoner: Printer, fish monger, passeur
Wealth Income Source 	 Labor
Home 	 Country Home 	Asset Value	 1 
Wealth Rating	 1/6 
Income in Livres	 ₶ 10s 
Social Strata	 Beggars
 
Lifestyle	 Respectable
Dependents	 'child related to you by in-law', 'younger cousin related to you by blood', 'nephew related to you by blood' 
Dependents Lifestyle	 Bread Alone
Debt	  you are in debt (+2 Obligations)
Obligations	 10 
Language	 French, rating 3/6 
Nationality 	 French, rating 1/6 
Religious Affiliation	 Catholic, rating 1/6 
Political Affiliation 	 Politically ignorant, rating 1/6 
STATS 
 10 	Strength 
 10 	Intelligence 
 9 	Wisdom 
 11 	Dexterity 
 8 	Constitution 
 9 	Charisma 



## To Do
- File I/O
    - Done
- error detection
    - Done
- CLI user input with parameters
    - Done
- User input
    - Done
- GitHub Integration
    - Done
- Imported Modules
    - Done

### Future
- add option to show dice rolls
- update file output so it writes a new filename each time 
- follow the example of income to add flexibility to the script 
- implement alternative output like partially filled character sheet
- simplify code
- add more rolls expand parts of character creation 
- research 
