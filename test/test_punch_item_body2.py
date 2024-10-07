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

from procore_sdk.models.punch_item_body2 import PunchItemBody2

class TestPunchItemBody2(unittest.TestCase):
    """PunchItemBody2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PunchItemBody2:
        """Test PunchItemBody2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PunchItemBody2`
        """
        model = PunchItemBody2()
        if include_optional:
            return PunchItemBody2(
                project_id = 56,
                punch_item = procore_sdk.models.punch_item.Punch Item(
                    description = 'Here is my updated description', 
                    due = 'Fri Jan 01 00:00:00 UTC 2016', 
                    name = 'My Updated Item', 
                    schedule_risk = 'ml_high', 
                    position = 56, 
                    priority = '', 
                    private = False, 
                    status = 'open', 
                    date_initiated = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    schedule_impact = 'yes_known', 
                    schedule_impact_days = 43, 
                    reference = '4543b34', 
                    cost_impact = 'yes_known', 
                    cost_impact_amount = 54, 
                    trade_id = 1234, 
                    punch_item_type_id = 5436, 
                    login_information_ids = [2343,45343], 
                    distribution_member_ids = [4323,86298], 
                    punch_item_manager_id = 42, 
                    final_approver_id = 162, 
                    location_id = 9823, 
                    mt_location = ["upstairs","meetingroom"], 
                    workflow_status = 'initiated', 
                    drawing_revision_ids = [4,5], 
                    file_version_ids = [6,7], 
                    form_ids = [7,8], 
                    image_ids = [9,10], 
                    upload_ids = ["4120226e-36a8-416f-970e-880bae78164f","de07e35a-4860-4f96-acd8-8360833dc495"], 
                    custom_field_%{custom_field_definition_id} = custom field value, )
            )
        else:
            return PunchItemBody2(
                project_id = 56,
                punch_item = procore_sdk.models.punch_item.Punch Item(
                    description = 'Here is my updated description', 
                    due = 'Fri Jan 01 00:00:00 UTC 2016', 
                    name = 'My Updated Item', 
                    schedule_risk = 'ml_high', 
                    position = 56, 
                    priority = '', 
                    private = False, 
                    status = 'open', 
                    date_initiated = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                    schedule_impact = 'yes_known', 
                    schedule_impact_days = 43, 
                    reference = '4543b34', 
                    cost_impact = 'yes_known', 
                    cost_impact_amount = 54, 
                    trade_id = 1234, 
                    punch_item_type_id = 5436, 
                    login_information_ids = [2343,45343], 
                    distribution_member_ids = [4323,86298], 
                    punch_item_manager_id = 42, 
                    final_approver_id = 162, 
                    location_id = 9823, 
                    mt_location = ["upstairs","meetingroom"], 
                    workflow_status = 'initiated', 
                    drawing_revision_ids = [4,5], 
                    file_version_ids = [6,7], 
                    form_ids = [7,8], 
                    image_ids = [9,10], 
                    upload_ids = ["4120226e-36a8-416f-970e-880bae78164f","de07e35a-4860-4f96-acd8-8360833dc495"], 
                    custom_field_%{custom_field_definition_id} = custom field value, ),
        )
        """

    def testPunchItemBody2(self):
        """Test PunchItemBody2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
