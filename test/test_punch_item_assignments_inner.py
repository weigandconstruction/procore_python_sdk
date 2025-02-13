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

from procore_sdk.models.punch_item_assignments_inner import PunchItemAssignmentsInner

class TestPunchItemAssignmentsInner(unittest.TestCase):
    """PunchItemAssignmentsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PunchItemAssignmentsInner:
        """Test PunchItemAssignmentsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PunchItemAssignmentsInner`
        """
        model = PunchItemAssignmentsInner()
        if include_optional:
            return PunchItemAssignmentsInner(
                id = 333675,
                approved = True,
                comment = 'Completed',
                login_information_id = 420,
                login_information_name = 'Edgar Admin',
                login_information = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                attachments = [
                    procore_sdk.models.rest_v10_work_order_contracts_post_201_response_attachments_inner.RestV10WorkOrderContractsPost_201_response_attachments_inner(
                        id = 5324, 
                        url = 'http://www.example.com/', 
                        filename = 'january_receipt_copy.jpg', )
                    ],
                vendor = procore_sdk.models.compact.Compact(
                    id = 161072, 
                    name = 'SID Architecture', ),
                notified_at = '2018-06-25T22:22:42Z',
                responded_at = '2018-06-25T22:22:42Z',
                status = 'unresolved',
                manager_accepted_at = '2018-10-26T18:15:26Z',
                user_name = 'Edgar Admin',
                updated_at = '2018-10-26T18:15:26Z'
            )
        else:
            return PunchItemAssignmentsInner(
        )
        """

    def testPunchItemAssignmentsInner(self):
        """Test PunchItemAssignmentsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
