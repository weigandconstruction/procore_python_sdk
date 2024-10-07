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

from procore_sdk.models.array_of_cost_codes_errors_inner import ArrayOfCostCodesErrorsInner

class TestArrayOfCostCodesErrorsInner(unittest.TestCase):
    """ArrayOfCostCodesErrorsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArrayOfCostCodesErrorsInner:
        """Test ArrayOfCostCodesErrorsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArrayOfCostCodesErrorsInner`
        """
        model = ArrayOfCostCodesErrorsInner()
        if include_optional:
            return ArrayOfCostCodesErrorsInner(
                id = 12345,
                full_code = '02-300',
                name = 'Earthwork',
                biller = 'Campus',
                biller_id = 12345,
                biller_type = 'Project',
                budgeted = False,
                code = '300',
                created_at = '2015-05-15T00:00Z',
                deleted_at = '2017-07-29T21:39:40Z',
                origin_data = 'OD-129947',
                origin_id = '9874484',
                parent = procore_sdk.models.extended_parent.extended_parent(
                    id = 2345, ),
                position = 1,
                sortable_code = '02-300',
                standard_cost_code_id = 122334,
                standard_cost_code_list_id = 133445,
                updated_at = '2015-05-15T00:00Z',
                line_item_types = [
                    procore_sdk.models.line_item_type.LineItemType(
                        id = 12345, 
                        name = 'Equipment', 
                        code = 'LB', 
                        base_type = 'materials', 
                        origin_data = 'OD-2398273424', 
                        origin_id = 'ABC123', )
                    ],
                errors = procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_items_sync_patch_200_response_errors_inner_all_of_errors.RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch_200_response_errors_inner_allOf_errors(
                    field_name = [
                        ''
                        ], )
            )
        else:
            return ArrayOfCostCodesErrorsInner(
        )
        """

    def testArrayOfCostCodesErrorsInner(self):
        """Test ArrayOfCostCodesErrorsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
