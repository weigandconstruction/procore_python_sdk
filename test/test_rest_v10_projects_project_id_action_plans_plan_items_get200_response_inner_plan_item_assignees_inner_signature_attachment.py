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

from procore_sdk.models.rest_v10_projects_project_id_action_plans_plan_items_get200_response_inner_plan_item_assignees_inner_signature_attachment import RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerSignatureAttachment

class TestRestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerSignatureAttachment(unittest.TestCase):
    """RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerSignatureAttachment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerSignatureAttachment:
        """Test RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerSignatureAttachment
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerSignatureAttachment`
        """
        model = RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerSignatureAttachment()
        if include_optional:
            return RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerSignatureAttachment(
                id = 23,
                content_type = 'image/png',
                name = 'action_plan_signature_1_2_assignee_53.png',
                url = ''
            )
        else:
            return RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerSignatureAttachment(
        )
        """

    def testRestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerSignatureAttachment(self):
        """Test RestV10ProjectsProjectIdActionPlansPlanItemsGet200ResponseInnerPlanItemAssigneesInnerSignatureAttachment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
