class UserData:
    def __init__(self, username) -> None:
        self.username = username

    def writing(self, gamename):
        try:
            user_data = open(
                f"./core/critcalfiles/{self.username}_data.txt", "a+")
            user_data.writelines(f"{gamename} \n")
            user_data.close()
        except:
            print("cat")

    def reading(self):
        try:
            user_data = open(
                f"./core/critcalfiles/{self.username}_data.txt", "r")
            k = user_data.read().splitlines()
            for i in range(0, len(k)-1):
                if i == 0:
                    continue
                if k[i] == k[i-1]:
                    k.pop(i)
                else:
                    continue
            user_data.close()
            return k
        except:
            return []
