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

from procore_sdk.models.time_and_material_equipment_log_bulk_destroy_body import TimeAndMaterialEquipmentLogBulkDestroyBody

class TestTimeAndMaterialEquipmentLogBulkDestroyBody(unittest.TestCase):
    """TimeAndMaterialEquipmentLogBulkDestroyBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeAndMaterialEquipmentLogBulkDestroyBody:
        """Test TimeAndMaterialEquipmentLogBulkDestroyBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeAndMaterialEquipmentLogBulkDestroyBody`
        """
        model = TimeAndMaterialEquipmentLogBulkDestroyBody()
        if include_optional:
            return TimeAndMaterialEquipmentLogBulkDestroyBody(
                time_and_material_equipment_logs = procore_sdk.models.time_and_material_equipment_logs.Time and Material equipment logs(
                    time_and_material_equipment_logs_ids = [
                        3944
                        ], )
            )
        else:
            return TimeAndMaterialEquipmentLogBulkDestroyBody(
                time_and_material_equipment_logs = procore_sdk.models.time_and_material_equipment_logs.Time and Material equipment logs(
                    time_and_material_equipment_logs_ids = [
                        3944
                        ], ),
        )
        """

    def testTimeAndMaterialEquipmentLogBulkDestroyBody(self):
        """Test TimeAndMaterialEquipmentLogBulkDestroyBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
