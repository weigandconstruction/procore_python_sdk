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

from procore_sdk.models.rest_v10_change_order_packages_post201_response_line_items_inner_cost_code import RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerCostCode

class TestRestV10ChangeOrderPackagesPost201ResponseLineItemsInnerCostCode(unittest.TestCase):
    """RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerCostCode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerCostCode:
        """Test RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerCostCode
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerCostCode`
        """
        model = RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerCostCode()
        if include_optional:
            return RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerCostCode(
                id = 12345,
                biller = 'Campus',
                biller_id = 12345,
                biller_type = 'Project',
                biller_origin_id = '98765',
                budgeted = False,
                code = '300',
                created_at = '2015-05-15T00:00Z',
                deleted_at = '2017-07-29T21:39:40Z',
                full_code = '02-300',
                name = 'Earthwork',
                origin_data = 'OD-129947',
                origin_id = '9874484',
                parent = procore_sdk.models.extended_1_parent.extended_1_parent(
                    id = 2345, ),
                position = 1,
                sortable_code = '02-300',
                standard_cost_code_id = 122334,
                updated_at = '2015-05-15T00:00Z',
                line_item_types = [
                    procore_sdk.models.line_item_type.LineItemType(
                        id = 12345, 
                        name = 'Equipment', 
                        code = 'LB', 
                        base_type = 'materials', 
                        origin_data = 'OD-2398273424', 
                        origin_id = 'ABC123', )
                    ]
            )
        else:
            return RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerCostCode(
        )
        """

    def testRestV10ChangeOrderPackagesPost201ResponseLineItemsInnerCostCode(self):
        """Test RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerCostCode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
