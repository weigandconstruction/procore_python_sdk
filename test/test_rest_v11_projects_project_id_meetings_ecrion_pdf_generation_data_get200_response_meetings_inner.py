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

from procore_sdk.models.rest_v11_projects_project_id_meetings_ecrion_pdf_generation_data_get200_response_meetings_inner import RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponseMeetingsInner

class TestRestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponseMeetingsInner(unittest.TestCase):
    """RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponseMeetingsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponseMeetingsInner:
        """Test RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponseMeetingsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponseMeetingsInner`
        """
        model = RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponseMeetingsInner()
        if include_optional:
            return RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponseMeetingsInner(
                id = 2,
                name = 'meeting_1',
                xml = '<xml></xml>'
            )
        else:
            return RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponseMeetingsInner(
        )
        """

    def testRestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponseMeetingsInner(self):
        """Test RestV11ProjectsProjectIdMeetingsEcrionPdfGenerationDataGet200ResponseMeetingsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
