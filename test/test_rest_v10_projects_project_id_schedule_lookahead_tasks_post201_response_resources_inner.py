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

from procore_sdk.models.rest_v10_projects_project_id_schedule_lookahead_tasks_post201_response_resources_inner import RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner

class TestRestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner(unittest.TestCase):
    """RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner:
        """Test RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner`
        """
        model = RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner()
        if include_optional:
            return RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner(
                source_uid = '0687b2f6-dc92-40c7-a8c8-a3c1f3ac9305',
                id = 1359235,
                name = 'INTERIOR'
            )
        else:
            return RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner(
        )
        """

    def testRestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner(self):
        """Test RestV10ProjectsProjectIdScheduleLookaheadTasksPost201ResponseResourcesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
