class Model:
    _model = None
    _base_url = None
    _api_key = None
    _description = None

    def __init__(self, model, base_url, api_key, description):
        self._model = model
        self._base_url = base_url
        self._api_key = api_key
        self._description = description

    def to_config(self):
        return {
            "model": self._model,
            "api_key": self._api_key,
            "base_url": self._base_url,
        }
    
    def test(self):
        pass
        
