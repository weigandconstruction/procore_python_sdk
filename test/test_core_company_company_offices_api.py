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

from procore_sdk.api.core_company_company_offices_api import CoreCompanyCompanyOfficesApi


class TestCoreCompanyCompanyOfficesApi(unittest.TestCase):
    """CoreCompanyCompanyOfficesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CoreCompanyCompanyOfficesApi()

    def tearDown(self) -> None:
        pass

    def test_rest_v10_offices_get(self) -> None:
        """Test case for rest_v10_offices_get

        List company offices
        """
        pass

    def test_rest_v10_offices_id_delete(self) -> None:
        """Test case for rest_v10_offices_id_delete

        Delete a company office
        """
        pass

    def test_rest_v10_offices_id_get(self) -> None:
        """Test case for rest_v10_offices_id_get

        Show company office
        """
        pass

    def test_rest_v10_offices_id_patch(self) -> None:
        """Test case for rest_v10_offices_id_patch

        Update company office
        """
        pass

    def test_rest_v10_offices_post(self) -> None:
        """Test case for rest_v10_offices_post

        Create company office
        """
        pass


if __name__ == '__main__':
    unittest.main()
