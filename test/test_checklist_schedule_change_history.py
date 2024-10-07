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

from procore_sdk.models.checklist_schedule_change_history import ChecklistScheduleChangeHistory

class TestChecklistScheduleChangeHistory(unittest.TestCase):
    """ChecklistScheduleChangeHistory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChecklistScheduleChangeHistory:
        """Test ChecklistScheduleChangeHistory
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChecklistScheduleChangeHistory`
        """
        model = ChecklistScheduleChangeHistory()
        if include_optional:
            return ChecklistScheduleChangeHistory(
                id = 101,
                column = 'name',
                old_value = 'The original title',
                new_value = 'The updated title',
                created_by_id = 102,
                created_at = '2018-05-08T13:21:20Z'
            )
        else:
            return ChecklistScheduleChangeHistory(
        )
        """

    def testChecklistScheduleChangeHistory(self):
        """Test ChecklistScheduleChangeHistory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
