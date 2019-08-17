from . import BaseTag, BaseSingletonTag


class Audio(BaseTag):
    tag_name = 'audio'


class Source(BaseSingletonTag):
    tag_name = 'source'


class Track(BaseSingletonTag):
    tag_name = 'track'


class Video(BaseTag):
    tag_name = 'video'
