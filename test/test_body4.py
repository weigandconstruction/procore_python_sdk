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

from procore_sdk.models.body4 import Body4

class TestBody4(unittest.TestCase):
    """Body4 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body4:
        """Test Body4
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body4`
        """
        model = Body4()
        if include_optional:
            return Body4(
                project_id = 34567,
                contract_detail_line_item = procore_sdk.models.body_4_contract_detail_line_item.Body_4_contract_detail_line_item(
                    line_item_id = 1, 
                    amount = '1000.0', 
                    description = 'Cleanup', )
            )
        else:
            return Body4(
                project_id = 34567,
                contract_detail_line_item = procore_sdk.models.body_4_contract_detail_line_item.Body_4_contract_detail_line_item(
                    line_item_id = 1, 
                    amount = '1000.0', 
                    description = 'Cleanup', ),
        )
        """

    def testBody4(self):
        """Test Body4"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
