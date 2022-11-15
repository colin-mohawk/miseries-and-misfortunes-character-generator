# a character generator that rolls most of the random tables in character creation, for the game Miseries and Misfortunes by Luke Crane
# generator by Colin Ferrie 2022 

#we need to import the die roller
from dieSideRoller import roll_d

print("\n\n\nBonjour, you are about to create a character for Miseries and Misfortunes RPG, Roleplaying in 1648 France.\nYou should have on hand Miseries & Misfortunes Book 2: Les Fruits Malheureux. \nFollowing the book, Motif should already be established avec tes amis(with your Friends)\nWe will roll some dice on the tables and provide you with the results\nThis covers the Birth and Wealth Section to the start of Determine Languages section.\nYou will continue with the book to complete character creation\nOnce you run this there will be a file MyCharacter.txt created,\nit will be replaced if you run this script again without copying it somewhere safe\n")

#obligations are a game stat and we define a value of 0 for now since thats where you start 
obligations = 0

# roll 3 6 sided die, get quality of birth, income_source, update obligations
quality_birth = roll_d(6, 3)

#roll 1 6 sided die for income sources
income_source = (roll_d(6, 1))

# income index is use to select our randomized income source based on the quality of birth roll
# we need to reduce the result 1-6 to 0-5 to easily referenced in income list since our list starts at 0 
income_index = (income_source) - 1

##################################################################################################
# Quality of Birth assigns:
#           quality_Birth
#           income_source[based on rolled index position] 
##################################################################################################

if quality_birth in [3, 4, 5]:
    obligations = obligations + 2
    quality_birth = 'Marginaux: Actor, prostitute, urchin, soldier, filou, sailor'
    income_list = ['None', 'None', 'None', 'Labor', 'Sale Boulot', 'Sale Boulot']
    income_source = income_list[income_index]  

elif quality_birth in [6, 7, 8, 9, 10]:
    obligations = obligations + 3
    quality_birth = 'Peasant: Laborer, villein, farmer'
    income_list = ['None', 'Labor', 'Labor', 'Labor', 'Produce', 'Produce']
    income_source = income_list[income_index]

elif quality_birth in [11, 12, 13]:
    obligations = obligations + 2
    quality_birth = 'Commoner: Printer, fish monger, passeur'
    income_list = ['Labor', 'Labor', 'Labor', 'Labor', 'Business', 'Business']
    income_source = income_list[income_index]

elif quality_birth == 14:
    obligations = obligations + 2
    quality_birth = 'Artisan: Smith, carpenter, clothier, mason, plumber, clock maker'
    income_list = ['Labor', 'Labor', 'Labor', 'Business', 'Business', 'Business']
    income_source = income_list[income_index]

elif quality_birth == 15:
    obligations = obligations + 2
    quality_birth = 'Bourgeoisie: Merchant, financier, architect, famous artist'
    income_list = ['Auction', 'Business', 'Business', 'Business', 'Logeur', 'Usury & Zinskauf']
    income_source = income_list[income_index]

elif quality_birth == 16:
    obligations = obligations + 1
    quality_birth = 'Noblesse d’épée sans titre(Noble without Title): Écuyer, chevalier, dame, gentilhomme'
    income_list = ['None', 'None', 'None', 'None', 'Charge', 'Benefice']
    income_source = income_list[income_index]

elif quality_birth == 18:
    #obligations = obligations + 0 #no additional obligations
    quality_birth = 'Noblesse d’épée avec titre(Noble of the Sword with title): Sieur, seigneur, baron, vicomte, comte, marquis'
    income_list = ['None', 'Charge', 'Logeur', 'Logeur', 'Benefice', 'Taxation']
    income_source = income_list[income_index]
 
else:
    # quality_birth == 17
    # this quality of birth has a special income source and possible second one we added income_source_2 to deal with it
    #     income_source = income_list[income_index]    are in the if and elif statements because of this need for 2 values
    obligations = obligations + 2
    quality_birth = 'Noblesse de robe(Noble of the Robe): Minister, judge, intendant'
    income_list = ['None', 'None', 'None', 'None', 'Logeur', 'Benefice']
    income_source = 'Droit Annuel'
    income_source_2 = income_list[income_index]
    income_range = 0
 
##################################################################################################
# Income and Property, this assigns:
#               income_range
#               property_type - at the end of If statements
##################################################################################################

# roll 1d6 based on income_source
property_type = roll_d(6, 1)

if income_source == 'None':
    income_range = 0
    property_list = ['Homeless', 'Homeless', 'Homeless', 'Homeless', 'Rented Flat', 'Country Home']

elif income_source == 'Labor':
    income_range = roll_d(3, 1)
    property_list = ['Homeless', 'Rented Flat', 'Rented Flat', 'Rented Flat', 'Rented Flat', 'Country Home']

elif income_source == 'Sale Boulot':
    income_range = roll_d(4, 1)
    property_list = ['Homeless', 'Homeless', 'Homeless', 'Homeless', 'Rented Flat', 'City Home']

elif income_source == 'Produce':
    income_range = roll_d(6, 1)
    property_list = ['Country Home', 'Country Home', 'Country Home', 'Country Home', 'Country Home', 'Manor']

elif income_source == 'Business':
    income_range = roll_d(6, 1)
    property_list = ['Rented Flat', 'City Home', 'City Home', 'City Home', 'City Home', 'Townhouse']

elif income_source == 'Auction':
    income_range = roll_d(4, 1) + 1
    property_list = ['Country Home', 'Country Home', 'City Home', 'City Home', 'City Home', 'Townhouse']

elif income_source == 'Logeur':
    income_range = roll_d(6, 1) + 2
    property_list = ['Manor', 'Townhouse', 'Townhouse', 'Townhouse', 'Townhouse', 'Estate']

elif income_source == 'Benefice':
    income_range = roll_d(6, 1) + 1
    property_list = ['', 'Country Home', 'Country Home', 'Country Home', 'Country Home', 'Abby (Estate)']
 
elif income_source == 'Charge':
    income_range = roll_d(6, 1) + 1
    property_list = ['Country Home', 'Country Home', 'Country Home', 'Country Home', 'City Home', 'Fortress']

elif income_source == 'Droit Annuel':
    income_range = roll_d(4, 1) + 1
    property_list = ['City Home', 'City Home', 'City Home', 'City Home', 'City Home', 'Villa']

elif income_source == 'Taxation':
    income_range = roll_d(4, 2) + 1
    property_list = ['Villa', 'Manor', 'Manor', 'Estate', 'Village,', 'Castle']
else:
    # income source Usury & Zinskauf
    income_range = roll_d(8, 1) + 2
    property_list = ['Townhouse', 'Townhouse', 'Townhouse', 'Manor', 'Manor', 'Estate']

# 
# convert the rolled value property_type to an index value starting at 0 thus the -1 again
property_type = property_list[(property_type) - 1]

##################################################################################################
# Property details this section assigns:
#               obligations 
#               income_modifier 
#               asset_value 
##################################################################################################

# we figure out the values of your property obligation changes and income modifiers based on property here 
income_modifier = 0
asset_value = 0

#some errors where happening when income_modifier was added to a number but setting them  integers has fixed it
if property_type == 'Homeless':
    obligations = obligations + 0
    income_modifier = income_modifier + int(-1)
    asset_value = 0

elif property_type == 'Rented Flat':
    obligations = obligations + 1
    income_modifier = income_modifier + int(0)
    asset_value = 0

elif property_type == 'Country Home':
    obligations = obligations + 1
    income_modifier = income_modifier + int(0)
    asset_value = roll_d(3, 1)

elif property_type == 'City Home':
    obligations = obligations + 2
    income_modifier = income_modifier + int(0)
    asset_value = roll_d(4, 1)

elif property_type == 'Manor':
    obligations = obligations + 3
    income_modifier = income_modifier + int(1)
    asset_value = roll_d(6, 1)

elif property_type == 'Townhouse':
    obligations = obligations + 3
    income_modifier = income_modifier + int(1)
    asset_value = roll_d(6, 1) + 1

elif property_type == 'Villa':
    obligations = obligations + 5
    income_modifier = income_modifier + int(2)
    asset_value = roll_d(8, 1)

elif property_type == 'Estate':
    obligations = obligations + 6
    income_modifier = income_modifier + int(3)
    asset_value = roll_d(8, 1)

elif property_type == 'Village':
    obligations = obligations + 8
    income_modifier = income_modifier + int(3)
    asset_value = roll_d(8, 1)

elif property_type == 'Castle':
    obligations = obligations + 9
    income_modifier = income_modifier + int(2)
    asset_value = roll_d(10, 1)

elif property_type == 'Castle':
    obligations = obligations + 10
    income_modifier = income_modifier + int(1)
    asset_value = roll_d(10, 1)

##################################################################################################
# File I/O - file input
################################################################################################## 
#       Wealth Rating, This section defines:
#               wealth_rating           
#               income_total
#               wealth_rating 
#               income_livres 
#               social_strata
#       
##################################################################################################

#income total is calculated by adding these values 
income_total = income_range + income_modifier

#to fix an issue with property type homeless providing a -1 as a result 
# we created a copy of the income_total for the issue 
income_true_total = income_total
if income_total < 0:
    income_total = 0

#define a few more values
wealth_rating = 0
# wealth_rating= some value from chart
income_livres = 0
social_strata = "null Place"
# based on wealth rating

# we open the local file income.txt to import values into a dictionary with nested dictionaries 
with open('income.txt', encoding="utf-8") as f:
    income_dict={}
    for line in f.readlines():
        info = line.split(",")
        income_tot = info[0]
        wealth_rat = info[1]
        income_liv = info[2]
        social_str = info[3]

        income_dict[income_tot] = {"income_total":income_tot, "wealth_rating":wealth_rat,"income_livres":income_liv,"social_srata":social_str}

# now we are extracting the values calculated from Income_total
income_results = income_dict[str(income_total)]
income_total = str(income_results["income_total"])
wealth_rating = str(income_results["wealth_rating"])
income_livres = str(income_results["income_livres"])
social_strata = str(income_results["social_srata"])

########################################################################################
# User input with parameters
########################################################################################
#             Lifestyle Choice this section defines:
#                   lifestyle_choice
#                   obligations 
########################################################################################

#define another variable 
lifestyle_choice = "null life"

# User Input with a loop that requires input 0,1,2,3,4 invalid choice not accepted
while True:
    lifestyle_choice = input("How do you live your life? This choice will add to your Obligations but will later affect your reputation.\nChoose one, \n0)Natural \n1)Bread Alone Obligations +1 \n2)Respectable Obligations +2 \n3)Fashionable Obligations +3\n4)Lavish Obligations +5\n\n")
    try:
        lifestyle_choice = int(lifestyle_choice)
    except:
        print("\nAttention, s'il vous plaît; please enter a number 0-4\n")
        continue
    if lifestyle_choice < 0 or lifestyle_choice > 4:
        print("\nAttention, s'il vous plaît; please enter a number 0-4\n")
        continue
    break

if lifestyle_choice == 1:
    lifestyle_choice ='Bread Alone'
    obligations = obligations + 1

elif lifestyle_choice == 2:
    lifestyle_choice ='Respectable'
    obligations = obligations + 2

elif lifestyle_choice == 3:
    lifestyle_choice ='Fashionable'
    obligations = obligations + 3

elif lifestyle_choice == 4:
    lifestyle_choice ='Fashionable'
    obligations = obligations + 5

else:
    # lifestyle is 0
    lifestyle_choice ='Natural'
    #obligations = obligations + 0

###########################################################################################
# User input 
###########################################################################################
#   Dependents 
#   this section defines:
#           dependents_all
#           dependent_lifestyle_choice
#   Note: dependent_lifestyle_choice will be skipped if you have no dependents 
###########################################################################################

# a few new variables are defined 
dependents = 0
dependents_all = []
dependent_lifestyle_roll= 'none'
dependent_lifestyle_choice = "error dependents lifestyle"
# roll 1d4-1 to have 0-3 dependents
dependents = roll_d(4,1) -1

# this allows combining relationships from Dependent_list to be combined with Relationship_table

if dependents >= 1:
    dependents_index = 0
    for i in range (0,dependents):
        dependent_list=['child','younger cousin','nephew','niece','younger sister','younger brother','sickly childhood friend','spouse','older cousin','elder brother','elder sister','impecunious lover','infirm father','dying mentor','infirm mother','widower infirm uncle','widowed infirm aunt','infirm grandfather','infirm grandmother','drunk uncle or aunt']
        relationship_sub=roll_d(6,1) -1 # minus one for indexing correctly
        relationship_table=['blood','blood','blood','in-law','in-law','filial or adopted']
        deps_add= str( (dependent_list[dependents_index])+" related to you by "+(relationship_table[relationship_sub]) )
        dependents_all.append(deps_add)
        dependents_index +=1
else:
    dependents_all="no one, you lucky devil!"

#the next section checks if you have any dependents, if you dont it will be skipped ####

# random 2d6 or match your choice
# adds to obligation only once same for all dependents
# r or R is accepted to roll any other input results in matching dependant choice to your earlier selection 
if dependents >= 1:

    dependent_lifestyle_roll= input ("\nDo your dependents match your lifestyle?\nIf you want them to be the same as you, simply press enter\nIf you want the fates to determine their collective lifestyle, roll for it. Input R to roll \n")
    if dependent_lifestyle_roll == "r" or dependent_lifestyle_roll == "R":
        dependents_life_roll= roll_d(6,2) -1 #-1 for indexing again
        dependent_lifestyle_list=['Natural','Natural','Bread Alone','Bread Alone','Bread Alone','Bread Alone','Bread Alone','Respectable','Respectable','Fashionable','Lavish','Lavish']
#test results as bread alone keeps comming up        dependent_lifestyle_list=['Natural0','Natural1','Bread Alone2','Bread Alone3','Bread Alone4','Bread Alone5','Bread Alone6','Respectable7','Respectable8','Fashionable9','Lavish10','Lavish11']
        dependent_lifestyle_choice = dependent_lifestyle_list[int(dependents_life_roll)]
    else:
        dependent_lifestyle_choice = lifestyle_choice

obligations+=int(dependents)

###########################################################################################
# Debits           
#          this section defines: 
#               debts
#               obligations 
#               total_obligations 
###########################################################################################

debts_roll = roll_d(6,1)
# roll 1d6  will modify obligations,
debts = 'null error'# i added this value to test for an error
wealth_rating_debt = 0
# if debts is 1 then roll 2d3 to calculate the one who owes you

if debts_roll == 1:
    # You are owed money (value: 2d3 Wealth)
    wealth_rating_debt = roll_d(3,2)
    debts = 'You are debt free'

elif  debts_roll == 2:
    debts = 'you have a sizable debt (+3 Obligations)'
    obligations = obligations + 3

elif  debts_roll == 3:
    debts = 'you are in debt (+2 Obligations)'
    obligations = obligations + 2

elif  debts_roll == 4:
    debts = 'you owe a small debt (+1 Obligations)'
    obligations = obligations + 1

else:
    # # 5-6
    debts = 'You are debt free'

total_obligations = obligations
# Total Obligations has been updated as we have rolled 
# Birth quality obligations (0-3) from Quality of Birth table
# + property obligations (0-10) from Property table
# + personal lifestyle (0-5)
# + number of dependents (0-3)
# + dependents’ lifestyles (0-5) from Dependent Lifestyle table
# + number of debts (0-3) from Debts table

###########################################################################################
#           Nation Religion Politics
#               this section defines:
#                   nationality
#                   religion
#                   political          
###########################################################################################

nationality = 'French, rating 1/6'
# you are french but you might be american following the book

#make a new variable so i can tell if something fails later 
religion='null gods'
religion_roll = roll_d(6,2)

# 2d6 for gods
if religion_roll == 2 or religion_roll == 3:
    religion = 'Lutheran, rating 1/6'
elif religion_roll == 4  or religion_roll == 5 or religion_roll == 6 or religion_roll == 7:
    religion = 'Catholic, rating 1/6'
elif religion_roll == 8  or religion_roll == 9 or religion_roll == 10 or religion_roll == 11:
    religion = 'Huguenot, rating 1/6'
else:
    #12   
    religion = 'Jewish, rating 1/6'

#more variables, with unique names to i can test for issues
political='null politic'
# 2d6 for king or other
political_roll = roll_d(6,2)

if political_roll == 2:
    political='Cardinalist, rating 1/6'
elif political_roll == 3 or political_roll == 4 :
    political='Noble, rating 1/6'
elif political_roll == 5 or political_roll == 6 or political_roll == 7:
    political='Royalist, rating 1/6'
elif political_roll == 8 or political_roll == 9 or political_roll == 10:
    political='Frondeur, rating 1/6'
elif political_roll == 11 :
    political='Hapsburg, rating 1/6'
else:
    # roll must have been 12
    political='Politically ignorant, rating 1/6'

#now re roll our basic stats this part should be familiar if you've played D&D
# roll 3d6 
Strength = roll_d(6,3)
Intelligence = roll_d(6,3)
Wisdom = roll_d(6,3)
Dexterity = roll_d(6,3)
Constitution = roll_d(6,3)
Charisma = roll_d(6,3)
#no roll for language 
language = 'French, rating 3/6'
               
###########################################################################################
#                   Output
#                       no new variables 
###########################################################################################

print("\n\nYou were born to the caste of " + quality_birth)
if quality_birth == 'Noblesse de robe: Minister, judge, intendant':
    print("Your Wealth comes from " + str(income_source) + " and " + str(income_source_2))
else:
    print("Your Wealth comes from " + income_source)
print("Home for you is", property_type, 
" which has an Asset Value of",  asset_value, 
'\nWealth Rating is', wealth_rating,
" and Income in Livres is", income_livres,
"\nYour Social Strata, those you may be seen pressing hands with;", social_strata,
"You chose to live in the", lifestyle_choice,"Lifestyle")

if dependents == 0:
    print ("Your Dependents include; " + dependents_all)
else:
    print ("Your Dependents include; " + str(dependents_all)[1:-1] + " and they live a " + str(dependent_lifestyle_choice ) +" lifestyle.")
if wealth_rating_debt != 0:
    print ('and you are owed a debt, your debtor has a wealth rating of ' + str(wealth_rating_debt))   
else:
    print ("and " + debts)
print("You have " + str(total_obligations) + " total Obligations"+ "\nYour Language is " + language +"\nYour Nationality is " + nationality + '\nYour Religion is '+ str(religion) +'\nYour Political Affiliation is ' + political +'\nSTATS \n'  + str(Strength) + '\tStrength \n' + str(Intelligence) + '\tIntelligence \n' + str(Wisdom) + '\tWisdom \n' + str(Dexterity) + '\tDexterity \n'+ str(Constitution) +'\tConstitution \n'+ str(Charisma) + '\tCharisma \n')


###########################################################################################
# File I/O write to file
#                   
###########################################################################################
#                   below we write to file MyCharacter.txt
#                   the results are simplified and presented in a format to 
#                   easily copy to a character sheet 
###########################################################################################

with open('MyCharacter.txt', "w", encoding="utf-8") as f:
    print("Below find all the details required to continue building your Miseries and Misfortunes character\n\nQuality of birth\t",quality_birth, file=f)
    if quality_birth == 'Noblesse de robe: Minister, judge, intendant':
        print("Wealth Income Source \t",str(income_source)," & ",str(income_source_2), file=f)
    else:
        print("Wealth Income Source \t",str(income_source), file=f)
    print("Home \t", property_type, "\tAsset Value\t", str(asset_value), '\nWealth Rating\t', wealth_rating, "\nIncome in Livres\t",
        income_livres, "\nSocial Strata\t", social_strata,'\nLifestyle\t', lifestyle_choice, file=f)
    if dependents == 0:
        print ("Dependents","none", file=f)
    else:
        print ("Dependents\t",str(dependents_all)[1:-1],"\nDependents Lifestyle\t",str(dependent_lifestyle_choice ), file=f)
    if wealth_rating_debt != 0:
        print ('Debt Owed to you\t',str(wealth_rating_debt), file=f)   
    else:
        print ("Debt\t ",debts, file=f)
    print("Obligations\t",str(total_obligations),"\nLanguage\t",language ,"\nNationality \t",nationality,'\nReligious Affiliation\t',str(religion) ,'\nPolitical Affiliation \t',political ,'\nSTATS \n' ,str(Strength),'\tStrength \n',str(Intelligence),'\tIntelligence \n',str(Wisdom),'\tWisdom \n',str(Dexterity),'\tDexterity \n',str(Constitution) ,'\tConstitution \n',str(Charisma),'\tCharisma \n', file=f)