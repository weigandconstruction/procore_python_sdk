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

from procore_sdk.models.standard_cost_code_sync_body import StandardCostCodeSyncBody

class TestStandardCostCodeSyncBody(unittest.TestCase):
    """StandardCostCodeSyncBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> StandardCostCodeSyncBody:
        """Test StandardCostCodeSyncBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `StandardCostCodeSyncBody`
        """
        model = StandardCostCodeSyncBody()
        if include_optional:
            return StandardCostCodeSyncBody(
                company_id = 12345,
                standard_cost_code_list_id = 23456,
                updates = [
                    procore_sdk.models.standard_cost_code_sync_body_updates_inner.Standard_Cost_Code_Sync_Body_updates_inner(
                        name = 'General Requirements', 
                        id = 123, 
                        code = '2-075', 
                        parent_id = 456, 
                        origin_id = 'OID-123', 
                        origin_data = 'OD-234', )
                    ]
            )
        else:
            return StandardCostCodeSyncBody(
                company_id = 12345,
                standard_cost_code_list_id = 23456,
                updates = [
                    procore_sdk.models.standard_cost_code_sync_body_updates_inner.Standard_Cost_Code_Sync_Body_updates_inner(
                        name = 'General Requirements', 
                        id = 123, 
                        code = '2-075', 
                        parent_id = 456, 
                        origin_id = 'OID-123', 
                        origin_data = 'OD-234', )
                    ],
        )
        """

    def testStandardCostCodeSyncBody(self):
        """Test StandardCostCodeSyncBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
