import phpserialize
from django.utils.encoding import force_bytes


from redis_sessions.session import SessionStore as RedisStore

class SessionStore(RedisStore):
    '''
    Thanks to Alex Ezell for assistance on this php-django session engine.
    http://groups.google.com/group/django-users/browse_thread/thread/f5b464379f2e4154/e358161c95e507c0

    Override the default database session backend to use php-style serialization.
    '''
    def __init__(self, session_key=None):
        # call the super class's init
        super(SessionStore, self).__init__(session_key)

    def decode(self, session_data):
        return phpserialize.loads(force_bytes(session_data), decode_strings=True)

    def encode(self, session_dict):
        return phpserialize.dumps(session_dict)
