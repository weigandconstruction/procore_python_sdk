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

from procore_sdk.api.quality_safety_forms_form_templates_api import QualitySafetyFormsFormTemplatesApi


class TestQualitySafetyFormsFormTemplatesApi(unittest.TestCase):
    """QualitySafetyFormsFormTemplatesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = QualitySafetyFormsFormTemplatesApi()

    def tearDown(self) -> None:
        pass

    def test_rest_v10_companies_company_id_form_templates_get(self) -> None:
        """Test case for rest_v10_companies_company_id_form_templates_get

        List Company Form Templates
        """
        pass

    def test_rest_v10_companies_company_id_form_templates_id_delete(self) -> None:
        """Test case for rest_v10_companies_company_id_form_templates_id_delete

        Delete Company Form Template
        """
        pass

    def test_rest_v10_companies_company_id_form_templates_id_get(self) -> None:
        """Test case for rest_v10_companies_company_id_form_templates_id_get

        Show Company Form Template
        """
        pass

    def test_rest_v10_companies_company_id_form_templates_id_patch(self) -> None:
        """Test case for rest_v10_companies_company_id_form_templates_id_patch

        Update Company Form Template
        """
        pass

    def test_rest_v10_companies_company_id_form_templates_post(self) -> None:
        """Test case for rest_v10_companies_company_id_form_templates_post

        Create Company Form Template
        """
        pass

    def test_rest_v10_companies_company_id_recycle_bin_form_templates_get(self) -> None:
        """Test case for rest_v10_companies_company_id_recycle_bin_form_templates_get

        List Recycled Company Form Templates
        """
        pass

    def test_rest_v10_companies_company_id_recycle_bin_form_templates_id_get(self) -> None:
        """Test case for rest_v10_companies_company_id_recycle_bin_form_templates_id_get

        Show Recycled Company Form Template
        """
        pass

    def test_rest_v10_companies_company_id_recycle_bin_form_templates_id_restore_patch(self) -> None:
        """Test case for rest_v10_companies_company_id_recycle_bin_form_templates_id_restore_patch

        Restore Company Form Template
        """
        pass

    def test_rest_v10_projects_project_id_form_templates_get(self) -> None:
        """Test case for rest_v10_projects_project_id_form_templates_get

        List Company Form Templates from Project
        """
        pass

    def test_rest_v10_projects_project_id_form_templates_id_get(self) -> None:
        """Test case for rest_v10_projects_project_id_form_templates_id_get

        Show Company Form Template from Project
        """
        pass


if __name__ == '__main__':
    unittest.main()
