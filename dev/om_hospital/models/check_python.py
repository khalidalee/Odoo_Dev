from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


import re
import shopify
# from testPython import testPython
# from shopify_read.py import Shopify_Read as shRead
# from . import Shopify_Read as shRead
# from om_hospital.common.util.shopify.shopify_read.py import Shopify_Read

class HospitalCheckPython(models.Model):
    _name = "hospital.check_python"
    output = fields.Text(String='Name')

    SHOP_HANDLE = 'a617df'
    ADMIN_API_KEY = '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'
    API_KEY = '7e6c5a6f718778c867edb2bf84a70336'
    API_SECRET_KEY = '51ed89ff8b57ce51dbe709b7dac8457d'
    PASSWORD = 'It07Shop'
    API_VERSION = '2022-07'

    def check_code(self):
        self.output = "Python code executed"

    def send_email(self):
        self.output = "Email Sent!"

    # def read_resources(self):
    #     self.output = "Python code executed"

    def setupShopifySessionUsingApiKeyPassword(self):
        shop_url = "https://{}.myshopify.com/admin/api/{}".format(self.SHOP_HANDLE, self.API_VERSION)
        shopify.ShopifyResource.set_site(shop_url)
        shopify.ShopifyResource.set_user(self.API_KEY)
        shopify.ShopifyResource.set_password(self.ADMIN_API_KEY)

    def readFromShopify(self, resource_type, **kwargs):
        resource_count = resource_type.count(**kwargs)
        resources = []
        if resource_count > 0:
            page=resource_type.find(**kwargs)
            resources.extend(page)
            while page.has_next_page():
                page = page.next_page()
                resources.extend(page)
        return resources

    def getShopifyData(self):
        # items = Shopify_Read.readFromShopify(shopify.Product)
        self.output = ""
        self.setupShopifySessionUsingApiKeyPassword()
        tmp_text = ""
        items = self.readFromShopify(shopify.Customer)
        # for item in self.readFromShopify(shopify.Product):
        for item in items:
            d = item.to_dict()
            for key in d:
                tmp_text += '<p>{} : {}</p>'.format(key, d[key])

            # print(tmp_text)
            self.output = "{} <p><hr><p> {}".format(self.output, tmp_text)

        print(tmp_text)

    def testExternalPythonFile(self):
        t = testPython()
        t.printText()
        return None

    def oepn_email_marketing_mailing(self):
        self.output = "Opening Email Marketing 'Mailing' Interface!"
        return {
            'name': ('Send Email from Hospital Module'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'mailing.mailing',
            # 'res_model': 'mailing.list',
            'view_id': False,
            'type': 'ir.actions.act_window',
            # 'flags': {'initial_mode': 'edit'},
            # 'target': 'current'
        }
