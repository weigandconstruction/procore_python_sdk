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

from procore_sdk.models.body74 import Body74

class TestBody74(unittest.TestCase):
    """Body74 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body74:
        """Test Body74
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body74`
        """
        model = Body74()
        if include_optional:
            return Body74(
                instruction = procore_sdk.models.instruction.Instruction(
                    number = '1', 
                    title = 'Fix this thing', 
                    status = 'draft', 
                    instruction_type_id = 1, 
                    instruction_from_id = 1, 
                    date_received = 'Thu Oct 13 00:00:00 UTC 2016', 
                    schedule_impact = procore_sdk.models.instruction_schedule_impact.Instruction_schedule_impact(
                        status = 'yes_known', 
                        value = 14, ), 
                    cost_impact = procore_sdk.models.instruction_cost_impact.Instruction_cost_impact(
                        status = 'yes_known', 
                        value = 12039.55, ), 
                    private = False, 
                    description = 'This is a description', 
                    attention_ids = [
                        56
                        ], 
                    distribution_member_ids = [
                        56
                        ], 
                    trade_ids = [
                        56
                        ], 
                    attachments = [
                        ''
                        ], )
            )
        else:
            return Body74(
                instruction = procore_sdk.models.instruction.Instruction(
                    number = '1', 
                    title = 'Fix this thing', 
                    status = 'draft', 
                    instruction_type_id = 1, 
                    instruction_from_id = 1, 
                    date_received = 'Thu Oct 13 00:00:00 UTC 2016', 
                    schedule_impact = procore_sdk.models.instruction_schedule_impact.Instruction_schedule_impact(
                        status = 'yes_known', 
                        value = 14, ), 
                    cost_impact = procore_sdk.models.instruction_cost_impact.Instruction_cost_impact(
                        status = 'yes_known', 
                        value = 12039.55, ), 
                    private = False, 
                    description = 'This is a description', 
                    attention_ids = [
                        56
                        ], 
                    distribution_member_ids = [
                        56
                        ], 
                    trade_ids = [
                        56
                        ], 
                    attachments = [
                        ''
                        ], ),
        )
        """

    def testBody74(self):
        """Test Body74"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
