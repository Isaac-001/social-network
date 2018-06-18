## Made by: Isaac Ajayi
## My Social Network


class User:
    def __init__(self, firstName, lastName, username, bio, userID) :
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.bio = bio
        self.userID = userID
        self.friends = []
        self.posts = []

    def addFriend(self,username):
       self.friends.append(username)

##    def unFriend():
##
##    def viewNewsFeed():


if __name__ == "__main__":
    firstName = "Isaac"
    lastName = "Ajayi"
    username = "Isaac_da_lion_killer"
    bio = "nah"
    userID = 4171

    isaac = User(firstName, lastName, username, bio, userID)
        
