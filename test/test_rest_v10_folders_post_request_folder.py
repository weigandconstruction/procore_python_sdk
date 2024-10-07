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

from procore_sdk.models.rest_v10_folders_post_request_folder import RestV10FoldersPostRequestFolder

class TestRestV10FoldersPostRequestFolder(unittest.TestCase):
    """RestV10FoldersPostRequestFolder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10FoldersPostRequestFolder:
        """Test RestV10FoldersPostRequestFolder
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10FoldersPostRequestFolder`
        """
        model = RestV10FoldersPostRequestFolder()
        if include_optional:
            return RestV10FoldersPostRequestFolder(
                parent_id = 12,
                name = 'test_folder',
                is_tracked = True,
                explicit_permissions = True,
                custom_field_custom_field_definition_id = custom field value
            )
        else:
            return RestV10FoldersPostRequestFolder(
                name = 'test_folder',
        )
        """

    def testRestV10FoldersPostRequestFolder(self):
        """Test RestV10FoldersPostRequestFolder"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
