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

from procore_sdk.api.quality_safety_action_plans_action_plan_items_api import QualitySafetyActionPlansActionPlanItemsApi


class TestQualitySafetyActionPlansActionPlanItemsApi(unittest.TestCase):
    """QualitySafetyActionPlansActionPlanItemsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = QualitySafetyActionPlansActionPlanItemsApi()

    def tearDown(self) -> None:
        pass

    def test_rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch(self) -> None:
        """Test case for rest_v10_projects_project_id_action_plans_plan_items_bulk_update_patch

        Bulk Update Action Plan Item
        """
        pass

    def test_rest_v10_projects_project_id_action_plans_plan_items_create_from_item_post(self) -> None:
        """Test case for rest_v10_projects_project_id_action_plans_plan_items_create_from_item_post

        Create a copy of the Action Plan Item in the Item's Section.
        """
        pass

    def test_rest_v10_projects_project_id_action_plans_plan_items_get(self) -> None:
        """Test case for rest_v10_projects_project_id_action_plans_plan_items_get

        List Action Plan Items
        """
        pass

    def test_rest_v10_projects_project_id_action_plans_plan_items_id_delete(self) -> None:
        """Test case for rest_v10_projects_project_id_action_plans_plan_items_id_delete

        Delete Action Plan Item
        """
        pass

    def test_rest_v10_projects_project_id_action_plans_plan_items_id_get(self) -> None:
        """Test case for rest_v10_projects_project_id_action_plans_plan_items_id_get

        Show Action Plan Item
        """
        pass

    def test_rest_v10_projects_project_id_action_plans_plan_items_id_move_post(self) -> None:
        """Test case for rest_v10_projects_project_id_action_plans_plan_items_id_move_post

        Move Action Plan Item within or across Sections
        """
        pass

    def test_rest_v10_projects_project_id_action_plans_plan_items_id_patch(self) -> None:
        """Test case for rest_v10_projects_project_id_action_plans_plan_items_id_patch

        Update Action Plan Item
        """
        pass

    def test_rest_v10_projects_project_id_action_plans_plan_items_post(self) -> None:
        """Test case for rest_v10_projects_project_id_action_plans_plan_items_post

        Create Action Plan Item
        """
        pass

    def test_rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_get(self) -> None:
        """Test case for rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_get

        List Recycled Action Plan Items
        """
        pass

    def test_rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_id_get(self) -> None:
        """Test case for rest_v10_projects_project_id_recycle_bin_action_plans_plan_items_id_get

        Show Recycled Action Plan Item
        """
        pass


if __name__ == '__main__':
    unittest.main()
