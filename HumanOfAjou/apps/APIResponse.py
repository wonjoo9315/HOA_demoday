class APIResponse(object):
    APICode = None
    APIMessage = None
    APIPayload = None

    def __init__(self, **kwargs):
        self.APICode = kwargs.get('APICode')
        self.APIMessage = kwargs.get('APIMessage')
        self.APIPayload = kwargs.get('APIPayload')

    @property
    def generate(self):
        return {'APICode': self.APICode, 'APIMessage': self.APIMessage, 'APIPayload': self.APIPayload}