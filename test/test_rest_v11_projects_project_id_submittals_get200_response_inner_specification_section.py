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

from procore_sdk.models.rest_v11_projects_project_id_submittals_get200_response_inner_specification_section import RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSpecificationSection

class TestRestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSpecificationSection(unittest.TestCase):
    """RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSpecificationSection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSpecificationSection:
        """Test RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSpecificationSection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSpecificationSection`
        """
        model = RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSpecificationSection()
        if include_optional:
            return RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSpecificationSection(
                id = 161072,
                number = '08560',
                description = 'Vinyl Windows',
                label = '08560 Vinyl Windows',
                current_revision_id = 145092
            )
        else:
            return RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSpecificationSection(
        )
        """

    def testRestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSpecificationSection(self):
        """Test RestV11ProjectsProjectIdSubmittalsGet200ResponseInnerSpecificationSection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
