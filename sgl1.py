import requests
import pprint
import json
import sys
import time
import sgl_cmd_helper as cmdh
import sgl_ballchaser_api_helper as bcapi

def main():
    #TODO: change from just calling for hardcoded test game to list of all the games
    cmdh.welcome()
    data = bcapi.apiCallByReplayId('1ef2f98e-d7d9-45a3-b2dd-7e92a2da73b0')
    #print(data)
    print(data['blue']['players'][0]['camera']['fov'])
    bcapi.apiCallReplays(76561198977461300, )
    
if __name__ == '__main__':
    main()
