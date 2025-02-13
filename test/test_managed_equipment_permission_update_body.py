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

from procore_sdk.models.managed_equipment_permission_update_body import ManagedEquipmentPermissionUpdateBody

class TestManagedEquipmentPermissionUpdateBody(unittest.TestCase):
    """ManagedEquipmentPermissionUpdateBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ManagedEquipmentPermissionUpdateBody:
        """Test ManagedEquipmentPermissionUpdateBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ManagedEquipmentPermissionUpdateBody`
        """
        model = ManagedEquipmentPermissionUpdateBody()
        if include_optional:
            return ManagedEquipmentPermissionUpdateBody(
                id = 93988,
                user_access_level_id = 2
            )
        else:
            return ManagedEquipmentPermissionUpdateBody(
        )
        """

    def testManagedEquipmentPermissionUpdateBody(self):
        """Test ManagedEquipmentPermissionUpdateBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
