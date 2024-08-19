import time

class User:
    def __init__(self, nickname,password,age):
        
        self.nickname = nickname
        self.password = hash (password)
        self.age = age

class Video:
    
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.user = []
        self.videos = []
        self.current_user = []
    
    def log_in(self, nickname,password):
        
        self.nickname = nickname
        self.password = password
        
        for i in self.user():
            if i[0] == self.nickname and i[1] == self.password:
                self.current_user = self.nickname
                self.veryfy_user = 1
            elif i[0] == self.nickname and i[1] != self.password:
                self.veryfy_user = 2
        return self.veryfy_user