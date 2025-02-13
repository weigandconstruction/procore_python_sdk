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

from procore_sdk.models.rest_v10_projects_project_id_specification_uploads_post_request import RestV10ProjectsProjectIdSpecificationUploadsPostRequest

class TestRestV10ProjectsProjectIdSpecificationUploadsPostRequest(unittest.TestCase):
    """RestV10ProjectsProjectIdSpecificationUploadsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdSpecificationUploadsPostRequest:
        """Test RestV10ProjectsProjectIdSpecificationUploadsPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdSpecificationUploadsPostRequest`
        """
        model = RestV10ProjectsProjectIdSpecificationUploadsPostRequest()
        if include_optional:
            return RestV10ProjectsProjectIdSpecificationUploadsPostRequest(
                specification_set_id = 1144,
                specification_section_id = 3001,
                default_revision = '1',
                files = [
                    'See body parameters description.'
                    ],
                upload_uuids = [
                    '1ZE258W9K804SAJJZX19JVAB3R'
                    ],
                issued_date = '2015-02-17',
                received_date = '2015-03-17',
                ignore_number = '072100',
                spec_format = 'CSI'
            )
        else:
            return RestV10ProjectsProjectIdSpecificationUploadsPostRequest(
                specification_set_id = 1144,
                spec_format = 'CSI',
        )
        """

    def testRestV10ProjectsProjectIdSpecificationUploadsPostRequest(self):
        """Test RestV10ProjectsProjectIdSpecificationUploadsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
