print('This program calculates the perfect sensitivity based on your liking')
print('                                                                                                                ')
print('                                                                                                                ')
print('                                                                                                                ')
data_valid =False


while data_valid == False :
    dpi = input('type the dpi you are using (ex: 800 or 1600) ')
    print('                                                                                                                ')
    try:
        dpi = float(dpi)
    except:
        print('Invalid input. Only numbers are accepted.')
        continue
    if dpi <= 0:
            print('The dpi should be above 0. It cannot be below or equal to 0')
            continue
    else:
        data_valid = True

ms = 280/dpi
hs = ms*2
ls = ms/2

print('High SEN---Middle SEN---Low SEN')
print(' ---',hs,' -------',ms,'------- ',ls,'--- ')
print('                                                                                                                ')
print('Now use the high sens and low sens and choose which one you like the most')
print('                                                                                                                ')



def LDSChoice():
    while True:
        LDS = input('Which sensitivity did you like? Put in the form 1=High Sens or 2=Low Sens. ')
        print('                                                                                                                          ')

        try:
            LDS = float(LDS)
        except:
            print('Invalid input. Only 1 or 2 are accepted.')
            continue
        if LDS <1:
            print('Invalid input. Only 1 or 2 are accepted')
            continue
        elif LDS >2:
            print('Invalid input. Only 1 or 2 are accepted')
            continue
        else:
            return LDS


LDS = LDSChoice()


if LDS == 1:
        Nhs = round(hs,3)
        Nms = round(((hs+ms)/2),4)
        Nls = round(ms,3)
        print('The new values for the High SEN, Middle SEN, and Low SEN are as listed in the same order')
        print('                                                                                                                          ')
        print('High Sens-',Nhs,', Middle Sens-',Nms,', Low Sens-',Nls)
elif LDS == 2:
        Nhs = round(ms,3)
        Nms = round(((ms+ls)/2),4)
        Nls = round(ls,3)
        print('The new values for the High SEN, Middle SEN, and Low SEN are as listed in the same order')
        print('                                                                               ')
        print('High Sens-',Nhs,', Middle Sens-',Nms,', Low Sens-',Nls)
        print('                                                                               ')



while True:
    ynchoice = input('Do you wish to continue getting a better sens? Yes/No? ').lower()
    print('                                                                               ')
    if ynchoice == 'yes' or ynchoice == 'y' or ynchoice == '2':
        LDS = LDSChoice()
        if LDS == 1:
            Nhs = round(Nhs,3)
            Nms = round(((Nhs+Nms)/2),4)
            Nls = round(Nms,3)
            print('                                                                                                                                     ')
            print('The new values for the High SEN, Middle SEN, and Low SEN are as listed in the same order')
            print('                                                                               ')
            print('High Sens-',Nhs,', Middle Sens-',Nms,', Low Sens-',Nls)
            print('                                                                               ')
        elif LDS == 2:
            Nhs = round(Nms,3)
            Nms = round(((Nms+Nls)/2),4)
            Nls = round(Nls,3)
            print('                                                                                                                                     ')
            print('The new values for the High SEN, Middle SEN, and Low SEN are as listed in the same order')
            print('                                                                               ')
            print('High Sens-',Nhs,', Middle Sens-',Nms,', Low Sens-',Nls)
            print('                                                                               ')
    elif ynchoice == 'no' or ynchoice == 'n' or ynchoice == '1':
        break

        
    
