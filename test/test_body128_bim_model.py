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

from procore_sdk.models.body128_bim_model import Body128BimModel

class TestBody128BimModel(unittest.TestCase):
    """Body128BimModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body128BimModel:
        """Test Body128BimModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body128BimModel`
        """
        model = Body128BimModel()
        if include_optional:
            return Body128BimModel(
                title = 'Combined Model',
                auto_publish = False
            )
        else:
            return Body128BimModel(
                title = 'Combined Model',
        )
        """

    def testBody128BimModel(self):
        """Test Body128BimModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
