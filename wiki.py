import requests
import json
import sys

#print ("Finding next episode details of %s" % str(sys.argv[1]))

#nameOfShow = input('Hello! Enter the name of the show: \n')
nameOfShow = sys.argv[1]
omdbBaseUrl = 'http://www.omdbapi.com/?'

omdb_my_atts = {'r': 'json',  't': nameOfShow}

omdb_resp = requests.get(omdbBaseUrl, params = omdb_my_atts)

# print("\n")
# print(omdb_resp.url)

IMDBdata = omdb_resp.json()
# print("\n")
# print(IMDBdata)

# print("\n")

imdbID = IMDBdata["imdbID"]

# print (imdbID)

# tv maze search for next episode

tvMazeBaseUrl = 'http://api.tvmaze.com/lookup/shows?'

tvMaze_my_atts = {'imdb': imdbID}

tvMaze_resp = requests.get(tvMazeBaseUrl, params = tvMaze_my_atts)

#print(tvMaze_resp.url)

tvMazedata = tvMaze_resp.json()
# print("\n")
#print(tvMazedata) #this is a string
# print("\n")

nextEpisodeURL = tvMazedata['_links']['nextepisode']['href']
nextEpisodeCountry = tvMazedata['network']['country']['name']
nextEpisodeURL_resp = requests.get(nextEpisodeURL)

#print(nextEpisodeURL_resp.url)

nextEpisodeData = nextEpisodeURL_resp.json()

#print("\n")

#print(nextEpisodeData)

#print("\n")

nextEpisodeNumber = str(nextEpisodeData['number'])
nextEpisodeSeason = str(nextEpisodeData['season'])
nextEpisodeDate = nextEpisodeData['airdate']
nextEpisodeTime = nextEpisodeData['airtime']
nextEpisodeName = nextEpisodeData['name']


print("The next episode [Episode " + nextEpisodeNumber + " - " + nextEpisodeName + "] of season " + nextEpisodeSeason + " of " + nameOfShow + " will premiere on " + nextEpisodeDate + " at " + nextEpisodeTime + " in " + nextEpisodeCountry)

#print("\n\n************Thanks for using this script!!************")
