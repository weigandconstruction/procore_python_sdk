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

from procore_sdk.models.rest_v11_projects_project_id_schedule_lookaheads_id_get200_response_generation_errors_inner_task import RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseGenerationErrorsInnerTask

class TestRestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseGenerationErrorsInnerTask(unittest.TestCase):
    """RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseGenerationErrorsInnerTask unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseGenerationErrorsInnerTask:
        """Test RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseGenerationErrorsInnerTask
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseGenerationErrorsInnerTask`
        """
        model = RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseGenerationErrorsInnerTask()
        if include_optional:
            return RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseGenerationErrorsInnerTask(
                id = 43,
                row_number = 43,
                name = 'task'
            )
        else:
            return RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseGenerationErrorsInnerTask(
        )
        """

    def testRestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseGenerationErrorsInnerTask(self):
        """Test RestV11ProjectsProjectIdScheduleLookaheadsIdGet200ResponseGenerationErrorsInnerTask"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
