from cloudfoundry_client.entities import Entity, EntityManager


class BuildpackManager(EntityManager):
    def __init__(self, target_endpoint, client):
        super(BuildpackManager, self).__init__(target_endpoint, client, '/v2/buildpacks',
                                               lambda pairs: Entity(target_endpoint, client, pairs))

    def update(self, buildpack_guid, parameters):
        return super(BuildpackManager, self)._update(buildpack_guid, parameters)
