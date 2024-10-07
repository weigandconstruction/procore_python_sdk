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

from procore_sdk.models.rest_v10_coordination_issue_activities_feed_get200_response_inner import RestV10CoordinationIssueActivitiesFeedGet200ResponseInner

class TestRestV10CoordinationIssueActivitiesFeedGet200ResponseInner(unittest.TestCase):
    """RestV10CoordinationIssueActivitiesFeedGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CoordinationIssueActivitiesFeedGet200ResponseInner:
        """Test RestV10CoordinationIssueActivitiesFeedGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CoordinationIssueActivitiesFeedGet200ResponseInner`
        """
        model = RestV10CoordinationIssueActivitiesFeedGet200ResponseInner()
        if include_optional:
            return RestV10CoordinationIssueActivitiesFeedGet200ResponseInner(
                id = 101,
                coordination_issue_id = 86,
                type = 'status_change',
                details = procore_sdk.models.rest_v10_coordination_issues_id_status_changes_get_200_response_inner.RestV10CoordinationIssuesIdStatusChangesGet_200_response_inner(
                    id = 101, 
                    coordination_issue_id = 123, 
                    old_status = 'open', 
                    new_status = 'closed', 
                    created_by_id = 577, 
                    created_by = null, 
                    linked_rfi = null, 
                    linked_observation_item = procore_sdk.models.rest_v10_coordination_issues_get_200_response_inner_all_of_linked_observation_items_inner.RestV10CoordinationIssuesGet_200_response_inner_allOf_linked_observation_items_inner(
                        id = 93, 
                        number = '113', 
                        personal = True, 
                        title = '#113 - Duct and Structural Conflict', 
                        url = 'http://app.procore.com/3664/project/observations/items/7142', 
                        created_by_id = 47531, ), 
                    created_at = '2018-05-08T13:21:20Z', ),
                created_at = '2018-04-19T09:36:42Z',
                updated_at = '2018-04-19T09:36:42Z'
            )
        else:
            return RestV10CoordinationIssueActivitiesFeedGet200ResponseInner(
        )
        """

    def testRestV10CoordinationIssueActivitiesFeedGet200ResponseInner(self):
        """Test RestV10CoordinationIssueActivitiesFeedGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
