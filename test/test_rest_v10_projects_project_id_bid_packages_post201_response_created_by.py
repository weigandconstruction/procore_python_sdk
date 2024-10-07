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

from procore_sdk.models.rest_v10_projects_project_id_bid_packages_post201_response_created_by import RestV10ProjectsProjectIdBidPackagesPost201ResponseCreatedBy

class TestRestV10ProjectsProjectIdBidPackagesPost201ResponseCreatedBy(unittest.TestCase):
    """RestV10ProjectsProjectIdBidPackagesPost201ResponseCreatedBy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdBidPackagesPost201ResponseCreatedBy:
        """Test RestV10ProjectsProjectIdBidPackagesPost201ResponseCreatedBy
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdBidPackagesPost201ResponseCreatedBy`
        """
        model = RestV10ProjectsProjectIdBidPackagesPost201ResponseCreatedBy()
        if include_optional:
            return RestV10ProjectsProjectIdBidPackagesPost201ResponseCreatedBy(
                email = 'john.doe@example.com',
                first = 'John',
                last = 'Doe',
                numbers = '512-555-5555'
            )
        else:
            return RestV10ProjectsProjectIdBidPackagesPost201ResponseCreatedBy(
        )
        """

    def testRestV10ProjectsProjectIdBidPackagesPost201ResponseCreatedBy(self):
        """Test RestV10ProjectsProjectIdBidPackagesPost201ResponseCreatedBy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
