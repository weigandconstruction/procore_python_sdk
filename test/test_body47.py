# coding: utf-8

"""
    Procore Rest API Documentation

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2.0
    Contact: apisupport@procore.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from procore_sdk.models.body47 import Body47

class TestBody47(unittest.TestCase):
    """Body47 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body47:
        """Test Body47
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body47`
        """
        model = Body47()
        if include_optional:
            return Body47(
                change_order_batch = procore_sdk.models.change_order_batch.Change Order Batch()
            )
        else:
            return Body47(
                change_order_batch = procore_sdk.models.change_order_batch.Change Order Batch(),
        )
        """

    def testBody47(self):
        """Test Body47"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
