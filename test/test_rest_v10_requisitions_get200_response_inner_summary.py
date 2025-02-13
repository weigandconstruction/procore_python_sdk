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

from procore_sdk.models.rest_v10_requisitions_get200_response_inner_summary import RestV10RequisitionsGet200ResponseInnerSummary

class TestRestV10RequisitionsGet200ResponseInnerSummary(unittest.TestCase):
    """RestV10RequisitionsGet200ResponseInnerSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10RequisitionsGet200ResponseInnerSummary:
        """Test RestV10RequisitionsGet200ResponseInnerSummary
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10RequisitionsGet200ResponseInnerSummary`
        """
        model = RestV10RequisitionsGet200ResponseInnerSummary()
        if include_optional:
            return RestV10RequisitionsGet200ResponseInnerSummary(
                balance_to_finish_including_retainage = '1268346.55',
                completed_work_retainage_percent = '10',
                completed_work_retainage_amount = '1201.0',
                contract_sum_to_date = '1279159.15',
                current_payment_due = '10812.6',
                formatted_period = '01/06/19 - 30/06/19',
                less_previous_certificates_for_payment = '0',
                negative_change_order_item_total = '0',
                negative_new_change_order_item_total = '0',
                negative_previous_change_order_item_total = '0',
                net_change_by_change_orders = '256706.65',
                original_contract_sum = '1022452.5',
                positive_change_order_item_total = '0.00',
                positive_new_change_order_item_total = '0.00',
                positive_previous_change_order_item_total = '0.00',
                stored_materials_retainage_amount = '0.4',
                stored_materials_retainage_percent = '10',
                tax_applicable_to_this_payment = '0',
                total_completed_and_stored_to_date = '1201.4',
                total_earned_less_retainage = '10812.6',
                total_retainage = '1201.4'
            )
        else:
            return RestV10RequisitionsGet200ResponseInnerSummary(
        )
        """

    def testRestV10RequisitionsGet200ResponseInnerSummary(self):
        """Test RestV10RequisitionsGet200ResponseInnerSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
