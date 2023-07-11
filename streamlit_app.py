from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Welcome to the New Rice Purity Test! :heart:

Edit `/streamlit_app.py` to customize this app to your heart's desire 

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

'''
with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
'''

score = 0

score += st.checkbox("1. Held hands romantically?")
score += st.checkbox("2. Been on a date?")
score += st.checkbox("3. Been in a relationship?")
score += st.checkbox("4. Danced without leaving room for Jesus?")
score += st.checkbox("5. Kissed a non-family member?")
score += st.checkbox("6. Kissed a non-family member on the lips?")
score += st.checkbox("7. French kissed?")
score += st.checkbox("8. French kissed in public?")
score += st.checkbox("9. Kissed on the neck?")
score += st.checkbox("10. Kissed horizontally?")
score += st.checkbox("11. Given or received a hickey?")
score += st.checkbox("12. Kissed or been kissed on the breast?")
score += st.checkbox("13. Kissed someone below the belt?")
score += st.checkbox("14. Kissed for more than two hours consecutively?")
score += st.checkbox("15. Played a game involving stripping?")
score += st.checkbox("16. Seen or been seen by another person in a sensual context?")
score += st.checkbox("17. Masturbated?")
score += st.checkbox("18. Masturbated to a picture or video?")
score += st.checkbox("19. Masturbated while someone else was in the room?")
score += st.checkbox("20. Been caught masturbating?")
score += st.checkbox("21. Masturbated with an inanimate object?")
score += st.checkbox("22. Seen or read pornographic material?")
score += st.checkbox("23. Massaged or been massaged sensually?")
score += st.checkbox("24. Gone through the motions of intercourse while fully dressed?")
score += st.checkbox("25. Undressed or been undressed by a MPS (member of the preferred sex)?")
score += st.checkbox("26. Showered with a MPS?")
score += st.checkbox("27. Fondled or had your butt cheeks fondled?")
score += st.checkbox("28. Fondled or had your breasts fondled?")
score += st.checkbox("29. Fondled or had your genitals fondled?")
score += st.checkbox("30. Had or given 'blue balls'?")
score += st.checkbox("31. Had an orgasm due to someone else’s manipulation?")
score += st.checkbox("32. Sent a sexually explicit text or instant message?")
score += st.checkbox("33. Sent or received sexually explicit photographs?")
score += st.checkbox("34. Engaged in sexually explicit activity over video chat?")
score += st.checkbox("35. Cheated on a significant other during a relationship?")
score += st.checkbox("36. Purchased contraceptives?")
score += st.checkbox("37. Gave oral sex?")
score += st.checkbox("38. Received oral sex?")
score += st.checkbox("39. Ingested someone else’s genital secretion?")
score += st.checkbox("40. Used a sex toy with a partner?")
score += st.checkbox("41. Spent the night with a MPS?")
score += st.checkbox("42. Been walked in on while engaging in a sexual act?")
score += st.checkbox("43. Kicked a roommate out to commit a sexual act?")
score += st.checkbox("44. Ingested alcohol in a non-religious context?")
score += st.checkbox("45. Played a drinking game?")
score += st.checkbox("46. Been drunk?")
score += st.checkbox("47. Faked sobriety to parents or teachers?")
score += st.checkbox("48. Had severe memory loss due to alcohol?")
score += st.checkbox("49. Used tobacco?")
score += st.checkbox("50. Used marijuana?")
score += st.checkbox("51. Used a drug stronger than marijuana?")
score += st.checkbox("52. Used methamphetamine, crack cocaine, PCP, horse tranquilizers or heroin?")
score += st.checkbox("53. Been sent to the office of a principal, dean or judicial affairs representative for a disciplinary infraction?")
score += st.checkbox("54. Been put on disciplinary probation or suspended?")
score += st.checkbox("55. Urinated in public?")
score += st.checkbox("56. Gone skinny-dipping?")
score += st.checkbox("57. Gone streaking?")
score += st.checkbox("58. Seen a stripper?")
score += st.checkbox("59. Had the police called on you?")
score += st.checkbox("60. Run from the police?")
score += st.checkbox("61. Had the police question you?")
score += st.checkbox("62. Had the police handcuff you?")
score += st.checkbox("63. Been arrested?")
score += st.checkbox("64. Been convicted of a crime?")
score += st.checkbox("65. Been convicted of a felony?")
score += st.checkbox("66. Committed an act of vandalism?")
score += st.checkbox("67. Had sexual intercourse?")
score += st.checkbox("68. Had sexual intercourse three or more times in one night?")
score += st.checkbox("70. Had sexual intercourse 10 or more times?")
score += st.checkbox("71. Had sexual intercourse in four or more positions?")
score += st.checkbox("72. Had sexual intercourse with a stranger or person you met within 24 hours?")
score += st.checkbox("73. Had sexual intercourse in a motor vehicle?")
score += st.checkbox("74. Had sexual intercourse outdoors?")
score += st.checkbox("75. Had sexual intercourse in public?")
score += st.checkbox("76. Had sexual intercourse in a swimming pool or hot tub?")
score += st.checkbox("77. Had sexual intercourse in a bed not belonging to you or your partner?")
score += st.checkbox("78. Had sexual intercourse while you or your partner’s parents were in the same home?")
score += st.checkbox("79. Had sexual intercourse with non-participating third party in the same room?")
score += st.checkbox("80. Joined the mile high club?")
score += st.checkbox("81. Participated in a 'booty call' with a partner whom you were not in a relationship with?")
score += st.checkbox("82. Traveled 100 or more miles for the primary purpose of sexual intercourse?")
score += st.checkbox("83. Had sexual intercourse with a partner with a 3 or more year age difference?")
score += st.checkbox("84. Had sexual intercourse with a virgin?")
score += st.checkbox("85. Had sexual intercourse without a condom?")
score += st.checkbox("86. Had a STI test due to reasonable suspicion?")
score += st.checkbox("87. Had a STI?")
score += st.checkbox("88. Had a threesome?")
score += st.checkbox("89. Attended an orgy?")
score += st.checkbox("90. Had two or more distinct acts of sexual intercourse with two or more people within 24 hours?")
score += st.checkbox("91. Had sexual intercourse with five or more partners?")
score += st.checkbox("92. Been photographed or filmed during sexual intercourse by yourself or others?")
score += st.checkbox("93. Had period sex?")
score += st.checkbox("94. Had anal sex?")
score += st.checkbox("95. Had a pregnancy scare?")
score += st.checkbox("96. Impregnated someone or been impregnated?")
score += st.checkbox("97. Paid or been paid for a sexual act?")
score += st.checkbox("98. Committed an act of voyeurism?")
score += st.checkbox("99. Committed an act of incest?")
score += st.checkbox("100. Engaged in bestiality?")


    
st.write("Your rice purity test is:")
st.write(100 - score)
