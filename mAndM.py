# a character generator that rolls most of the random tables in character creation, for the game Miseries and Misfortunes by Luke Crane
# generator by Colin Ferrie 2022 

import random
#this is a fuction that rolls n-sided die(dice) n-rolls and totals the result of the rolls
#example  roll_d(6,2) would most likely result in 6,7,8 but it should be possible to get 2-12 as a result
def roll_d(side, rolls):

    roll_result = 0

    for _ in range(rolls):

        roll = random.randint(1, side)

        roll_result = roll_result + roll

    return int(roll_result)


#obligations are a game stat and we define a value of 0 for now
obligations = 0

# roll 3 6 sided die, get qality of birth, income_source, update obligations
quality_birth = roll_d(6, 3)
# uncomment to test
# quality_birth=17

income_source = (roll_d(6, 1))
# type(income_source)
# print (income_source)

# we need to reduce the result 1-6 to 0-5 to easily refrence in income list 
income_index = (income_source) - 1



if quality_birth in [3, 4, 5]:

    obligations = obligations + 2

    quality_birth = 'Marginaux: Actor, prostitute, urchin, soldier, filou, sailor'

    income_list = ['None', 'None', 'None', 'Labor', 'Sale Boulot', 'Sale Boulot']

    income_source = income_list[income_index]  



#if quality_birth in [3, 4, 5]:
#    obligations = obligations + 2
#    quality_birth = 'Marginaux: Actor, prostitute, urchin, soldier, filou, sailor'
#    income_list = ['None', 'None', 'None', 'Labor', 'Sale Boulot', 'Sale Boulot']
#    income_source = income_list[income_index]
 

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

    #quality_birth is 18

    #oblgations + 0

    quality_birth = 'Noblesse d’épée avec titre(Noble of the Sword with title): Sieur, seigneur, baron, vicomte, comte, marquis'

    income_list = ['None', 'Charge', 'Logeur', 'Logeur', 'Benefice', 'Taxation']

    income_source = income_list[income_index]

 

else:

    # quality_birth == 17

    obligations = obligations + 2

    quality_birth = 'Noblesse de robe(Noble of the Robe): Minister, judge, intendant'

    income_list = ['None', 'None', 'None', 'None', 'Logeur', 'Benefice']

    income_source = 'Droit Annuel'

    income_source_2 = income_list[income_index]

    income_range = 0
 
# rolled based on income_source, is this also income rating /mod?

property_type = 0

# roll 1d6 based on income_source
# broken somwhere here V below

property_type = roll_d(6, 1)
 

if income_source == 'None':

    income_range = 0

    property_list = ['Homeless', 'Homeless', 'Homeless',

                     'Homeless', 'Rented Flat', 'Country Home']

 

elif income_source == 'Labor':

    income_range = roll_d(3, 1)

    property_list = ['Homeless', 'Rented Flat', 'Rented Flat',

                     'Rented Flat', 'Rented Flat', 'Country Home']

 

elif income_source == 'Sale Boulot':

    income_range = roll_d(4, 1)

    property_list = ['Homeless', 'Homeless', 'Homeless',

                     'Homeless', 'Rented Flat', 'City Home']

elif income_source == 'Produce':

    income_range = roll_d(6, 1)

    property_list = ['Country Home', 'Country Home',

                     'Country Home', 'Country Home', 'Country Home', 'Manor']

 

elif income_source == 'Business':

    income_range = roll_d(6, 1)

    property_list = ['Rented Flat', 'City Home',

                     'City Home', 'City Home', 'City Home', 'Townhouse']

 

elif income_source == 'Auction':

    income_range = roll_d(4, 1) + 1

    property_list = ['Country Home', 'Country Home',

                     'City Home', 'City Home', 'City Home', 'Townhouse']

 

elif income_source == 'Logeur':

    income_range = roll_d(6, 1) + 2

    property_list = ['Manor', 'Townhouse', 'Townhouse',

                     'Townhouse', 'Townhouse', 'Estate']

 

elif income_source == 'Benefice':

    income_range = roll_d(6, 1) + 1

    property_list = ['', 'Country Home', 'Country Home',

                     'Country Home', 'Country Home', 'Abby (Estate)']

 

elif income_source == 'Charge':

    income_range = roll_d(6, 1) + 1

    property_list = ['Country Home', 'Country Home',

                     'Country Home', 'Country Home', 'City Home', 'Fortress']

 

elif income_source == 'Droit Annuel':

    income_range = roll_d(4, 1) + 1

    property_list = ['City Home', 'City Home',

                     'City Home', 'City Home', 'City Home', 'Villa']

 

elif income_source == 'Taxation':

    income_range = roll_d(4, 2) + 1

    property_list = ['Villa', 'Manor', 'Manor', 'Estate', 'Village,', 'Castle']

 

else:

    # income source Usury & Zinskauf

    income_range = roll_d(8, 1) + 2

    property_list = ['Townhouse', 'Townhouse',

                     'Townhouse', 'Manor', 'Manor', 'Estate']

property_type = property_list[(property_type) - 1]

 

##### property_details #########

# update oblgations, create Income Modifier, and asset Value

 

income_modifier = 0

# from property_detail

 

asset_value = 0

# from property_detail

 

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

 

income_total = income_range + income_modifier

 

#print (income_total)

 

wealth_rating = 0

# income_range + income_modifier = income_total

# wealth_rating= some value from chart

#

income_livres = 0

 

social_strata = 0

# based on wealth rating

 

# wealth rating

if income_total == 13:

    wealth_rating = '99/100'

    income_livres = '₶ 1,000,000,000s'

    social_strata = 'VOC'

 

elif income_total == 12:

    wealth_rating = '98/100'

    income_livres = '₶ 100,000,000s'

    social_strata = 'The state'

 

elif income_total == 11:

    wealth_rating = '97/100'

    income_livres = '₶ 50,000,000s'

    social_strata = 'M. Le Cardinal'

 

elif income_total == 10:

    wealth_rating = '96/100'

    income_livres = '₶ 10,000,000s'

    social_strata = 'Ministers of State'

 

elif income_total == 9:

    wealth_rating = '19/20'

    income_livres = '₶ 5,000,000s'

    social_strata = 'Financiers'

 

elif income_total == 8:

    wealth_rating = '11/12'

    income_livres = '₶ 1,000,000s'

    social_strata = 'Princes & Dukes'

 

elif income_total == 7:

    wealth_rating = '9/10'

    income_livres = '₶ 100,000s'

    social_strata = 'Merchants'

 

elif income_total == 6:

    wealth_rating = '7/8'

    income_livres = '₶ 10,000s'

    social_strata = 'Marquis & Barons'

 

elif income_total == 5:

    wealth_rating = '5/6'

    income_livres = '₶ 1000s'

    social_strata = 'Artisans'

  

elif income_total == 4:

    wealth_rating = '4/6'

    income_livres = '₶ 500s'

    social_strata = 'Tradesmen'

 

elif income_total == 3:

    wealth_rating = '3/6'

    income_livres = '₶ 200s'

    social_strata = 'Peasants'

 

 

elif income_total == 2:

    wealth_rating = '2/6'

    income_livres = '₶ 100s'

    social_strata = 'Laborers'

 

 

elif income_total == 1:

    wealth_rating = '1/6'

    income_livres = '₶ 10s'

    social_strata = 'Beggars'

 

else:

    # income total == 0

    wealth_rating = '0'

    income_livres = '₶0'

    social_strata = 'Hermits'

 

lifestyle_choice = ''

# this updates oblgations you get to choose this

 

lifestyle_choice = input(

    "How do you live your life? \n0)Natural \n1)Bread Alone Obligations +1 \n2)Respectable Obligations +2 \n3)Fashionable Obligations +3\n4)Lavish Oblgations +5\n\n")

if lifestyle_choice == '1':

    lifestyle_choice ='Bread Alone'

    obligations = obligations + 1

   

elif lifestyle_choice == '2':

    lifestyle_choice ='Respectable'

    obligations = obligations + 2

 

elif lifestyle_choice == '3':

    lifestyle_choice ='Fashionable'

    obligations = obligations + 3

 

elif lifestyle_choice == '4':

    lifestyle_choice ='Fashionable'

    obligations = obligations + 5

 

else:

    # lifestyle is 0

    lifestyle_choice ='Natural'

 

dependents = 0

# roll 1d4-1 to have 0-3 dependants

dependents = roll_d(4,1) -1

# roll dependants 1d20

# roll to determine relationship 1d6

# number of dependants modifies oblgations

dependants_all = []

 

dependent_lifestyle_roll= 'none'

dependent_lifestyle_choice='Natural'

 

if dependents >= 1:

    dependents_index = 0

    for i in range (0,dependents):

 

        dependent_list=['Child','Younger cousin','Nephew','Niece','Younger sister','Younger brother','Sickly childhood friend','Spouse','Older cousin','Elder brother','Elder sister','Impecunious lover','Infirm father','Dying mentor','Infirm mother','Widower infirm uncle','Widowed infirm aunt','Infirm grandfather','Infirm grandmother','Drunk uncle or aunt']

        relationship_sub=roll_d(6,1) -1

        relationship_table=['Blood','Blood','Blood','In-law','In-law','Filial or adopted']

        deps_add= str( (dependent_list[dependents_index])+" by "+(relationship_table[relationship_sub]) )

        dependants_all.append(deps_add)

        dependents_index +=1

 

else:

    dependants_all=" no one, you lucky devil "

   

    

lifestyle_dependents = 'Natural'

# random 2d6 or match your choice

# adds to oblgation only once same for all depedants

if dependents >= 1:

    dependent_lifestyle_roll= input (

        "Do your dependants match your lifestyle, enter nothing, or do you want to roll for it? input R to roll \n\n")

    if dependent_lifestyle_roll== "r" or dependent_lifestyle_roll== "R":

        dependants_life_roll= roll_d(6,2) -1

        dependent_lifestyle_list=['Natural','Natural','Bread Alone','Bread Alone','Bread Alone','Bread Alone','Bread Alone','Respectable','Respectable','Fashionable','Lavish','Lavish']

 

   

    else:

        pass

        #dependent_lifestyle_list=['Natural','Bread Alone','Respectable','Fashionable','Lavish']

if dependents >= 1:  

        

    if lifestyle_choice == 'Bread Alone':

        dependent_lifestyle_choice ='Bread Alone'

        obligations = obligations + 1

               

    elif lifestyle_choice == 'Respectable':

        dependent_lifestyle_choice ='Respectable'

        obligations = obligations + 2

   

    elif lifestyle_choice == 'Fashionable':

        dependent_lifestyle_choice ='Fashionable'

        obligations = obligations + 3

   

    elif lifestyle_choice == 'Lavish':

        dependent_lifestyle_choice ='Lavish'

        obligations = obligations + 5

    else:

                # lifestyle is Natural

                dependent_lifestyle_choice ='Natural'

           

        

else:       

    pass

debts_roll = roll_d(6,1)

# roll 1d6  will modify oblgations,

 

debts = 'null error'

 

weath_rating_debt = 0

# if debts is 1 then roll 2d3 to calculate the one who owes you

if debts_roll == 1:

    # You are owed money (value: 2d3 Wealth)

    weath_rating_debt = roll_d(3,2)

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

# Total Obligations

# Birth quality obligations (0-3) from Quality of Birth table

# + property obligations (0-10) from Property table

# + personal lifestyle (0-5)

# + number of dependents (0-3)

# + dependents’ lifestyles (0-5) from Dependent Lifestyle table

# + number of debts (0-3) from Debts table

 

nationality = 'French, rating 1/6'

# you are french but you might be american

 

relgion='null'

 

relgion_roll = roll_d(6,2)

# 2d6 for gods

if relgion_roll == 2 or relgion_roll == 3:

    relgion = 'Lutheran, rating 1/6'

   

elif relgion_roll == 4  or relgion_roll == 5 or relgion_roll == 6 or relgion_roll == 7:

    relgion = 'Catholic, rating 1/6'

   

elif relgion_roll == 8  or relgion_roll == 9 or relgion_roll == 10 or relgion_roll == 11:

    relgion = 'Huguenot, rating 1/6'

   

else:

    #12   

    relgion = 'Jewish, rating 1/6'

 

political='null'

political_roll = roll_d(6,2)

# 2d6 for king

 

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

Strength = roll_d(6,3)

# roll 3d6

 

Intelligence = roll_d(6,3)

# roll 3d6

 

Wisdom = roll_d(6,3)

# roll 3d6

 

Dexterity = roll_d(6,3)

# roll 3d6

 

Constitution = roll_d(6,3)

# roll 3d6

 

Chrisma = roll_d(6,3)

# roll 3d6

 

language = 'French, rating 3/6'

# language is french at 3/6 rating

 

 

print("you were born to the " + quality_birth)

# special for Noblesse de robe

if quality_birth == 'Noblesse de robe: Minister, judge, intendant':

    print("your wealth comes from " + str(income_source) +

          " and " + str(income_source_2))

 

else:

    print("your wealth comes from " + str(income_source))

print("Home for you is " + (property_type) +

      " and that has an Asset Value of " + str(asset_value))

 

print('your Wealth Rating is ' + wealth_rating + " and Income in Livres is " +

      income_livres + " which means Social Strata is " + social_strata)

 

print('you chose to live in the ' + lifestyle_choice + " style")

 

 

print ("your dependants include; " + str(dependants_all)[1:-1] + " and they live a " + str(dependent_lifestyle_choice ) +" lifestyle.")

 

if weath_rating_debt != 0:

    print ('and you are owed a debt, your debitor has a wealth rating of ' + str(weath_rating_debt))   

else:

    print ("and " + debts)

 

print("you have " + str(total_obligations) + " total obligations")

 

print(

"Your Language is " + language +" and are Nationality " + nationality +" but you could be American " )

 

print ('Your Religious Affiliation is '+ str(relgion) +' and Political Affiliation is ' + political

       )

 

print ('STATS \n'  + str(Strength) + ' Strength \n'

      + str(Intelligence) + ' Intelligence \n'

      + str(Wisdom) + ' Wisdom \n'

      + str(Dexterity) + ' Dexterity \n'

      + str(Constitution) +'  Constitution \n'

      + str(Chrisma) + ' Chrisma \n'       )

