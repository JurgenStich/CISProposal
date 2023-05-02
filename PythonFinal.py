


#WELCOME TO LIFETIMENAMES! THE PREMIER SITE FOR EVALUATING POTENTIAL BABY NAMES! Note: This software only supports China, India, and the Uited States so far,#
#Check back in the future for more additions!#


import random
import difflib

def getCloseMatches(word, possibilities):
    closeMatches = []
    for name in possibilities:
        if name == word:
            return [name]
        elif abs(len(name) - len(word)) > 1:
            continue
        elif name.lower() == word.lower():
            return [name]
        elif difflib.SequenceMatcher(None, name.lower(), word.lower()).ratio() >= 0.8:
            closeMatches.append(name)
        elif len(word) == len(name) - 1 and name.lower().startswith(word.lower()):
            closeMatches.append(name)
        elif len(word) == len(name) + 1 and word.lower().startswith(name.lower()):
            closeMatches.append(name)
    return closeMatches

def evaluateName(proposedName, proposedCountry):
    if proposedCountry not in countryNames:
        return "I don't currently support names from {}. Check back soon for future additions!".format(proposedCountry)
    else:
        topNames = countryNames[proposedCountry]
        if proposedName in topNames:
            rank = topNames[proposedName]
            if rank <= 10:
                return "Great name choice! That name is ranked within the top ten most popular names of {} at rank {}.".format(proposedCountry, rank)
            else:
                return "That's a fantastic name! It's ranked {} in {}.".format(rank, proposedCountry)
        else:
            closeNames = getCloseMatches(proposedName, topNames.keys())
            if closeNames:
                return "Did you mean the name {}? If not, that's an very unique exciting variation of {}, great choice!".format(closeNames[0], closeNames[0])
            else:
                otherCountries = [c for c in countryNames.keys() if c != proposedCountry]
                for country in otherCountries:
                    if proposedName in countryNames[country]:
                        popularName = random.choice(list(countryNames[proposedCountry].keys()))
                        return "That name may be culturally obscure in {}. How about using a more popular name in {} like {}? If not, your child will stand out from the crowd in the best way!".format(proposedCountry, proposedCountry, popularName)
                randomName = random.choice(list(topNames.keys()))
                return "I do not recognize this name for {}, it's very unique!. If you would like a recommendation for a more popular name, try {} instead. ".format(proposedCountry, randomName)


proposedCountry = input("Are you from China, India, or the U.S.? ")
proposedName = input("What is your proposed name? ")

chinaNames = {
    "Muchen": 1,  "Wang": 2,  "Haoyu": 3,  "He": 4,  "Chen": 5,  "Yize": 6,  "Zhao": 7,  "Huang": 8,  "Zhou": 9,  "Wu": 10,  "Xu": 11,  "Sun": 12,  "Ma": 13,
    "Yize": 14,  "Zhang": 15,  "Lin": 16,  "Fang": 17,  "Guo": 18,  "Lu": 19,  "Wei": 20,  "Yan": 21,  "Xie": 22,  "Qian": 23,  "Feng": 24,  "Deng": 25,  "Cao": 26,
    "Song": 27,  "Tang": 28,  "Yu": 29,  "Jin": 30,  "Zeng": 31,  "Xiao": 32,  "Li": 33,  "Yang": 34,  "Dong": 35,  "Yuan": 36,  "Xiang": 37,  "Jiang": 38,
    "Shen": 39, "Zhu": 40, "Yu": 41, "Muyang": 42, "Mao": 43, "Zou": 44, "Xue": 45, "Han": 46, "Haoran": 47, "Xia": 48, "Chu": 49, "Niu": 50}

usNames = {
    "Liam": 1, "Noah": 2, "Oliver": 3, "Elijah": 4, "William": 5, "James": 6, "Benjamin": 7, "Lucas": 8, "Henry": 9, "Alexander": 10, "Mason": 11, "Michael": 12,
    "Ethan": 13, "Daniel": 14, "Jacob": 15, "Logan": 16, "Jackson": 17, "Levi": 18, "Sebastian": 19, "Mateo": 20, "Jack": 21, "Owen": 22, "Theodore": 23, "Aiden": 24,
    "Samuel": 25, "Grayson": 26, "Leo": 27, "Asher": 28, "Wyatt": 29, "Lincoln": 30, "Carter": 31, "Gabriel": 32, "Julian": 33, "Matthew": 34, "Leo": 35, "Nicholas": 36,
    "Nathan": 37, "Ezra": 38, "Isaac": 39, "Jayden": 40, "Eli": 41, "David": 42, "Joseph": 43, "Samuel": 44, "Henry": 45, "Max": 46, "Ethan": 47, "Anthony": 48, "Christopher": 49, "Joshua": 50}

indiaNames = {
     "Aarav": 1,"Aakrit": 2,"Vivaan": 3,"Amay": 4,"Ansh": 5,"Anuv": 6,"Arnav": 7,"Dhruv": 8,"Shaurya": 9,"Miraj": 10,"Naksh": 11,"Rudra": 12,"Mohammed": 13,"Ayaan": 14,
    "Aryan": 15,"Dheeraj": 16,"Arjun": 17,"Anay": 18,"Abhinav": 19,"Daiwik": 20,"Veer": 21,"Advik": 22,"Kabir": 23,"Aniruddha": 24,"Ansh": 25,"Devansh": 26,"Sarthak": 27,"Siddharth": 28,"Darsh": 29,
    "Aaryan": 30,"Aarush": 31,"Neel": 32,"Rohan": 33,"Rishi": 34,"Aryan": 35,"Nirvaan": 36,"Anshuman": 37,"Aryaveer": 38,"Hriday": 39,"Krish": 40,"Aditya": 41,"Vansh": 42,"Dhairya": 43,
    "Dhruva": 44, "Priyansh": 45, "Sai": 46, "Neil": 47, "Pranav": 48, "Vyan": 49, "Vedant": 5}

countryNames = {
    "China": chinaNames,
    "India": indiaNames,
    "U.S.": usNames}

print(evaluateName(proposedName, proposedCountry))
