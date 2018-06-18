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
    def viewNewsFeed(self,friends):
        self.f.posts.append(username)


if __name__ == "__main__":
    firstName = "Isaac"
    lastName = "Ajayi"
    username = "Isaac_da_lion_killer"
    bio = "nah"
    userID = "4171"

    isaac = User(firstName, lastName, username, bio, userID)
    lucy = User("Lucy", "Jones", "lucccccy", "np", "5151")
    jucy = User("Jucy", "Jones", "jucccccy", "the world is loss", "5191")
    print("First name: ")
    print(isaac.firstName)
    print("Last Name: ")
    print(lucy.firstName)
    

    isaac.addFriend("lucccccy")
    isaac.addFriend("jucccccy")
    
    print(isaac.friends)
    lucy.posts.append("chicken boi")
    jucy.posts.append("Do it for our master, Daddy Trump -Obama 2018")
##    print(lucy.posts)
##    print(jucy.posts)
    for f in isaac.friends:
            print(f.posts)
    isaac.viewNewsFeed(isaac.friends)
    
    
