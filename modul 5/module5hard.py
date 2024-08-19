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
    