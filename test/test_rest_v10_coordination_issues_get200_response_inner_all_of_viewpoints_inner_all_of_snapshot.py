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

from procore_sdk.models.rest_v10_coordination_issues_get200_response_inner_all_of_viewpoints_inner_all_of_snapshot import RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfSnapshot

class TestRestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfSnapshot(unittest.TestCase):
    """RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfSnapshot unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfSnapshot:
        """Test RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfSnapshot
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfSnapshot`
        """
        model = RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfSnapshot()
        if include_optional:
            return RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfSnapshot(
                id = 56,
                name = 'filename.ext',
                content_type = 'image/png',
                url = 'https://storage.procore.com/v3/d/default/procore-files/1ZE258W9K804SAJJZX19JVAB3R?sig=e7a476ec0a46154d05e0d4a554fb2ea0904cb6604670f9247c54d7c56a84d0b6'
            )
        else:
            return RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfSnapshot(
        )
        """

    def testRestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfSnapshot(self):
        """Test RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInnerAllOfSnapshot"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
