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

from procore_sdk.models.rest_v11_projects_project_id_drawing_disciplines_get200_response_inner import RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner

class TestRestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner(unittest.TestCase):
    """RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner:
        """Test RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner`
        """
        model = RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner()
        if include_optional:
            return RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner(
                id = 1,
                name = 'Architectural',
                position = 3,
                abbreviations = ["A","ARC"]
            )
        else:
            return RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner(
        )
        """

    def testRestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner(self):
        """Test RestV11ProjectsProjectIdDrawingDisciplinesGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
