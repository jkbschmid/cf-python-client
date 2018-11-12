from cloudfoundry_client.json_object import JsonObject


class ResourceManager(object):
    def __init__(self, target_endpoint, client):
        self.target_endpoint = target_endpoint
        self.client = client

    def match(self, items):
        response = self.client.put('%s/v2/resource_match' % self.client.info.api_endpoint, json=items)
        return response.json(object_pairs_hook=JsonObject)
