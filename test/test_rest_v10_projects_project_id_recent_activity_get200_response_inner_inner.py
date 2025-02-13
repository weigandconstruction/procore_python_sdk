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

from procore_sdk.models.rest_v10_projects_project_id_recent_activity_get200_response_inner_inner import RestV10ProjectsProjectIdRecentActivityGet200ResponseInnerInner

class TestRestV10ProjectsProjectIdRecentActivityGet200ResponseInnerInner(unittest.TestCase):
    """RestV10ProjectsProjectIdRecentActivityGet200ResponseInnerInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdRecentActivityGet200ResponseInnerInner:
        """Test RestV10ProjectsProjectIdRecentActivityGet200ResponseInnerInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdRecentActivityGet200ResponseInnerInner`
        """
        model = RestV10ProjectsProjectIdRecentActivityGet200ResponseInnerInner()
        if include_optional:
            return RestV10ProjectsProjectIdRecentActivityGet200ResponseInnerInner(
                id = 0,
                details = '#211000-1.0: Private submittal with Sub-GC-AE workflow',
                number = 1,
                created_by = 'Jennifer Howard',
                created_at = '2022-12-15T18:16:57Z',
                updated_at = '2022-12-15T18:17:19Z',
                status = 'Draft',
                type = 'Submittals',
                activity_type = 'submittal_log',
                url = 'https://localhost/3279/project/submittal_logs/66951',
                due_date = 'Thu Jan 26 00:00:00 UTC 2023'
            )
        else:
            return RestV10ProjectsProjectIdRecentActivityGet200ResponseInnerInner(
        )
        """

    def testRestV10ProjectsProjectIdRecentActivityGet200ResponseInnerInner(self):
        """Test RestV10ProjectsProjectIdRecentActivityGet200ResponseInnerInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
