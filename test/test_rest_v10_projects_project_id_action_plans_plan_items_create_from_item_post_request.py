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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_create_from_item_post_request import RestV10ProjectsProjectIdActionPlansPlanItemsCreateFromItemPostRequest

class TestRestV10ProjectsProjectIdActionPlansPlanItemsCreateFromItemPostRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlanItemsCreateFromItemPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlanItemsCreateFromItemPostRequest:
        """Test RestV10ProjectsProjectIdActionPlansPlanItemsCreateFromItemPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlanItemsCreateFromItemPostRequest`
        """
        model = RestV10ProjectsProjectIdActionPlansPlanItemsCreateFromItemPostRequest()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlanItemsCreateFromItemPostRequest(
                plan_item_id = 4435
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlanItemsCreateFromItemPostRequest(
                plan_item_id = 4435,
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlanItemsCreateFromItemPostRequest(self):
        """Test RestV10ProjectsProjectIdActionPlansPlanItemsCreateFromItemPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
