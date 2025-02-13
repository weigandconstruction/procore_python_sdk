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

from procore_sdk.models.rest_v10_coordination_issues_coordination_issue_id_assignments_post201_response import RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response

class TestRestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response(unittest.TestCase):
    """RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response:
        """Test RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response`
        """
        model = RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response()
        if include_optional:
            return RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response(
                id = 101,
                coordination_issue_id = 86,
                old_assignee_id = 99,
                new_assignee_id = 199,
                created_by_id = 199,
                created_at = '2019-05-14T14:39:36Z'
            )
        else:
            return RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response(
        )
        """

    def testRestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response(self):
        """Test RestV10CoordinationIssuesCoordinationIssueIdAssignmentsPost201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
