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

from procore_sdk.models.rest_v11_projects_project_id_direct_costs_post201_response import RestV11ProjectsProjectIdDirectCostsPost201Response

class TestRestV11ProjectsProjectIdDirectCostsPost201Response(unittest.TestCase):
    """RestV11ProjectsProjectIdDirectCostsPost201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdDirectCostsPost201Response:
        """Test RestV11ProjectsProjectIdDirectCostsPost201Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdDirectCostsPost201Response`
        """
        model = RestV11ProjectsProjectIdDirectCostsPost201Response()
        if include_optional:
            return RestV11ProjectsProjectIdDirectCostsPost201Response(
                id = 3,
                attachments = [
                    procore_sdk.models.rest_v10_work_order_contracts_post_201_response_attachments_inner.RestV10WorkOrderContractsPost_201_response_attachments_inner(
                        id = 5324, 
                        url = 'http://www.example.com/', 
                        filename = 'january_receipt_copy.jpg', )
                    ],
                attachments_count = 0,
                company = procore_sdk.models.rest_v10_work_order_contracts_post_201_response_line_items_inner_company.RestV10WorkOrderContractsPost_201_response_line_items_inner_company(
                    id = 163215, 
                    name = 'Procore Tech', ),
                created_at = '2012-10-23T21:39:40Z',
                deleted_at = '2017-07-29T21:39:40Z',
                description = 'Home Depot Purchase',
                direct_cost_type = 'invoice',
                employee = procore_sdk.models.rest_v11_projects_project_id_direct_costs_get_200_response_inner_employee.RestV11ProjectsProjectIdDirectCostsGet_200_response_inner_employee(
                    id = 5, 
                    name = 'Bob the Builder', ),
                invoice_number = 'ab-3456',
                direct_cost_date = 'Thu Oct 16 00:00:00 UTC 2014',
                origin_data = 'OD-2398273424',
                origin_id = 'px-1990',
                grand_total = '0.0',
                line_items_count = 0,
                payment_date = 'Tue Dec 16 00:00:00 UTC 2014',
                project = procore_sdk.models.rest_v10_work_order_contracts_get_200_response_inner_project.RestV10WorkOrderContractsGet_200_response_inner_project(
                    id = 123456, 
                    name = 'Children's Hospital', ),
                received_date = 'Sun Nov 16 00:00:00 UTC 2014',
                status = 'pending',
                terms = 'Net 30',
                updated_at = '2012-10-24T21:39:40Z',
                vendor = procore_sdk.models.rest_v11_projects_project_id_direct_costs_post_201_response_vendor.RestV11ProjectsProjectIdDirectCostsPost_201_response_vendor(
                    id = 8, 
                    name = 'Steve's Plumbing and Hardware', ),
                vendor_id = 1,
                vendor_name = 'Steves Plumbing and Hardware',
                currency_configuration = procore_sdk.models.rest_v10_payment_applications_get_200_response_inner_all_of_currency_configuration.RestV10PaymentApplicationsGet_200_response_inner_allOf_currency_configuration(
                    currency_iso_code = 'USD', 
                    currency_exchange_rate = '2.1', 
                    base_currency_iso_code = 'USD', ),
                line_items = [
                    procore_sdk.models.direct_cost_line_item.Direct Cost Line Item(
                        id = 4896147, 
                        amount = '1000.0', 
                        company = procore_sdk.models.rest_v10_work_order_contracts_post_201_response_line_items_inner_company.RestV10WorkOrderContractsPost_201_response_line_items_inner_company(
                            id = 163215, 
                            name = 'Procore Tech', ), 
                        cost_code = null, 
                        created_at = '2016-08-01T23:33:54Z', 
                        currency_configuration = procore_sdk.models.direct_cost_line_item_1_currency_configuration.Direct_Cost_Line_Item_1_currency_configuration(
                            currency_iso_code = 'USD', 
                            base_currency_iso_code = 'EUR', 
                            currency_exchange_rate = '1.2', ), 
                        description = 'Cleanup', 
                        extended_type = 'calculated', 
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
                        quantity = '10.0', 
                        tax_code_id = 1, 
                        total_amount = '1000.0', 
                        extended_amount = '900.0', 
                        unit_cost = '100.0', 
                        uom = 'Lbs', 
                        updated_at = '2016-09-01T21:33:54Z', 
                        wbs_code = procore_sdk.models.rest_v10_work_order_contracts_post_201_response_line_items_inner_wbs_code.RestV10WorkOrderContractsPost_201_response_line_items_inner_wbs_code(
                            id = 999, 
                            flat_code = '01-011.CT1', 
                            description = 'Project Engineer.Cost Type 1', ), 
                        ref = 'PQRS5678', )
                    ]
            )
        else:
            return RestV11ProjectsProjectIdDirectCostsPost201Response(
        )
        """

    def testRestV11ProjectsProjectIdDirectCostsPost201Response(self):
        """Test RestV11ProjectsProjectIdDirectCostsPost201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
