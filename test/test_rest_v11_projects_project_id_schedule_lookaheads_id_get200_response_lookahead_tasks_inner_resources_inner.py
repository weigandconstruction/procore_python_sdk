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

from procore_sdk.models.rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_lookahead_tasks_inner_resources_inner import RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerResourcesInner

class TestRestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerResourcesInner(unittest.TestCase):
    """RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerResourcesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerResourcesInner:
        """Test RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerResourcesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerResourcesInner`
        """
        model = RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerResourcesInner()
        if include_optional:
            return RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerResourcesInner(
                id = 1,
                company_id = 2,
                deleted_at = '2019-08-01T00:00Z',
                project_id = 3,
                source_uid = '00000000-0000-0000-0000-000000000000'
            )
        else:
            return RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerResourcesInner(
        )
        """

    def testRestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerResourcesInner(self):
        """Test RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseLookaheadTasksInnerResourcesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
