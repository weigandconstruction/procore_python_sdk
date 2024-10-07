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

from procore_sdk.models.rest_v10_projects_project_id_bid_packages_post201_response_manager import RestV10ProjectsProjectIdBidPackagesPost201ResponseManager

class TestRestV10ProjectsProjectIdBidPackagesPost201ResponseManager(unittest.TestCase):
    """RestV10ProjectsProjectIdBidPackagesPost201ResponseManager unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdBidPackagesPost201ResponseManager:
        """Test RestV10ProjectsProjectIdBidPackagesPost201ResponseManager
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdBidPackagesPost201ResponseManager`
        """
        model = RestV10ProjectsProjectIdBidPackagesPost201ResponseManager()
        if include_optional:
            return RestV10ProjectsProjectIdBidPackagesPost201ResponseManager(
                login_information_id = 67,
                contact_id = 345,
                name = 'John Doe',
                email = '',
                job_title = 'Estimator',
                invited = True,
                vendor = procore_sdk.models.rest_v10_projects_project_id_bid_packages_post_201_response_manager_vendor.RestV10ProjectsProjectIdBidPackagesPost_201_response_manager_vendor(
                    id = 123, 
                    name = 'Vendor Name', )
            )
        else:
            return RestV10ProjectsProjectIdBidPackagesPost201ResponseManager(
        )
        """

    def testRestV10ProjectsProjectIdBidPackagesPost201ResponseManager(self):
        """Test RestV10ProjectsProjectIdBidPackagesPost201ResponseManager"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
