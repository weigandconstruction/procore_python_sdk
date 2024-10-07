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

from procore_sdk.models.managed_equipment_body import ManagedEquipmentBody

class TestManagedEquipmentBody(unittest.TestCase):
    """ManagedEquipmentBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ManagedEquipmentBody:
        """Test ManagedEquipmentBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ManagedEquipmentBody`
        """
        model = ManagedEquipmentBody()
        if include_optional:
            return ManagedEquipmentBody(
                managed_equipment = procore_sdk.models.managed_equipment.ManagedEquipment(
                    current_project_id = 14406, 
                    name = 'Backhoe', 
                    serial_number = 'S#12892', 
                    identification_number = 'ID982011', 
                    description = 'This equipment was brought in for the backyard work.', 
                    managed_equipment_make_id = 14, 
                    managed_equipment_model_id = 13, 
                    managed_equipment_type_id = 13, 
                    managed_equipment_category_id = 13, 
                    company_visible = False, 
                    year = 2017, 
                    status = 'in_use', 
                    ownership = 'owned', )
            )
        else:
            return ManagedEquipmentBody(
                managed_equipment = procore_sdk.models.managed_equipment.ManagedEquipment(
                    current_project_id = 14406, 
                    name = 'Backhoe', 
                    serial_number = 'S#12892', 
                    identification_number = 'ID982011', 
                    description = 'This equipment was brought in for the backyard work.', 
                    managed_equipment_make_id = 14, 
                    managed_equipment_model_id = 13, 
                    managed_equipment_type_id = 13, 
                    managed_equipment_category_id = 13, 
                    company_visible = False, 
                    year = 2017, 
                    status = 'in_use', 
                    ownership = 'owned', ),
        )
        """

    def testManagedEquipmentBody(self):
        """Test ManagedEquipmentBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
