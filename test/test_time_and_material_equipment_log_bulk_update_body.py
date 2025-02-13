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

from procore_sdk.models.time_and_material_equipment_log_bulk_update_body import TimeAndMaterialEquipmentLogBulkUpdateBody

class TestTimeAndMaterialEquipmentLogBulkUpdateBody(unittest.TestCase):
    """TimeAndMaterialEquipmentLogBulkUpdateBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeAndMaterialEquipmentLogBulkUpdateBody:
        """Test TimeAndMaterialEquipmentLogBulkUpdateBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeAndMaterialEquipmentLogBulkUpdateBody`
        """
        model = TimeAndMaterialEquipmentLogBulkUpdateBody()
        if include_optional:
            return TimeAndMaterialEquipmentLogBulkUpdateBody(
                time_and_material_equipment_logs = [
                    procore_sdk.models.time_and_material_equipment_log_properties.Time and Material Equipment Log Properties(
                        time_and_material_entry_id = 16, 
                        description = 'This backhoe was used for the second day for all damaged pipes', 
                        uom = 'each', 
                        quantity = 10, )
                    ]
            )
        else:
            return TimeAndMaterialEquipmentLogBulkUpdateBody(
                time_and_material_equipment_logs = [
                    procore_sdk.models.time_and_material_equipment_log_properties.Time and Material Equipment Log Properties(
                        time_and_material_entry_id = 16, 
                        description = 'This backhoe was used for the second day for all damaged pipes', 
                        uom = 'each', 
                        quantity = 10, )
                    ],
        )
        """

    def testTimeAndMaterialEquipmentLogBulkUpdateBody(self):
        """Test TimeAndMaterialEquipmentLogBulkUpdateBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
