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

from procore_sdk.models.rest_v10_projects_project_id_correspondence_types_defaults_get200_response_inner import RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInner

class TestRestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInner(unittest.TestCase):
    """RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInner:
        """Test RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInner`
        """
        model = RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInner()
        if include_optional:
            return RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInner(
                id = 1,
                correspondence_type_id = 1,
                description = 'A description',
                due_days = 1,
                distribution_members = [
                    procore_sdk.models.rest_v11_projects_project_id_submittals_get_200_response_inner_approvers_inner_user.RestV11ProjectsProjectIdSubmittalsGet_200_response_inner_approvers_inner_user(
                        id = 161072, 
                        name = 'Carl the Contractor', )
                    ],
                available_statuses = [
                    'Open'
                    ],
                statuses = [
                    procore_sdk.models.rest_v10_projects_project_id_correspondence_types_defaults_get_200_response_inner_statuses_inner.RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet_200_response_inner_statuses_inner(
                        name = 'In Progress', 
                        status = 'Draft', )
                    ],
                private_by_default = True,
                workflows_enabled = False
            )
        else:
            return RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInner(
        )
        """

    def testRestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInner(self):
        """Test RestV10ProjectsProjectIdCorrespondenceTypesDefaultsGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
