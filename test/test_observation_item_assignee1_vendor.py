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

from procore_sdk.models.observation_item_assignee1_vendor import ObservationItemAssignee1Vendor

class TestObservationItemAssignee1Vendor(unittest.TestCase):
    """ObservationItemAssignee1Vendor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ObservationItemAssignee1Vendor:
        """Test ObservationItemAssignee1Vendor
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ObservationItemAssignee1Vendor`
        """
        model = ObservationItemAssignee1Vendor()
        if include_optional:
            return ObservationItemAssignee1Vendor(
                id = 2675,
                name = 'Brick and Morty'
            )
        else:
            return ObservationItemAssignee1Vendor(
        )
        """

    def testObservationItemAssignee1Vendor(self):
        """Test ObservationItemAssignee1Vendor"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
