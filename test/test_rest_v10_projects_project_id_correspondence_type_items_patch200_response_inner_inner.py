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

from procore_sdk.models.rest_v10_projects_project_id_correspondence_type_items_patch200_response_inner_inner import RestV10ProjectsProjectIdCorrespondenceTypeItemsPatch200ResponseInnerInner

class TestRestV10ProjectsProjectIdCorrespondenceTypeItemsPatch200ResponseInnerInner(unittest.TestCase):
    """RestV10ProjectsProjectIdCorrespondenceTypeItemsPatch200ResponseInnerInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdCorrespondenceTypeItemsPatch200ResponseInnerInner:
        """Test RestV10ProjectsProjectIdCorrespondenceTypeItemsPatch200ResponseInnerInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdCorrespondenceTypeItemsPatch200ResponseInnerInner`
        """
        model = RestV10ProjectsProjectIdCorrespondenceTypeItemsPatch200ResponseInnerInner()
        if include_optional:
            return RestV10ProjectsProjectIdCorrespondenceTypeItemsPatch200ResponseInnerInner(
                id = 123,
                status = 'success',
                errors = None
            )
        else:
            return RestV10ProjectsProjectIdCorrespondenceTypeItemsPatch200ResponseInnerInner(
        )
        """

    def testRestV10ProjectsProjectIdCorrespondenceTypeItemsPatch200ResponseInnerInner(self):
        """Test RestV10ProjectsProjectIdCorrespondenceTypeItemsPatch200ResponseInnerInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
