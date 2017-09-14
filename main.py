
print ("\n\nLet's get started:\n");
spy_name	=	raw_input("Plz enter ur secret name: ");
spy_age		=	12;

i=0;
while(i==0):
	if(spy_name == "" or spy_name == " "):
		print ("Plz enter correct name...\n");
		spy_name	=	raw_input();
	else:
		i=1;


spy_salutation	=	raw_input("\nPlz enter proper salutation(Mr or Mrs):");
while(i==1):
	if (spy_salutation == "Mr." or spy_salutation == "mr" or spy_salutation =="Mr" or spy_salutation == "Mrs." or spy_salutation == "mrs" or spy_salutation == "Mrs" or spy_salutation == "MR" or spy_salutation == "MR." or spy_salutation == "MRS" or spy_salutation == "MRS."):
		i=0;
	else:
		print ("Plz enter correct salutation...\n");
		spy_salutation	=	raw_input();
		
		
spy_name	=	spy_salutation+ " " + spy_name;
print("\n\nWelcome " +spy_name+ ".\nAur ki haal chaal.");

print type(spy_age);


