from default_details import *;
from default_validations import *;
print ("\n\nLet's get started:\n");
user_dec=raw_input("U want to continue as default user?(y/n): ");
while(user_dec!='y' and user_dec!='Y' and user_dec!='n' and user_dec!='N'):
    print("plz enter proper choice: ");
    user_dec=raw_input("U want to continue as default user?(y/n): ");
else:#new user
    if(user_dec=='n' or user_dec=='N'):
        spy_name=raw_input("Plz enter spy name: ");
        while(spy_name==""):
            spy_name=raw_input("Plz enter valid name.\nPlz enter spy name: ");

        spy_salutation=raw_input("Plz enter proper Salutation(Mr./Mrs/: ");
        while(spy_salutation.lower()!="mr." or spy_salutation.lower()!="mr" or spy_salutation.lower()!="mrs" or spy_salutation.lower()!="mrs."):
            spy_salutation=raw_input("Plz enter proper salutation(Mr./Mrs.: ");
        spy_name=spy_salutation.title().strip(".")+"."+" "+spy_name;


        spy_age=int(raw_input("Plz enter age: "));
        if(spy_age<12 or spy_age>50):
            print ("Sry! "+spy_name+"\nU age must be between 12 to 50 to use SPY CHAT.\nThank You.");
        else:
            spy_rating=float(raw_input("Plz enter rating(out of 5): "));
            while(spy_rating<0 or spy_rating>5):
                spy_rating=float(raw_input("Plz enter proper rating(out of 5): "));
    else:
        