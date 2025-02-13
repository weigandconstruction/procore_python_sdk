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

from procore_sdk.models.timesheet3 import Timesheet3

class TestTimesheet3(unittest.TestCase):
    """Timesheet3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Timesheet3:
        """Test Timesheet3
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Timesheet3`
        """
        model = Timesheet3()
        if include_optional:
            return Timesheet3(
                id = 1,
                created_at = '2012-10-23T21:39:40Z',
                updated_at = '2012-10-24T21:39:40Z',
                var_date = 'Tue May 12 00:00:00 UTC 2015',
                number = 1,
                created_by = procore_sdk.models.rest_v10_projects_project_id_work_logs_get_200_response_inner_created_by.RestV10ProjectsProjectIdWorkLogsGet_200_response_inner_created_by(
                    id = 160586, 
                    login = 'carl.contractor@example.com', 
                    name = 'Carl Contractor', ),
                name = '2015-05-12 - 01',
                status = 'pending'
            )
        else:
            return Timesheet3(
        )
        """

    def testTimesheet3(self):
        """Test Timesheet3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
