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

from procore_sdk.api.quality_safety_incidents_actions_api import QualitySafetyIncidentsActionsApi


class TestQualitySafetyIncidentsActionsApi(unittest.TestCase):
    """QualitySafetyIncidentsActionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = QualitySafetyIncidentsActionsApi()

    def tearDown(self) -> None:
        pass

    def test_rest_v10_projects_project_id_incidents_actions_get(self) -> None:
        """Test case for rest_v10_projects_project_id_incidents_actions_get

        List Actions
        """
        pass

    def test_rest_v10_projects_project_id_incidents_actions_id_delete(self) -> None:
        """Test case for rest_v10_projects_project_id_incidents_actions_id_delete

        Destroy Action
        """
        pass

    def test_rest_v10_projects_project_id_incidents_actions_id_get(self) -> None:
        """Test case for rest_v10_projects_project_id_incidents_actions_id_get

        Show Action
        """
        pass

    def test_rest_v10_projects_project_id_incidents_actions_id_patch(self) -> None:
        """Test case for rest_v10_projects_project_id_incidents_actions_id_patch

        Update Action
        """
        pass

    def test_rest_v10_projects_project_id_incidents_actions_post(self) -> None:
        """Test case for rest_v10_projects_project_id_incidents_actions_post

        Create Action
        """
        pass

    def test_rest_v10_projects_project_id_recycle_bin_incidents_actions_get(self) -> None:
        """Test case for rest_v10_projects_project_id_recycle_bin_incidents_actions_get

        List Recycled Actions
        """
        pass

    def test_rest_v10_projects_project_id_recycle_bin_incidents_actions_id_get(self) -> None:
        """Test case for rest_v10_projects_project_id_recycle_bin_incidents_actions_id_get

        Show Recycled Action
        """
        pass

    def test_rest_v10_projects_project_id_recycle_bin_incidents_actions_id_restore_patch(self) -> None:
        """Test case for rest_v10_projects_project_id_recycle_bin_incidents_actions_id_restore_patch

        Retrieve Recycled Action
        """
        pass

    def test_rest_v11_projects_project_id_recycle_bin_incidents_actions_get(self) -> None:
        """Test case for rest_v11_projects_project_id_recycle_bin_incidents_actions_get

        List Recycled Actions
        """
        pass

    def test_rest_v11_projects_project_id_recycle_bin_incidents_actions_id_get(self) -> None:
        """Test case for rest_v11_projects_project_id_recycle_bin_incidents_actions_id_get

        Show Recycled Action
        """
        pass

    def test_rest_v11_projects_project_id_recycle_bin_incidents_actions_id_restore_patch(self) -> None:
        """Test case for rest_v11_projects_project_id_recycle_bin_incidents_actions_id_restore_patch

        Retrieve Recycled Action
        """
        pass


if __name__ == '__main__':
    unittest.main()
