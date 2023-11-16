import shopify

class Shopify_Read():

	def __init__(self):
        self.SHOP_HANDLE = 'a617df'
        self.ADMIN_API_KEY = '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'
        self.API_KEY = '7e6c5a6f718778c867edb2bf84a70336'
        self.API_SECRET_KEY = '51ed89ff8b57ce51dbe709b7dac8457d'
        self.PASSWORD = 'It07Shop'
        self.API_VERSION = '2022-07'


    def setupShopifySessionUsingApiKeyPassword(self):
        shop_url = "https://{}.myshopify.com/admin/api/{}".format(self.SHOP_HANDLE, self.API_VERSION)
        shopify.ShopifyResource.set_site(shop_url)
        shopify.ShopifyResource.set_user(self.API_KEY)
        shopify.ShopifyResource.set_password(self.ADMIN_API_KEY)

    def readFromShopify(self, resource_type, **kwargs):
        self.setupShopifySessionUsingApiKeyPassword()

        resource_count = resource_type.count(**kwargs)
        resources = []
        if resource_count > 0:
            page = resource_type.find(**kwargs)
            resources.extend(page)
            while page.has_next_page():
                page = page.next_page()
                resources.extend(page)
        return resources

