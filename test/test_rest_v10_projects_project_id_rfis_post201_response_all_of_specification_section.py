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

from procore_sdk.models.rest_v10_projects_project_id_rfis_post201_response_all_of_specification_section import RestV10ProjectsProjectIdRfisPost201ResponseAllOfSpecificationSection

class TestRestV10ProjectsProjectIdRfisPost201ResponseAllOfSpecificationSection(unittest.TestCase):
    """RestV10ProjectsProjectIdRfisPost201ResponseAllOfSpecificationSection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdRfisPost201ResponseAllOfSpecificationSection:
        """Test RestV10ProjectsProjectIdRfisPost201ResponseAllOfSpecificationSection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdRfisPost201ResponseAllOfSpecificationSection`
        """
        model = RestV10ProjectsProjectIdRfisPost201ResponseAllOfSpecificationSection()
        if include_optional:
            return RestV10ProjectsProjectIdRfisPost201ResponseAllOfSpecificationSection(
                id = 56,
                description = '',
                number = ''
            )
        else:
            return RestV10ProjectsProjectIdRfisPost201ResponseAllOfSpecificationSection(
        )
        """

    def testRestV10ProjectsProjectIdRfisPost201ResponseAllOfSpecificationSection(self):
        """Test RestV10ProjectsProjectIdRfisPost201ResponseAllOfSpecificationSection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
