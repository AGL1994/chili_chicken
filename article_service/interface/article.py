from chili.gateway import ServiceClient, service_client


class ArticleClient(ServiceClient):

    @service_client('service_name', 'function_name', method='post')
    async def get_blogger_list(self, json=None):
        """ 获取所有博客用户 """
        pass

