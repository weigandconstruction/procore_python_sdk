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

from procore_sdk.models.body_part import BodyPart

class TestBodyPart(unittest.TestCase):
    """BodyPart unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BodyPart:
        """Test BodyPart
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BodyPart`
        """
        model = BodyPart()
        if include_optional:
            return BodyPart(
                id = 999,
                name = 'finger_index_right',
                selectable = True,
                created_at = '2016-10-25T17:53:35Z',
                updated_at = '2016-10-25T17:53:35Z',
                parent_id = 999
            )
        else:
            return BodyPart(
        )
        """

    def testBodyPart(self):
        """Test BodyPart"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
