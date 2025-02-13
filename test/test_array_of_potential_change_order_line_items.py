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

from procore_sdk.models.array_of_potential_change_order_line_items import ArrayOfPotentialChangeOrderLineItems

class TestArrayOfPotentialChangeOrderLineItems(unittest.TestCase):
    """ArrayOfPotentialChangeOrderLineItems unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArrayOfPotentialChangeOrderLineItems:
        """Test ArrayOfPotentialChangeOrderLineItems
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArrayOfPotentialChangeOrderLineItems`
        """
        model = ArrayOfPotentialChangeOrderLineItems()
        if include_optional:
            return ArrayOfPotentialChangeOrderLineItems(
                entities = [
                    procore_sdk.models.default.default(
                        id = 4896147, 
                        amount = '1000.0', 
                        company = procore_sdk.models.rest_v10_work_order_contracts_post_201_response_line_items_inner_company.RestV10WorkOrderContractsPost_201_response_line_items_inner_company(
                            id = 163215, 
                            name = 'Procore Tech', ), 
                        cost_code = procore_sdk.models.extended.extended(
                            id = 12345, 
                            biller = 'Campus', 
                            biller_id = 12345, 
                            biller_type = 'Project', 
                            budgeted = False, 
                            code = '300', 
                            created_at = '2015-05-15T00:00Z', 
                            deleted_at = '2017-07-29T21:39:40Z', 
                            full_code = '02-300', 
                            name = 'Earthwork', 
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
                                ], ), 
                        created_at = '2016-08-01T23:33:54Z', 
                        description = 'Cleanup', 
                        extended_type = 'calculated', 
                        holder = procore_sdk.models.rest_v10_work_order_contracts_post_201_response_line_items_inner_holder.RestV10WorkOrderContractsPost_201_response_line_items_inner_holder(
                            id = 233245, 
                            holder_type = 'WorkOrderContract', ), 
                        line_item_type = procore_sdk.models.line_item_type.LineItemType(
                            id = 12345, 
                            name = 'Equipment', 
                            code = 'LB', 
                            base_type = 'materials', 
                            origin_data = 'OD-2398273424', 
                            origin_id = 'ABC123', ), 
                        origin_data = 'OD-39823232', 
                        origin_id = '239233', 
                        position = 1, 
                        project = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_project.RestV10WorkOrderContractsGet_200_response_inner_project(
                            id = 123456, 
                            name = 'Children's Hospital', ), 
                        quantity = '10.0', 
                        tax_code_id = 1, 
                        total_amount = '1000.0', 
                        extended_amount = '900.0', 
                        unit_cost = '100.0', 
                        uom = 'Lbs', 
                        wbs_code = procore_sdk.models.rest_v10_work_order_contracts_post_201_response_line_items_inner_wbs_code.RestV10WorkOrderContractsPost_201_response_line_items_inner_wbs_code(
                            id = 999, 
                            flat_code = '01-011.CT1', 
                            description = 'Project Engineer.Cost Type 1', ), 
                        updated_at = '2016-09-01T21:33:54Z', 
                        change_event_line_item = procore_sdk.models.rest_v10_work_order_contracts_post_201_response_line_items_inner_change_event_line_item.RestV10WorkOrderContractsPost_201_response_line_items_inner_change_event_line_item(
                            id = 5, 
                            cost_rom = '100.0', 
                            revenue_rom = '200.0', 
                            event_id = 6, 
                            currency_configuration = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_currency_configuration.RestV10WorkOrderContractsGet_200_response_inner_currency_configuration(
                                currency_iso_code = 'USD', ), ), 
                        currency_configuration = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_currency_configuration.RestV10WorkOrderContractsGet_200_response_inner_currency_configuration(
                            currency_iso_code = 'USD', ), )
                    ],
                errors = [
                    procore_sdk.models.array_of_potential_change_order_line_items_errors_inner.arrayOfPotentialChangeOrderLineItems_errors_inner()
                    ]
            )
        else:
            return ArrayOfPotentialChangeOrderLineItems(
        )
        """

    def testArrayOfPotentialChangeOrderLineItems(self):
        """Test ArrayOfPotentialChangeOrderLineItems"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
