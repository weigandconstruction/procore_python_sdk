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

from procore_sdk.models.rest_v10_projects_project_id_distribution_groups_get200_response_inner_users_inner import RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner

class TestRestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner(unittest.TestCase):
    """RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner:
        """Test RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner`
        """
        model = RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner()
        if include_optional:
            return RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner(
                id = 161072,
                name = 'Carl the Contractor',
                login = 'carl.contractor@example.com',
                image_url = 'http://s3.amazonaws.com/pro-core.com/prostore/20150713184222_production_74548228.gif?AWSAccessKeyId=0PFNH01C4MZVXKXZNK82&Expires=2067964943&Signature=l4zpZIM3bgxydrr4hn6lM%2FdtreQ%3D',
                initials = 'BS'
            )
        else:
            return RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner(
        )
        """

    def testRestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner(self):
        """Test RestV10ProjectsProjectIdDistributionGroupsGet200ResponseInnerUsersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
