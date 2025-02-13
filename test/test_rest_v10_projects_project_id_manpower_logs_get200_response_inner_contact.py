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

from procore_sdk.models.rest_v10_projects_project_id_manpower_logs_get200_response_inner_contact import RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact

class TestRestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact(unittest.TestCase):
    """RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact:
        """Test RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact`
        """
        model = RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact()
        if include_optional:
            return RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact(
                id = 1128828,
                business_phone = '(503)744-3200',
                business_phone_extension = 1234,
                email = 'john.doe@example.com',
                fax_number = '813043',
                job_title = 'Engineer',
                login_information_id = 56,
                mobile_phone = '',
                name = 'A-1 Electric Company',
                vendor_name = ''
            )
        else:
            return RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact(
        )
        """

    def testRestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact(self):
        """Test RestV10ProjectsProjectIdManpowerLogsGet200ResponseInnerContact"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
