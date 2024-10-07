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

from procore_sdk.api.project_management_rfi_potential_assignees_api import ProjectManagementRFIPotentialAssigneesApi


class TestProjectManagementRFIPotentialAssigneesApi(unittest.TestCase):
    """ProjectManagementRFIPotentialAssigneesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectManagementRFIPotentialAssigneesApi()

    def tearDown(self) -> None:
        pass

    def test_rest_v10_projects_project_id_rfis_potential_assignees_get(self) -> None:
        """Test case for rest_v10_projects_project_id_rfis_potential_assignees_get

        Get a list of possible assignees for an RFI
        """
        pass


if __name__ == '__main__':
    unittest.main()
