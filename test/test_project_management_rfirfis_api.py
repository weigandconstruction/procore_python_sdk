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

from procore_sdk.api.project_management_rfirfis_api import ProjectManagementRFIRFIsApi


class TestProjectManagementRFIRFIsApi(unittest.TestCase):
    """ProjectManagementRFIRFIsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectManagementRFIRFIsApi()

    def tearDown(self) -> None:
        pass

    def test_rest_v10_projects_project_id_rfis_get(self) -> None:
        """Test case for rest_v10_projects_project_id_rfis_get

        List RFIs
        """
        pass

    def test_rest_v10_projects_project_id_rfis_id_get(self) -> None:
        """Test case for rest_v10_projects_project_id_rfis_id_get

        Show RFI
        """
        pass

    def test_rest_v10_projects_project_id_rfis_id_patch(self) -> None:
        """Test case for rest_v10_projects_project_id_rfis_id_patch

        Update RFI
        """
        pass

    def test_rest_v10_projects_project_id_rfis_id_recycle_patch(self) -> None:
        """Test case for rest_v10_projects_project_id_rfis_id_recycle_patch

        Recycle RFI
        """
        pass

    def test_rest_v10_projects_project_id_rfis_id_retrieve_patch(self) -> None:
        """Test case for rest_v10_projects_project_id_rfis_id_retrieve_patch

        Retrieve Recycled RFI
        """
        pass

    def test_rest_v10_projects_project_id_rfis_idpdf_get(self) -> None:
        """Test case for rest_v10_projects_project_id_rfis_idpdf_get

        Show RFI in PDF format
        """
        pass

    def test_rest_v10_projects_project_id_rfis_patch(self) -> None:
        """Test case for rest_v10_projects_project_id_rfis_patch

        Batch Update RFIs
        """
        pass

    def test_rest_v10_projects_project_id_rfis_post(self) -> None:
        """Test case for rest_v10_projects_project_id_rfis_post

        Create RFI
        """
        pass

    def test_rest_v10_projects_project_id_rfis_recycle_bin_get(self) -> None:
        """Test case for rest_v10_projects_project_id_rfis_recycle_bin_get

        List Recycled RFIs
        """
        pass


if __name__ == '__main__':
    unittest.main()
