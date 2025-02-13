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

from procore_sdk.models.rest_v10_projects_project_id_direct_costs_line_items_get200_response_inner import RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner

class TestRestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner(unittest.TestCase):
    """RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner:
        """Test RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner`
        """
        model = RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner()
        if include_optional:
            return RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner(
                id = 4896147,
                amount = '1000.0',
                cost_code = procore_sdk.models.rest_v10_projects_project_id_direct_costs_line_items_get_200_response_inner_cost_code.RestV10ProjectsProjectIdDirectCostsLineItemsGet_200_response_inner_cost_code(
                    id = 12345, 
                    full_code = '02-300', 
                    name = 'Earthwork', 
                    origin_id = '9874484', ),
                created_at = '2016-08-01T23:33:54Z',
                description = 'Cleanup',
                extended_amount = '900.0',
                extended_type = 'calculated',
                holder = procore_sdk.models.array_of_potential_change_order_line_items_errors_inner_all_of_holder.arrayOfPotentialChangeOrderLineItems_errors_inner_allOf_holder(
                    id = 233245, 
                    holder_type = 'DirectCost::Item', ),
                line_item_type = procore_sdk.models.rest_v10_projects_project_id_direct_costs_line_items_get_200_response_inner_line_item_type.RestV10ProjectsProjectIdDirectCostsLineItemsGet_200_response_inner_line_item_type(
                    id = 12345, 
                    base_type = 'materials', 
                    code = 'LB', 
                    name = 'Equipment', 
                    origin_data = 'OD-2398273424', 
                    origin_id = 'ABC123', ),
                origin_id = '239233',
                position = 1,
                project = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_project.RestV10WorkOrderContractsGet_200_response_inner_project(
                    id = 123456, 
                    name = 'Children's Hospital', ),
                quantity = '10.0',
                total_amount = '1000.0',
                unit_cost = '100.0',
                uom = 'Lbs',
                updated_at = '2016-09-01T21:33:54Z',
                wbs_code = procore_sdk.models.rest_v10_work_order_contracts_post_201_response_line_items_inner_wbs_code.RestV10WorkOrderContractsPost_201_response_line_items_inner_wbs_code(
                    id = 999, 
                    flat_code = '01-011.CT1', 
                    description = 'Project Engineer.Cost Type 1', ),
                currency_configuration = procore_sdk.models.rest_v10_projects_project_id_direct_costs_line_items_get_200_response_inner_currency_configuration.RestV10ProjectsProjectIdDirectCostsLineItemsGet_200_response_inner_currency_configuration(
                    currency_iso_code = 'USD', )
            )
        else:
            return RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner(
        )
        """

    def testRestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner(self):
        """Test RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
