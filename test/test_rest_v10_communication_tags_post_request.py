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

from procore_sdk.models.rest_v10_communication_tags_post_request import RestV10CommunicationTagsPostRequest

class TestRestV10CommunicationTagsPostRequest(unittest.TestCase):
    """RestV10CommunicationTagsPostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CommunicationTagsPostRequest:
        """Test RestV10CommunicationTagsPostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CommunicationTagsPostRequest`
        """
        model = RestV10CommunicationTagsPostRequest()
        if include_optional:
            return RestV10CommunicationTagsPostRequest(
                communication_tag = procore_sdk.models.rest_v10_communication_tags_post_request_communication_tag.RestV10CommunicationTagsPost_request_communication_tag(
                    title = '', )
            )
        else:
            return RestV10CommunicationTagsPostRequest(
                communication_tag = procore_sdk.models.rest_v10_communication_tags_post_request_communication_tag.RestV10CommunicationTagsPost_request_communication_tag(
                    title = '', ),
        )
        """

    def testRestV10CommunicationTagsPostRequest(self):
        """Test RestV10CommunicationTagsPostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
