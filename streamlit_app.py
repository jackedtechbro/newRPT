'''
from collections import namedtuple
import altair as alt
import math
import pandas as pd
'''
import streamlit as st

st.markdown("<h1 style='text-align: center; color: white;'>THE NEW RICE PURITY TEST</h1>", unsafe_allow_html=True)


"""

The Purity Test had historically served as a segue from O-week to true college life at Rice.
However, it is soooo outdated and in desperate need of an overhaul, so here's an updated version! 

If you have completed all this you are an absolute fuckin legend. 

Click on every item you have done. MPS stands for Member of the Preferred Sex.

**Created by [@jackedtechbro](https://twitter.com/JackedTechBro/)**, idea by [@tenobrus](https://twitter.com/tenobrus/status/1678502863813885952), additional questions credit [@spoonedher](https://twitter.com/spoonedher)
"""



score = 0

score += st.checkbox("1: Held hands romantically?")
score += st.checkbox("2: Been on a date?")
score += st.checkbox("3: Been in a relationship?")
score += st.checkbox("4: Been in an ethical non-monogamous relationship?")
score += st.checkbox("5: Danced without leaving room for Jesus?")
score += st.checkbox("6: Kissed a non-family member on the lips?")
score += st.checkbox("7: French kissed?")
score += st.checkbox("8: Given or received a hickey?")
score += st.checkbox("9: Kissed or been kissed on the breast?")
score += st.checkbox("10: Kissed someone below the belt?")
score += st.checkbox("11: Kissed for more than two hours consecutively?")
score += st.checkbox("12: Played a game involving stripping?")
score += st.checkbox("13: Seen or been seen by another person in a sensual context?")
score += st.checkbox("14: Masturbated?")
score += st.checkbox("15: Masturbated to a picture or video?")
score += st.checkbox("16: Masturbated while someone else was in the room?")
score += st.checkbox("17: Been caught masturbating?")
score += st.checkbox("18: Masturbated with an inanimate object?")
score += st.checkbox("19: Massaged or been massaged sensually?")
score += st.checkbox("20: Gone through the motions of intercourse while fully dressed?")
score += st.checkbox("21: Undressed or been undressed by a MPS (member of the preferred sex)?")
score += st.checkbox("22: Showered with a MPS?")
score += st.checkbox("23: Fondled or had your butt cheeks fondled?")
score += st.checkbox("24: Fondled or had your breasts fondled?")
score += st.checkbox("25: Fondled or had your genitals fondled?")
score += st.checkbox("26: Had or given 'blue balls'?")
score += st.checkbox("27: Had an orgasm due to someone else’s manipulation?")
score += st.checkbox("28: Sent or received nudes?")
score += st.checkbox("29: Engaged in sexually explicit activity over video chat?")
score += st.checkbox("30: Subscribed to Onlyfans?")
score += st.checkbox("31: Cheated on a significant other during a relationship?")
score += st.checkbox("32: Doordashed contraceptives?")
score += st.checkbox("33: Gave or received oral sex?")
score += st.checkbox("34: Ingested some wet ass pussy?")
score += st.checkbox("35: Used a bluetooth sex toy?")
score += st.checkbox("36: Spent the night with a MPS?")
score += st.checkbox("37: Been walked in on while engaging in a sexual act?")
score += st.checkbox("38: Kicked a roommate out to commit a sexual act?")
score += st.checkbox("39: Ingested alcohol in a non-religious context?")
score += st.checkbox("40: Played a drinking game?")
score += st.checkbox("41: Been drunk?")
score += st.checkbox("42: Faked sobriety to parents or teachers?")
score += st.checkbox("43: Had severe memory loss due to alcohol?")
score += st.checkbox("44: Used a Juul?")
score += st.checkbox("45: Used marijuana?")
score += st.checkbox("46: Done drugs given to you by a stranger?")
score += st.checkbox("47: Used ketamine, methamphetamine, crack cocaine, PCP, horse tranquilizers or heroin?")
score += st.checkbox("48: Been sent to the office of a principal, dean or judicial affairs representative for a disciplinary infraction?")
score += st.checkbox("49: Created an anon Twitter or a Finsta?")
score += st.checkbox("50: Been put on disciplinary probation or suspended?")
score += st.checkbox("51: Urinated in public?")
score += st.checkbox("52: Gone skinny-dipping?")
score += st.checkbox("53: Gone streaking?")
score += st.checkbox("54: Seen a stripper?")
score += st.checkbox("55: Had the police called on you?")
score += st.checkbox("56: Run from the police?")
score += st.checkbox("57: Had the police question you?")
score += st.checkbox("58: Had the police handcuff you?")
score += st.checkbox("59: Been arrested?")
score += st.checkbox("60: Been convicted of a crime?")
score += st.checkbox("61: Been convicted of a felony?")
score += st.checkbox("62: Griefed in Minecraft?")
score += st.checkbox("63: Had sexual intercourse?")
score += st.checkbox("64: Had sexual intercourse three or more times in one night?")
score += st.checkbox("65: Had sexual intercourse 10 or more times?")
score += st.checkbox("66: Had sexual intercourse in four or more positions?")
score += st.checkbox("67: Had sexual intercourse with a position learned from TikTok?")
score += st.checkbox("68: Had sexual intercourse with a stranger or person you met on Tinder?")
score += st.checkbox("69: ?")
score += st.checkbox("70: Had sexual intercourse in a motor vehicle?")
score += st.checkbox("71: Had sexual intercourse in an autonomous vehicle?")
score += st.checkbox("72: Had sexual intercourse outdoors?")
score += st.checkbox("73: Had sexual intercourse in public?")
score += st.checkbox("74: Had sexual intercourse on livestream?")
score += st.checkbox("75: Had sexual intercourse while wearing VR headsets?")
score += st.checkbox("76: Had sexual intercourse while you or your partner’s parents were in the same home?")
score += st.checkbox("77: Had sexual intercourse with non-participating third party in the same room?")
score += st.checkbox("78: Joined the mile high club?")
score += st.checkbox("79: Participated in a 'booty call' with a partner whom you were not in a relationship with?")
score += st.checkbox("80: Traveled 100 or more miles for the primary purpose of sexual intercourse?")
score += st.checkbox("81: Had sexual intercourse with a partner with a 3 or more year age difference?")
score += st.checkbox("82: Had sexual intercourse with a virgin?")
score += st.checkbox("83: Raw dogged it?")
score += st.checkbox("84: Had a STI test due to reasonable suspicion?")
score += st.checkbox("85: Had a threesome?")
score += st.checkbox("86: Attended an orgy?")
score += st.checkbox("87: Had two or more distinct acts of sexual intercourse with two or more people within 24 hours?")
score += st.checkbox("88: Had sexual intercourse with five or more partners?")
score += st.checkbox("89: Been photographed or filmed during sexual intercourse by yourself or others?")
score += st.checkbox("90: Had engaged, watched or witnessed fetish play publicly?")
score += st.checkbox("91: Had period sex?")
score += st.checkbox("92: Had anal sex?")
score += st.checkbox("93: Tried sounding?")
score += st.checkbox("94: Impregnated someone or been impregnated?")
score += st.checkbox("95: Doordashed Plan B?")
score += st.checkbox("96: Sent a hooker money on Cash App?")
score += st.checkbox("97: Committed an act of voyeurism?")
score += st.checkbox("98: Committed an act of incest?")
score += st.checkbox("99: Worn a fursuit?")
score += st.checkbox("100: Engaged in bestiality?")
    
st.write("Your rice purity test is:", 100 - score)
#st.write()
