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

from procore_sdk.api.core_company_directory_company_inactive_users_api import CoreCompanyDirectoryCompanyInactiveUsersApi


class TestCoreCompanyDirectoryCompanyInactiveUsersApi(unittest.TestCase):
    """CoreCompanyDirectoryCompanyInactiveUsersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CoreCompanyDirectoryCompanyInactiveUsersApi()

    def tearDown(self) -> None:
        pass

    def test_rest_v10_companies_company_id_users_inactive_get(self) -> None:
        """Test case for rest_v10_companies_company_id_users_inactive_get

        List company inactive users
        """
        pass

    def test_rest_v10_companies_company_id_users_inactive_id_patch(self) -> None:
        """Test case for rest_v10_companies_company_id_users_inactive_id_patch

        Reactivate company user
        """
        pass


if __name__ == '__main__':
    unittest.main()
