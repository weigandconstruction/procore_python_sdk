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

from procore_sdk.models.coordination_issue_assignment_activity_details import CoordinationIssueAssignmentActivityDetails

class TestCoordinationIssueAssignmentActivityDetails(unittest.TestCase):
    """CoordinationIssueAssignmentActivityDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CoordinationIssueAssignmentActivityDetails:
        """Test CoordinationIssueAssignmentActivityDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CoordinationIssueAssignmentActivityDetails`
        """
        model = CoordinationIssueAssignmentActivityDetails()
        if include_optional:
            return CoordinationIssueAssignmentActivityDetails(
                id = 1,
                old_assignee = procore_sdk.models.coordination_issue_assignment_activity_details_old_assignee.Coordination_Issue_Assignment_Activity_Details_old_assignee(
                    id = 161072, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                new_assignee = procore_sdk.models.coordination_issue_assignment_activity_details_new_assignee.Coordination_Issue_Assignment_Activity_Details_new_assignee(
                    id = 161074, 
                    login = 'carl.contractor@example.com', 
                    name = 'Peter Plumber', ),
                comment = procore_sdk.models.comment.Comment(
                    id = 1, 
                    body = 'This is a photo of a cat', 
                    creator = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                        id = 160586, 
                        login = 'carl.contractor@example.com', 
                        name = 'Carl Contractor', ), 
                    created_at = '2013-11-08T00:00Z', 
                    updated_at = '2013-11-08T00:00Z', ),
                created_by = procore_sdk.models.coordination_issue_assignment_activity_details_created_by.Coordination_Issue_Assignment_Activity_Details_created_by(
                    id = 161076, 
                    login = 'carl.contractor@example.com', 
                    name = 'Bill Bim Manager', )
            )
        else:
            return CoordinationIssueAssignmentActivityDetails(
        )
        """

    def testCoordinationIssueAssignmentActivityDetails(self):
        """Test CoordinationIssueAssignmentActivityDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
