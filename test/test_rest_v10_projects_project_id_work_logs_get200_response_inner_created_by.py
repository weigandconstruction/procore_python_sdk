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

from procore_sdk.models.rest_v10_projects_project_id_work_logs_get200_response_inner_created_by import RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy

class TestRestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy(unittest.TestCase):
    """RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy:
        """Test RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy`
        """
        model = RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy()
        if include_optional:
            return RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy(
                id = 160586,
                login = 'carl.contractor@example.com',
                name = 'Carl Contractor'
            )
        else:
            return RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy(
        )
        """

    def testRestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy(self):
        """Test RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
