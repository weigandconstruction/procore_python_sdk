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

from procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get200_response_inner_recording import RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecording

class TestRestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecording(unittest.TestCase):
    """RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecording unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecording:
        """Test RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecording
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecording`
        """
        model = RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecording()
        if include_optional:
            return RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecording(
                id = 1,
                witness_statement_id = 8,
                attachment = procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_recording_attachment.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_recording_attachment(
                    id = 30, 
                    content_type = 'audio/mp4', 
                    name = 'attachment.mp4', 
                    thumbnail_url = 'http://example.com/v4/d/us-east-1/attachment-thumbnail.mp4', 
                    url = 'http://example.com/v4/d/us-east-1/attachment.mp4', 
                    viewable_document_id = 4, ),
                captured_by = procore_sdk.models.rest_v11_projects_project_id_recycle_bin_incidents_witness_statements_get_200_response_inner_recording_captured_by.RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet_200_response_inner_recording_captured_by(
                    id = 1, 
                    name = 'John Doe', 
                    locale = 'en-GB', 
                    login = 'test@example.com', ),
                created_at = '2016-10-25T17:53:35Z'
            )
        else:
            return RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecording(
        )
        """

    def testRestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecording(self):
        """Test RestV11ProjectsProjectIdRecycleBinIncidentsWitnessStatementsGet200ResponseInnerRecording"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
