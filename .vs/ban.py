#!/usr/bin/env python3
CVIOLET = '\33[35m'
CRED = '\033[91m'
CEND = '\033[0m'

def showbanner():
        print(CVIOLET + '''
                 ____.__  ________         __ _________  ______
           _____/_   |  | \_____  \  _____/  |\______  \/  __  \\
  ______  /  ___/|   |  |   _(__  < /    \   __\  /    />      <   ______
 /_____/  \___ \ |   |  |__/       \   |  \  |   /    //   --   \ /_____/
         /____  >|___|____/______  /___|  /__|  /____/ \______  /
              \/                 \/     \/    ''' + CRED + "TigerShark v5" + CVIOLET + '''   \/    ''' + CEND)

        exit

showbanner()
