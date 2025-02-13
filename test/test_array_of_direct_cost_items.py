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

from procore_sdk.models.array_of_direct_cost_items import ArrayOfDirectCostItems

class TestArrayOfDirectCostItems(unittest.TestCase):
    """ArrayOfDirectCostItems unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArrayOfDirectCostItems:
        """Test ArrayOfDirectCostItems
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArrayOfDirectCostItems`
        """
        model = ArrayOfDirectCostItems()
        if include_optional:
            return ArrayOfDirectCostItems(
                entities = [
                    procore_sdk.models.rest_v10_projects_project_id_direct_costs_post_201_response.RestV10ProjectsProjectIdDirectCostsPost_201_response(
                        id = 3, 
                        attachments = [
                            procore_sdk.models.rest_v10_work_order_contracts_post_201_response_attachments_inner.RestV10WorkOrderContractsPost_201_response_attachments_inner(
                                id = 5324, 
                                url = 'http://www.example.com/', 
                                filename = 'january_receipt_copy.jpg', )
                            ], 
                        attachments_count = 0, 
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
                        received_date = 'Sun Nov 16 00:00:00 UTC 2014', 
                        status = 'pending', 
                        terms = 'Net 30', 
                        updated_at = '2012-10-24T21:39:40Z', 
                        vendor = procore_sdk.models.rest_v11_projects_project_id_direct_costs_post_201_response_vendor.RestV11ProjectsProjectIdDirectCostsPost_201_response_vendor(
                            id = 8, 
                            name = 'Steve's Plumbing and Hardware', ), 
                        vendor_id = 1, 
                        vendor_name = 'Steve's Plumbing and Hardware', 
                        currency_configuration = procore_sdk.models.rest_v10_payment_applications_id_get_200_response_all_of_g703_inner_currency_configuration.RestV10PaymentApplicationsIdGet_200_response_allOf_g703_inner_currency_configuration(
                            currency_iso_code = 'USD', ), )
                    ],
                errors = [
                    procore_sdk.models.array_of_direct_cost_items_errors_inner.arrayOfDirectCostItems_errors_inner()
                    ]
            )
        else:
            return ArrayOfDirectCostItems(
        )
        """

    def testArrayOfDirectCostItems(self):
        """Test ArrayOfDirectCostItems"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
