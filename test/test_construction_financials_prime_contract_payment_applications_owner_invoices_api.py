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

from procore_sdk.api.construction_financials_prime_contract_payment_applications_owner_invoices_api import ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi


class TestConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi(unittest.TestCase):
    """ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ConstructionFinancialsPrimeContractPaymentApplicationsOwnerInvoicesApi()

    def tearDown(self) -> None:
        pass

    def test_rest_v10_payment_applications_get(self) -> None:
        """Test case for rest_v10_payment_applications_get

        List Payment Applications (Owner Invoices) for a Project
        """
        pass

    def test_rest_v10_payment_applications_id_delete(self) -> None:
        """Test case for rest_v10_payment_applications_id_delete

        Delete a Payment Application (Owner Invoice)
        """
        pass

    def test_rest_v10_payment_applications_id_get(self) -> None:
        """Test case for rest_v10_payment_applications_id_get

        Show Payment Application (Owner Invoice)
        """
        pass

    def test_rest_v10_prime_contracts_prime_contract_id_payment_applications_get(self) -> None:
        """Test case for rest_v10_prime_contracts_prime_contract_id_payment_applications_get

        List Payment Applications (Owner Invoices) for Prime Contract
        """
        pass

    def test_rest_v10_prime_contracts_prime_contract_id_payment_applications_id_patch(self) -> None:
        """Test case for rest_v10_prime_contracts_prime_contract_id_payment_applications_id_patch

        Update Payment Application (Owner Invoice) for Prime Contract
        """
        pass

    def test_rest_v10_prime_contracts_prime_contract_id_payment_applications_post(self) -> None:
        """Test case for rest_v10_prime_contracts_prime_contract_id_payment_applications_post

        Create Payment Application (Owner Invoice) for Prime Contract
        """
        pass


if __name__ == '__main__':
    unittest.main()
