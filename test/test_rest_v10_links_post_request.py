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

from procore_sdk.models.rest_v10_links_post_request import RestV10LinksPostRequest

class TestRestV10LinksPostRequest(unittest.TestCase):
    """RestV10LinksPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10LinksPostRequest:
        """Test RestV10LinksPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10LinksPostRequest`
        """
        model = RestV10LinksPostRequest()
        if include_optional:
            return RestV10LinksPostRequest(
                link = procore_sdk.models.rest_v10_links_post_request_link.RestV10LinksPost_request_link(
                    title = 'Project cam', 
                    url = 'https://developers.procore.com/reference/authentication', )
            )
        else:
            return RestV10LinksPostRequest(
                link = procore_sdk.models.rest_v10_links_post_request_link.RestV10LinksPost_request_link(
                    title = 'Project cam', 
                    url = 'https://developers.procore.com/reference/authentication', ),
        )
        """

    def testRestV10LinksPostRequest(self):
        """Test RestV10LinksPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
