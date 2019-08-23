from chili.gateway import ServiceClient, service_client


class ArticleClient(ServiceClient):

    @service_client('service_name', 'function_name')
    async def get_blogger_list(self, json=None):
        pass

