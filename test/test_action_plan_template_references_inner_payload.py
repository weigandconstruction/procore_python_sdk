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

from procore_sdk.models.action_plan_template_references_inner_payload import ActionPlanTemplateReferencesInnerPayload

class TestActionPlanTemplateReferencesInnerPayload(unittest.TestCase):
    """ActionPlanTemplateReferencesInnerPayload unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ActionPlanTemplateReferencesInnerPayload:
        """Test ActionPlanTemplateReferencesInnerPayload
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ActionPlanTemplateReferencesInnerPayload`
        """
        model = ActionPlanTemplateReferencesInnerPayload()
        if include_optional:
            return ActionPlanTemplateReferencesInnerPayload(
                checklist_template_id = 42,
                form_template_id = 43,
                generic_tool_id = 41
            )
        else:
            return ActionPlanTemplateReferencesInnerPayload(
        )
        """

    def testActionPlanTemplateReferencesInnerPayload(self):
        """Test ActionPlanTemplateReferencesInnerPayload"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
