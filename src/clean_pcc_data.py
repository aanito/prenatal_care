import pandas as pd

# Load the dataset
df = pd.read_csv("data.csv")  # Replace with the correct file path

# Define variable mappings
variable_mapping = {
    # Sociodemographic variables
    "@1ageofthemother": "Age",
    "@2maritalstatus": "Marital_status",
    "@3ethinicity": "Ethnicity",
    "@4religion": "Religion",
    "@5educationalstatus": "Education",
    "@6husbandseducationalstatus": "Husband_Educ",
    "@7occupation": "Occupation",
    "@9monthelyincome": "Income_monthly",
    "@10Howmuchtimeyouspenttoreachhealthfacility": "Time_to_HC",
    
    # Knowledge variables
    "@26Doyouknowthatwomenshouldprepareampmaintaintheirhealthbeforege": "Prepare_Maintain",
    "@29Doyouknowthingsthatshouldbedonebeforepregnancy": "Plan_Visit",
    "@34Doyouknowthebenefitofpreconceptioncareservices": "Benefits",
    "@36Forwhompreconceptioncareisimportant": "Who_benefits",
    "@38Whoistheappropriatepersonforprovidingpreconceptioncare": "Professionals",
    "@39Doyouknowwherepreconceptioncareservicesareprovided": "Levels_of_care",
    "@40Howfrequentlyneedtheseservicestobeprovided": "Frequency",
    "@41Doyouknowwhenpreconceptioncareservicesareprovidedingeneral": "Time_of_care",
    
    # Attitude variables
    "@42Preconceptioncareisahighhealthcarepriorityforallwomencouplesp": "Att_Priority",
    "@43Womenwithmedicallyconfirmeddiseasesshouldonlyreceivepreconcep": "Att_chrn",
    "@44Womenwhohadpregnancycomplicationsoradversebirthoutcomesprevio": "Att_Birth",
    "@45Preconceptioncareservicesshouldbeprovidedforreproductiveagewo": "Att_Age",
    "@46Preconceptioncareservicesshouldbeprovidedformarriedwomen": "Att_married",
    "@47Preconceptioncareservicesshouldbeprovidedforunmarriedwomen": "For_unmarried",
    "@48Preconceptioncareservicesarenotimportantforadolescentgirls": "Not_For_Adolescent",
    "@49Husbandsshouldaccompanytheirwiveswhileseekinganypreconception": "Partner_company",
    "@50Preconceptioncareservicesshouldbeprovidedbymalehealthprofessi": "Male_Provider",
    "@51Preconceptioncareservicesshouldbeprovidedbyfemalehealthprofes": "Female_provider",
    "@52Preconceptioncareservicesshouldbeprovidedbytraditionalbirthat": "Traditional_provider",
    "@53Preconceptioncaredoesnothaveanyeffectonbirthoutcome": "Effect_on_baby",
    
    # Utilization variables
    "@83IfyesQ.82whichpreconceptioncareserviceshaveyoureceived": "Service_Utilized",
    "@84Haveyoureceivedpreconceptioncareservicefromhealthfacilityinth": "Received_PCC",
    "@85IfyesQ.84whichpreconceptioncareservicesshaveyoureceivedinthecu": "Type_PCC",
    "@86Whendidyoureceivepreconceptioncareserviceinthecurrentpregnanc": "Current_Preg_PCC",
    "@87Inwhichunithaveyoureceivedthepreconceptioncareserviceinthecur": "Unit_care_Received",
    "@88Wheredidyoureceivethepreconceptioncareserviceinthecurrentpreg": "Site_of_PCC",
    "@89Whoprovidedyouthepreconceptioncareserviceinthecurrentpregnanc": "Provider",
    "@90Whomakesdecisiononpregnancyplanningampseekinghealthcareservic": "Decision_with_Partner",
    "@91Didyourhusbandsupportsampaccompanyyouwhilehavingpreconception": "Hus_support",
    
    # Lifestyle and other variables
    "@60 Which chronic medical conditions affect the fetus?": "Hus_chrnc",
    "@61Whichlifestyleorbehavioralorenvironmentalconditionsaffectthef": "Hus_Behaviour",
    "@62Forwhomdoyouthinkpreconceptioncareandcounselingisneeded": "Target_group",
    "@63Doyouknowthebenefitofpreconceptioncareservices": "Know_Benefits",
    "@65Forwhompreconceptioncareisimportant": "Important_for",
    "@67Whoistheappropriatepersonforprovidingpreconceptioncare": "Appropriate_Provider",
    "@68Doyouknowwherepreconceptioncareservicesareprovided": "Sites_of_care",
    "@71Preconceptioncareisahighhealthcarepriorityforallwomencouplesp": "For_all_women",
    "@72Womenwithmedicallyconfirmeddiseasesshouldonlyreceivepreconcep": "For_Only_Medically_ill",
    "@73Womenwhohadpregnancycomplicationsoradversebirthoutcomesprevio": "For_WomenWithAdverseOutcome",
    "@74Preconceptioncareservicesshouldbeprovidedforreproductiveagewo": "For_ReproductiveAge",
    "@75Preconceptioncareservicesshouldbeprovidedformarriedwomen": "For_Married",
    "@76Preconceptioncareservicesshouldbeprovidedforunmarriedwomen": "For_Unmarried",
    "@77Preconceptioncareservicesarenotimportantforadolescentgirls": "Benefits_Adolescent",
    "@78Husbandsshouldaccompanytheirwiveswhileseekinganypreconception": "Hus_company",
    "@79Preconceptioncareservicesshouldbeprovidedbymalehealthprofessi": "Male_provider",
    "@80Preconceptioncareservicesshouldbeprovidedbyfemalehealthprofes": "Female_provider",
    "@81Preconceptioncaresshouldbeprovidedbytraditionalbirthat": "Traditional_provider",
    "@82Preconceptioncaredoesnothaveanyeffectonbirthoutcome": "Birth_outcome"
}

# Rename columns
df.rename(columns=variable_mapping, inplace=True)

# Save cleaned data
df.to_csv("../data/processed/cleaned_data.csv", index=False)

print("Data cleaning complete. Cleaned file saved as 'cleaned_data.csv'.")
