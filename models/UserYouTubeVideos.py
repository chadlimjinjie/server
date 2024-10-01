from mongoengine import Document, StringField

class UserYouTubeVideos(Document):
    videoId = StringField()
    title = StringField()
    description = StringField()
