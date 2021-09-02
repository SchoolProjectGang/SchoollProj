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
        user_data = open(
            f"./core/critcalfiles/{self.username}_data.txt", "r")
        k = user_data.readlines()
        if len(k) == 0:
            return ["No Games"]
        else:
            new_arr = []
            for i in range(0, len(k)):
                if k[i] == k[i-1]:
                    pass
                else:
                    new_arr.append(k[i])
        user_data.close()
        return new_arr
