# pip install requests
import requests
# pip install google-cloud-firestore
from google.cloud import firestore
import google.oauth2.credentials

from AIArena.AI import AI as AI

# Firestore client Documentation
# https://googleapis.dev/python/firestore/latest/client.html

projectApiKey = "AIzaSyClwnfN0p2V6tZlIMEANkh7M9PLJoo818U"
projectId = "ai-olympics"

class User:
    def __init__(self, email, password):
        print("t1")
        self.fb = Firebase(email,password)
        print("t2")

    def isAI(self, ai):
        if not issubclass(ai.__class__, AI):
            print("That AI does not inherit aiolympics.AI")
            return False
        return True

    def startGame(self, ai):
        if not self.isAI(ai):
            return False
        print("t3")
        self.fb.startGame(ai.name, ai.game)
        print("t4")




class Firebase:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.uid = None

        self.idToken = None
        self.idToken = self.authenticateUser()
        #self.db = self.returnDatabaseReference()


    def authenticateUser(self):
        """
        Authenticates user for the given firestore project
        :return:
        """
        url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={0}'.format(projectApiKey)
        payload = {
            "email": self.email,
            "password": self.password,
        }
        response = requests.post(url, data=payload).json()
        if not response or 'error' in response.keys():
            raise Exception(response)
        return response['idToken']


    def getUserAccessToken(self):
        """
        Responsible for obtaining Access Token for client from the Id Token
        :return: Access Token
        """
        url = 'https://securetoken.googleapis.com/v1/token'
        payload = {
            'grant_type': 'authorization_code',
            'code': self.idToken,
            'key': projectApiKey,
        }


        response = requests.post(url,data=payload).json()
        if not response or 'error' in response.keys():
            raise Exception(response)

        accessToken = response['access_token']
        print(response)
        self.uid = response['user_id']
        print(self.uid,"**************************************")
        return accessToken

    def returnDatabaseReference(self):
        """
        Creates A Firestore client Object that can be used by client for accessing collections / documents
        :return: Firestore client Object
        """
        accessToken = self.getUserAccessToken()
        credentials = google.oauth2.credentials.Credentials(accessToken)
        return firestore.Client(project=projectId, credentials=credentials)

    def startGame(self, name, game):
        print("make a game:", name, game)
        db = self.returnDatabaseReference()
        doc_ref = db.collection('MatchMaker').document(game).collection('Challenges')
        doc_ref.document().set({
            "uid":self.uid,
            "name":name,
            "game":game
        })

class fireAPI:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.uid = None

        #self.client = Client(credentials=credentials)
