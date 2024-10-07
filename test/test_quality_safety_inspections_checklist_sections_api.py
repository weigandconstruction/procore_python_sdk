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

from procore_sdk.api.quality_safety_inspections_checklist_sections_api import QualitySafetyInspectionsChecklistSectionsApi


class TestQualitySafetyInspectionsChecklistSectionsApi(unittest.TestCase):
    """QualitySafetyInspectionsChecklistSectionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = QualitySafetyInspectionsChecklistSectionsApi()

    def tearDown(self) -> None:
        pass

    def test_rest_v10_checklist_lists_list_id_sections_id_delete(self) -> None:
        """Test case for rest_v10_checklist_lists_list_id_sections_id_delete

        Delete Checklist Section
        """
        pass

    def test_rest_v10_checklist_lists_list_id_sections_id_get(self) -> None:
        """Test case for rest_v10_checklist_lists_list_id_sections_id_get

        Show Checklist Section
        """
        pass

    def test_rest_v10_checklist_lists_list_id_sections_id_patch(self) -> None:
        """Test case for rest_v10_checklist_lists_list_id_sections_id_patch

        Update Checklist Section
        """
        pass

    def test_rest_v10_checklist_lists_list_id_sections_post(self) -> None:
        """Test case for rest_v10_checklist_lists_list_id_sections_post

        Create Checklist Section
        """
        pass

    def test_rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_patch(self) -> None:
        """Test case for rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_patch

        Toggle Checklist Section Not Applicable status
        """
        pass

    def test_rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put(self) -> None:
        """Test case for rest_v10_checklist_lists_list_id_sections_section_id_toggle_not_applicable_put

        Toggle Checklist Section Not Applicable status
        """
        pass

    def test_rest_v10_projects_project_id_checklist_list_sections_get(self) -> None:
        """Test case for rest_v10_projects_project_id_checklist_list_sections_get

        List Checklist (Inspection) Sections
        """
        pass

    def test_rest_v11_projects_project_id_recycle_bin_checklist_list_sections_get(self) -> None:
        """Test case for rest_v11_projects_project_id_recycle_bin_checklist_list_sections_get

        List Recycled Checklist (Inspection) Sections
        """
        pass


if __name__ == '__main__':
    unittest.main()
