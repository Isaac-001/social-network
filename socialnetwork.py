## Made by: Isaac Ajayi
## My Social Network


class User:
    def __init__(self, username) :
        self.firstName = " "
        self.lastName = " "
        self.username = username
        self.bio = " "
##        self.userID = " "
        self.friends = []
        self.posts = []
        

    def addFirstName(self,firstName):
        self.firstName = firstName

    def addLastName(self,lastName):
        self.lastName = lastName

    def addBio(self, bio):
        self.bio = bio

    def addFriend(self,name):
        self.friends.append(name)

    def addPost(self,posts):
        self.posts.append(posts)
        
    def unFriend(self,obj):
        for friend in self.friends:
            if friend.username == obj.username:
                self.friends.remove(obj)

    def viewNewsFeed(self):
        for i in self.friends:
            print(i.posts)

    def viewFriends(self):
        print("Friends List")
        for e in self.friends:
            print(e.username)
        

if __name__ == "__main__":
    FirstName = "Isaac"
    lastName = "Ajayi"
    username = "Isaac_da_lion_killer"
    bio = "nah"
    userID = "4171"

    isaac = User("Isaac_da_lion_killer")
    isaac.addFirstName("Isaac")
    lucy = User("lucccccy")
    lucy.addLastName("Lucille")
    jucy = User("not_jucy")
    jason = User("hoihoi")
    chad = User("jason")
    isaac.addBio("nah")
    isaac.addPost("chickenchicken")
##    print("First name: ")
    print(isaac.firstName)
##    print("Las Name: ")
    print(lucy.username)
    print(lucy.lastName)
    
    

    isaac.addFriend(lucy)
    isaac.addFriend(jucy)
    isaac.addFriend(jason)
    isaac.addFriend(chad)
    print(isaac.username)
    lucy.addPost("chicken boi")
    jucy.addPost("Do it for our master, Daddy Trump -Obama 2018")
##    print(isaac.bio)
    isaac.viewFriends()
    isaac.unFriend(jason)
##    isaac.viewNewsFeed()
    isaac.viewFriends()
    
        
