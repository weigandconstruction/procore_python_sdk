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

from procore_sdk.api.core_settings_personal_settings_api import CoreSettingsPersonalSettingsApi


class TestCoreSettingsPersonalSettingsApi(unittest.TestCase):
    """CoreSettingsPersonalSettingsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CoreSettingsPersonalSettingsApi()

    def tearDown(self) -> None:
        pass

    def test_rest_v10_companies_company_id_settings_my_avatar_get(self) -> None:
        """Test case for rest_v10_companies_company_id_settings_my_avatar_get

        Returns avatar of the current user
        """
        pass

    def test_rest_v10_companies_company_id_settings_my_avatar_put(self) -> None:
        """Test case for rest_v10_companies_company_id_settings_my_avatar_put

        Bulk create/update UI flags
        """
        pass


if __name__ == '__main__':
    unittest.main()
