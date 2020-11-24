import sys
import time
import sgl_constants as const

def welcome():
    print('Hi SGL data collector, welcome! Mint City is the Best! Charlotte Til I Die!')
    print("""
                                       .
				     wWWWw
                                 mWWWw   wWWW;
                            .mWWWW’    ,-,,’;WWWWw.
                        .mWWW’’  _____^______  ‘’WWWWm.
		    .mWWWM’     /MMMMMMMMMMMMM\    ‘WWWWm.
                 .mWWWM’’      (W(  )MWMMW(  )M)       ‘WWWWm.
             .mWWWWM’           \WmmW-----WmmW/          ‘’WWWMm.
	     WMM’	          ‘’       ‘’                 WMM
             WMM  MMMMMMMMMMMM  MMMMMMMMMMMMM   MMMMM         WMM
             WMM  MMMMMMMMMMMM  MMMMMMMMMMMMM   MMMMM         WMM
             MMM  MMMMM   MMMM  MMMMM           MMMMM         WMM
             MMM  ‘MMMMM.       MMMMM           MMMMM         MMM
             MMM    ‘MMMMMm.    MMMMM  MMMMMM   MMMMM         MMM
             MMM        ‘MMMMM  MMMMM  MMMMMM   MMMMM         MMM
             MMM  MMMMM   MMMM  MMMMM    MMMM   MMMMM         MMM
             MMM  WWWWWWWWWWWW  WWWWWWWWWWWWW   WWWWWWWWWWWW  MMM
             MMM  WWWWWWWWWWWW  WWWWWWWWWWWWW   WWWWWWWWWWWW  MMM
             WWW  ______   ______   ______   ______   ______  MMM
             MMM  MMMMMM   MMMMMM   MMMMMM   MMMMMM   MMMMMM  MMM
             WWW   ‘WWWW   MMMMMM   MMMMMM   MMMMMM   WWWW’   MMM
             MMMm.    ‘M   M CAN!   M USA!   M MEX!    W’   .mWWW
               ‘TWWWMm     MWWWWM   MWMMMW   MMMMMM     ‘MMMM’
                   ‘TMMMW.   ‘TWM   MMMMMM   MMT’   ;MMMMM’ 
                      ‘TMMMW.   ‘   MMMMMM  ‘   .;MMMM’
                          ‘TMMMM;.  ‘’MT’’  ./MMMM’’ 
                              ‘TMMMM;.  .;WMMMM’ 
                                  ‘TMMMMMMT’
                                     ‘TT’

        """)
    if len(sys.argv) == 1:
        handleNoArgs()
    elif len(sys.argv) == 2:
        handleOneArg()
    elif len(sys.argv) == 4:
        handleSteamNameAndDateRange()
        
    print(len(sys.argv))

#Get the command args via MENU
def getCmdMatchIds():
    print("""Enter match IDs: 
    (enter as many as you\'d like, when done hit enter with blank line)
    (if none at all, hit enter with blank line to proceed to player ID args)
    """)
    blankEntered = False
    i = 1
    matchIDs = []
    while blankEntered == False:
        matchId = input('Enter match ' + str(i) + ' ID: ')
        i+=1
        if matchId == '':
            blankEntered = True;
            if len(matchIDs) > 0:
                print('\nRecieved ' + str(len(matchIDs))+ ' Match IDs: ')
                for match in matchIDs:
                    print(match + ", ", end='')
                print()
        else:
            matchIDs.append(matchId)
    return matchIDs

def getCmdSteamName():

    uploaderDict = const.uploaderDict

    steamNames = uploaderDict.keys()
    steamIDs = uploaderDict.keys()
    idValue = None

    while idValue is None:
        playerNameOrIDinput = input('\nSteam name or player ID of who uploaded this weeks matches to Ballchaser.com: ')
        playerNameOrIDinput = playerNameOrIDinput.lower()

        holder = playerNameOrIDinput
    
        idValue = uploaderDict.get(playerNameOrIDinput)
        
        if idValue is None and holder != '':
            print('Sorry could not validate an ID for that input, try again or enter blank to end.')
        elif holder == '':
            print('Ending')
            return
    return(idValue)

#goes into menus and prompts user for inputs
def handleNoArgs():
        print('You called the script without game id, player id, or date ranges.'+
              '\nOpening cmd ln MENU:')
        time.sleep(.5)
        print('.')
        time.sleep(.5)
        print('.')

        matchIDs = getCmdMatchIds()
        if len(matchIDs) == 0:
            playerId = getCmdSteamName()
            print('\nrecieved player id ' + playerId)

#signle arg can be match id OR player id, will have to solve
def handleOneArg():
    pass

# 3 args, currently assuming steamName/id + 2dates
def handleSteamNameAndDateRange():
    pass
