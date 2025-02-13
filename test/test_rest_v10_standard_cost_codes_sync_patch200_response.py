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

from procore_sdk.models.rest_v10_standard_cost_codes_sync_patch200_response import RestV10StandardCostCodesSyncPatch200Response

class TestRestV10StandardCostCodesSyncPatch200Response(unittest.TestCase):
    """RestV10StandardCostCodesSyncPatch200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10StandardCostCodesSyncPatch200Response:
        """Test RestV10StandardCostCodesSyncPatch200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10StandardCostCodesSyncPatch200Response`
        """
        model = RestV10StandardCostCodesSyncPatch200Response()
        if include_optional:
            return RestV10StandardCostCodesSyncPatch200Response(
                entities = [
                    procore_sdk.models.standard_cost_code.Standard Cost Code(
                        id = 12345, 
                        standard_cost_code_list_id = 12345, 
                        parent_id = 12345, 
                        code = '300', 
                        full_code = '02-300', 
                        name = 'Site Work', 
                        origin_data = 'OD-2398273424', 
                        origin_id = 'ABC123', )
                    ],
                errors = [{"id":3,"name":"General Requirements","errors":{"id":["Entity with this ID not found"]}}]
            )
        else:
            return RestV10StandardCostCodesSyncPatch200Response(
        )
        """

    def testRestV10StandardCostCodesSyncPatch200Response(self):
        """Test RestV10StandardCostCodesSyncPatch200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
