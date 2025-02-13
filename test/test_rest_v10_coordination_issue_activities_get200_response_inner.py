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

from procore_sdk.models.rest_v10_coordination_issue_activities_get200_response_inner import RestV10CoordinationIssueActivitiesGet200ResponseInner

class TestRestV10CoordinationIssueActivitiesGet200ResponseInner(unittest.TestCase):
    """RestV10CoordinationIssueActivitiesGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CoordinationIssueActivitiesGet200ResponseInner:
        """Test RestV10CoordinationIssueActivitiesGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CoordinationIssueActivitiesGet200ResponseInner`
        """
        model = RestV10CoordinationIssueActivitiesGet200ResponseInner()
        if include_optional:
            return RestV10CoordinationIssueActivitiesGet200ResponseInner(
                id = 101,
                coordination_issue_id = 86,
                type = 'comment',
                created_at = '2018-04-19T09:36:42Z',
                updated_at = '2018-04-19T09:36:42Z'
            )
        else:
            return RestV10CoordinationIssueActivitiesGet200ResponseInner(
        )
        """

    def testRestV10CoordinationIssueActivitiesGet200ResponseInner(self):
        """Test RestV10CoordinationIssueActivitiesGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
