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

from procore_sdk.models.rest_v10_tax_types_post400_response import RestV10TaxTypesPost400Response

class TestRestV10TaxTypesPost400Response(unittest.TestCase):
    """RestV10TaxTypesPost400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10TaxTypesPost400Response:
        """Test RestV10TaxTypesPost400Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10TaxTypesPost400Response`
        """
        model = RestV10TaxTypesPost400Response()
        if include_optional:
            return RestV10TaxTypesPost400Response(
                errors = procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch_200_response_errors_inner_all_of_errors.RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch_200_response_errors_inner_allOf_errors(
                    field_name = [
                        ''
                        ], )
            )
        else:
            return RestV10TaxTypesPost400Response(
        )
        """

    def testRestV10TaxTypesPost400Response(self):
        """Test RestV10TaxTypesPost400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
