import csv
import numpy as np
import streamlit as st
weaptype = 0
weapname = 0
weapelement = 0
weakness = "Weak"
weapdmg = 0

weapfile = csv.reader(open(r'kotdrebirthweapons.csv', newline='\n',encoding='utf-8-sig'))
#need full filepath here cause streamlit can't handle it otherwise!#



st.header("astro's KOTD damage calculator")
st.subheader('Original calculations by Mack!')
st.write('This will tell you what number to react with when gathering for a raid :)')

st.write('-------')
blust = st.checkbox('Check me you have blood lust')
weapid = st.number_input('What weapon ID are you using?', step=1)
lvl = st.number_input('What level are you?', step=1)
bosstype = st.selectbox('What type is the boss?', ['Melee','Ranged','Magic'])
st.write('-------')

for item in weapfile:
    if int(weapid) == int(item[0]):
        weaptype = item[1]
        weapname = item[2]
        weapdmg = item[3]
        weapelement = item[4]
        st.write(f'Current selected weapon is: **{weapname}**')
        st.write(f'This is a **{weaptype}** weapon. Make sure the level you put in is your **{weaptype}** level')
        elementtowrite = 'is boss weak to ' + weapelement + '?'
        weakness = st.selectbox(elementtowrite, ['Weak','Noot','Resist'])


if st.button('Calc my damage'):
    # damage calcs
    # (base + weapon + element + type)*BloodLust

    # element info
    if weakness == "Weak":
        evar = 0.5
    elif weakness == "Resist":
        evar = -0.5
    elif weakness == "Noot":
        evar = 0
    else:
        evar = 0

    # boss type info
    # stupid rock paper scissors that my stupid brain just refuses to remember!
    if bosstype == "Melee":
        if weapelement == "Melee":
            tvar = 0
        elif weapelement == "Ranged":
            tvar = -0.1  # ranged loses to melee
        elif weapelement == "Magic":
            tvar = 0.1  # magic wins to melee
        else:
            tvar = 0

    elif bosstype == "Ranged":
        if weapelement == "Melee":
            tvar = 0.1  # melee wins to ranged
        elif weapelement == "Ranged":
            tvar = 0
        elif weapelement == "Magic":
            tvar = -0.1  # magic loses to ranged
        else:
            tvar = 0

    elif bosstype == "Magic":
        if weapelement == "Melee":
            tvar = -0.1  # melee loses to magic
        elif weapelement == "Ranged":
            tvar = 0.1  # ranged wins to magic
        elif weapelement == "Magic":
            tvar = 0
        else:
            tvar = 0

    #blust info
    if blust == True:
        bvar = 2
    else:
        bvar =1

    if weapdmg == 0:
        st.write('Select a weapon u idiot')
    else:
        basedmg = float(3.5 + ((lvl / 10) - 2.34 + (3.65 * np.log(lvl))) / 2)
        weapondmg = float(weapdmg)
        elementdmg = float(evar * weapondmg)
        typedmg = float(tvar * weapondmg)

        totaldmg = (basedmg + weapondmg + elementdmg + typedmg)*bvar
        dmgrounddown = np.floor(totaldmg)
        react= int(dmgrounddown/5)

        st.subheader('Total estimated dmg is: ' + str(int(dmgrounddown)))
        st.write(f'For a Gnome Raid, you should react with a **{react}**')





