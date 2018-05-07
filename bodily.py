print "************************************WELCOME TO BODILY**************************************"
print "The guidelines-based clinical decision support tool for patients and primary care providers"
print "*******************************************************************************************"
print
print "Please enter your name"
name = raw_input("> ")
print "Please enter your age"
age = raw_input("> ")
print "Please enter your gender as F or M."
print "|  F - Female  |  M - Male  |"
gender = raw_input("> ")
print
print "Hello, {}".format(name)
print "Type in the numerical value of the body part that is bothering you today."
print
print "----------------------------------------------------------------------------------------------------------------------------------------------------"
print "|  1 - head      |     2 - ears    |   3 - eyes  |  4 - mouth/throat  |  5 - shoulders  |  6 - arms    | 7 - hands     |  8 - chest  |  9 - lungs  |"
print "----------------------------------------------------------------------------------------------------------------------------------------------------"
print "|  10 - abdomen  |  11 - genitals  |  12 - hips  |  13 - back/neck    |  14 - legs      |  15 - knees  |  16 - ankles  |  17 - feet  |  18 - skin  |"
print "----------------------------------------------------------------------------------------------------------------------------------------------------"
print
part = raw_input("> ")
print

if part == "1":
    print "You chose head. Please describe the problem. Pick one:"
    print "| 1 - pain |  2 - skin issue  |  3 - hair issue  |" 
    print
    problem = raw_input("> ")
    print

    if problem == "1":
        print "You chose pain. What type of pain do you have today? Type the corresponding number:"
        print "| 1 - dull and aching |  2 - squeezing and tightness  |  3 - thunder clap  | "  
        print
        type_of_pain = raw_input("> ")
        print

        if type_of_pain == "1":
            print "You chose dull and aching. Rate your level of pain."
            print "| 1 - mild |  2 - moderate  |  3 - severe, worse headache of my life  | "  
            print
            pain_rating = raw_input("> ")
            print
            

            if type_of_pain == "1":
                print "Your likely diagnosis is migraine headache."
                print
                print "Take NSAID (Advil, Aleve, Motrin) as directed on the OTC label if you have not done so already." 
                print "Limit caffeine and alcohol intake. Reduce stressful activities if possible at this time."
                print "If symptoms worsen or persist past 48 hours or are recurrent, follow up with your primary care provider." 
                print "If symptoms become sever, go to ER/urgent care."
                print
                print "For more information, go to AAFP clinical guidelines: https://www.aafp.org/afp/2013/0515/p682.html"

            if type_of_pain == "2":
                print "Your likely diagnosis is tension headache."
                print
                print "Take NSAID (Advil, Aleve, Motrin) as directed on the OTC label if you have not done so already." 
                print "Limit caffeine and alcohol intake. Reduce stressful activities if possible at this time."
                print "If symptoms worsen or persist past 48 hours or are recurrent, follow up with your primary care provider." 
                print "If symptoms become sever, go to ER/urgent care."
                print
                print "For more information, go to AAFP clinical guidelines: https://www.aafp.org/afp/2013/0515/p682.html"

            if type_of_pain == "3":
                print "You may have an underlying condition that will need to be investigated as soon as possible. Follow up with urgent care or ER immediately."
                print "For more information, go to AAFP clinical guidelines: https://www.aafp.org/afp/2013/0515/p682.html"

    if problem == "2":
        print "You chose skin issue. Describe the skin issue by choosing the number corresponding to the following:"
        print "| 1 - itching (no visible rash/wound) |  2 - open wound/lesion  |  3 - rash  |  4 - dryness  |"  
        print
        type_of_pain = raw_input("> ")
        print
        
        if type_of_pain == "1":
            print "You chose itching (no visible rash/wound). What have you already tried to relieve the itching?"
            print "|  1 - Benadryl over the counter  |  2 - Steroid Topical Cream  |  3 - Other over the counter medication  |  4 - Nothing  |"
            print
            itching_treatments = raw_input("> ")
            print 
            if itching_treatments == "1":
                print "Did the itching get"
                print "|  1 - Better  |  2 - Worse  |  3 - Stayed the same  |"
                print

        if type_of_pain == "1":
            print "You chose dull and aching. Rate your level of pain."
            print "| 1 - mild |  2 - moderate  |  3 - severe, worse headache of my life  | "  
            print
            pain_rating = raw_input("> ")
            print

            if type_of_pain == "1":
                print "You may have a migraine headache."
                print
                print "Take NSAID (Advil, Aleve, Motrin) as directed on the OTC label if you have not done so already." 
                print "Limit caffeine and alcohol intake. Reduce stressful activities if possible at this time."
                print "If symptoms worsen or persist past 48 hours or are recurrent, follow up with your primary care provider." 
                print "If symptoms become sever, go to ER/urgent care."
                print
                print "For more information, go to AAFP clinical guidelines: https://www.aafp.org/afp/2013/0515/p682.html"

            if type_of_pain == "2":
                print "Take NSAID (Advil, Aleve, Motrin) or Tylenol as directed on the OTC label if you have not done so already. If symptoms worsen or persist past 24 hours, follow up with your primary care clinician or go to ER/urgent care."
                print "For more information, go to AAFP clinical guidelines: https://www.aafp.org/afp/2013/0515/p682.html"

            if type_of_pain == "3":
                print "Follow up with urgent care or ER as soon as possible."
                print "For more information, go to AAFP clinical guidelines: https://www.aafp.org/afp/2013/0515/p682.html"

if part == "2":
    print "Describe the problem with your. Pick one"
    print "| 1 - pain |  2 - hearing loss  |  3 - wax  |  4 - discharge |" 
    print
    problem = raw_input("> ")
    print    
                




