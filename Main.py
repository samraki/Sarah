# -*- coding: utf-8 -*-
""" 
This is the Main file of Sarah
#TODO: This Doctype needs changes
""" 

#importings :
import re 
from Modules import STranslator, SWebscraper, SEmoji, SWikipedia, Stts
from Data import IntroOptions, langs, YES
from random import choice
from Setting import *
from webbrowser import open_new_tab as ont


intro = choice(IntroOptions)
Stts.say(intro)
intro_emoji = ["wink", "v", "smile"]
_emoji = SEmoji.Emoji(choice(intro_emoji)) #making a random emoji
intro = ("{} {}".format(intro, _emoji))
Stts.type(intro) #introducing to user

try :
    while True:
        inp = input("~> ")
        if inp is "" : # if the entered value was empty i'll pass
            pass #passing
        #---
        elif (inp[0:9] == "TRANSLATE") or (inp[0:9] == "Translate") or (inp[0:9] == "translate") :
            Content = inp[10:]
            Dest = input("To what language? Leave empty for using the default ({}) ".format(TDL))
            if Dest == "" :
                Dest = langs[TDL]
            else :
                for lang in langs.keys() :
                    if lang in Dest :
                        Dest = langs[lang]
            print(STranslator.Translate(Content, Dest))
        #---
        elif ("about" in inp or "About" in inp or "ABOUT" in inp) :
            pass
        else :
            try:
                print(SWikipedia.Compliter(SWikipedia.Wikipedia(inp)))
                Morecheck = input("Type More to see the whole article ")
                if ("More" in Morecheck) or ("more" in Morecheck) or ("MORE" in Morecheck) :
                    print("Opening Browser ...")
                    ont(SWikipedia.GetURL(inp))
            except:
                print("I'm sorry I didn't understand what did you mean, and I couldn't find any match for in Wikipeia\
                    \nBut in still can search it for you in {}".format(DiffBrow))
                SearchAsk = input("Do You Want? ")
                if SearchAsk in YES :
                    print("Opening Browser ...")
                    url = "https://www.google.com/search?client=ubuntu&channel=fs&q={}&ie=utf-8&oe=utf-8".format(inp)
                    ont(url)


except (KeyboardInterrupt):
    print("\nSure, Closing ...")
    try :
        exit()
    except:
        quit()
