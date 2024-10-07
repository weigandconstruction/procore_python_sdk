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

from procore_sdk.models.rfi_body2 import RFIBody2

class TestRFIBody2(unittest.TestCase):
    """RFIBody2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RFIBody2:
        """Test RFIBody2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RFIBody2`
        """
        model = RFIBody2()
        if include_optional:
            return RFIBody2(
                data = [
                    procore_sdk.models.rfi_body_2_data_inner.RFI_Body_2_data_inner(
                        id = '12345', 
                        cost_code_id = 21, 
                        cost_impact = procore_sdk.models.rfi_body_rfi_cost_impact.RFI_Body_rfi_cost_impact(
                            status = 'yes_known', 
                            value = 12039.55, ), 
                        drawing_number = '1A', 
                        due_date = 'Mon Jul 26 00:00:00 UTC 2021', 
                        location_id = 21, 
                        private = False, 
                        received_from_login_information_id = 123, 
                        reference = 'Color of the kitchen wall', 
                        responsible_contractor_id = 123, 
                        rfi_manager_id = 1, 
                        schedule_impact = procore_sdk.models.rfi_body_rfi_schedule_impact.RFI_Body_rfi_schedule_impact(
                            status = 'yes_known', 
                            value = 0, ), 
                        specification_section_id = 123, 
                        sub_job_id = 123, 
                        subject = 'Wall color', )
                    ]
            )
        else:
            return RFIBody2(
                data = [
                    procore_sdk.models.rfi_body_2_data_inner.RFI_Body_2_data_inner(
                        id = '12345', 
                        cost_code_id = 21, 
                        cost_impact = procore_sdk.models.rfi_body_rfi_cost_impact.RFI_Body_rfi_cost_impact(
                            status = 'yes_known', 
                            value = 12039.55, ), 
                        drawing_number = '1A', 
                        due_date = 'Mon Jul 26 00:00:00 UTC 2021', 
                        location_id = 21, 
                        private = False, 
                        received_from_login_information_id = 123, 
                        reference = 'Color of the kitchen wall', 
                        responsible_contractor_id = 123, 
                        rfi_manager_id = 1, 
                        schedule_impact = procore_sdk.models.rfi_body_rfi_schedule_impact.RFI_Body_rfi_schedule_impact(
                            status = 'yes_known', 
                            value = 0, ), 
                        specification_section_id = 123, 
                        sub_job_id = 123, 
                        subject = 'Wall color', )
                    ],
        )
        """

    def testRFIBody2(self):
        """Test RFIBody2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
