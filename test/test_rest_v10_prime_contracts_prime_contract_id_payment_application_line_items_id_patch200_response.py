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

from procore_sdk.models.rest_v10_prime_contracts_prime_contract_id_payment_application_line_items_id_patch200_response import RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response

class TestRestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response(unittest.TestCase):
    """RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response:
        """Test RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response`
        """
        model = RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response()
        if include_optional:
            return RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response(
                id = 135135,
                balance_to_finish = '1.00',
                materials_presently_stored = '0.00',
                scheduled_value = '1.00',
                total_completed_and_stored_to_date = '0.00',
                total_completed_and_stored_to_date_percent = '0.0',
                work_completed_from_previous_application = '0.00',
                work_completed_this_period = '0.00',
                description_of_work = 'Install windows',
                item_number = 1,
                cost_code = None,
                wbs_code = procore_sdk.models.wbs_code.Wbs Code(
                    id = 999, 
                    flat_code = '01-011.CT1', 
                    description = 'Project Engineer.Cost Type 1', ),
                scheduled_unit_price = '0.0',
                scheduled_quantity = '0.0',
                total_completed_and_stored_to_date_quantity = '0.0',
                work_completed_this_period_quantity = '0.0',
                work_completed_from_previous_application_quantity = '0.0',
                work_completed_retainage_currently_retained = '0.0',
                work_completed_retainage_from_previous_application = '0.0',
                work_completed_retainage_released_this_period = '0.0',
                work_completed_retainage_retained_this_period = '0.0',
                work_completed_retainage_percent_this_period = '10.0',
                materials_stored_retainage_currently_retained = '0.0',
                materials_stored_retainage_from_previous_application = '0.0',
                materials_stored_retainage_released_this_period = '0.0',
                materials_stored_retainage_retained_this_period = '0.0',
                materials_stored_retainage_percent_this_period = '10.0',
                total_retainage_currently_retained = '0.0',
                total_retainage_from_previous_application = '0.0',
                type = 'payment_application_markup_line_item'
            )
        else:
            return RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response(
        )
        """

    def testRestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response(self):
        """Test RestV10PrimeContractsPrimeContractIdPaymentApplicationLineItemsIdPatch200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
