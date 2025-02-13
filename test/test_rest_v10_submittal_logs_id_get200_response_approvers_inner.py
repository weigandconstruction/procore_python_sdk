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

from procore_sdk.models.rest_v10_submittal_logs_id_get200_response_approvers_inner import RestV10SubmittalLogsIdGet200ResponseApproversInner

class TestRestV10SubmittalLogsIdGet200ResponseApproversInner(unittest.TestCase):
    """RestV10SubmittalLogsIdGet200ResponseApproversInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10SubmittalLogsIdGet200ResponseApproversInner:
        """Test RestV10SubmittalLogsIdGet200ResponseApproversInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10SubmittalLogsIdGet200ResponseApproversInner`
        """
        model = RestV10SubmittalLogsIdGet200ResponseApproversInner()
        if include_optional:
            return RestV10SubmittalLogsIdGet200ResponseApproversInner(
                login_information = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                id = 939302,
                response = 'Approved as Noted',
                sent_date = 'Sat May 10 00:00:00 UTC 2014',
                returned_date = 'Mon May 12 00:00:00 UTC 2014',
                due_date = 'Mon May 12 00:00:00 UTC 2014',
                comment = 'See attached drawing for wall dimensions.',
                distributed = [
                    153532
                    ],
                attachments = [
                    procore_sdk.models.rest_v10_work_order_contracts_post_201_response_attachments_inner.RestV10WorkOrderContractsPost_201_response_attachments_inner(
                        id = 5324, 
                        url = 'http://www.example.com/', 
                        filename = 'january_receipt_copy.jpg', )
                    ]
            )
        else:
            return RestV10SubmittalLogsIdGet200ResponseApproversInner(
        )
        """

    def testRestV10SubmittalLogsIdGet200ResponseApproversInner(self):
        """Test RestV10SubmittalLogsIdGet200ResponseApproversInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
