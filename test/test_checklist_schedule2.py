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

from procore_sdk.models.checklist_schedule2 import ChecklistSchedule2

class TestChecklistSchedule2(unittest.TestCase):
    """ChecklistSchedule2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChecklistSchedule2:
        """Test ChecklistSchedule2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChecklistSchedule2`
        """
        model = ChecklistSchedule2()
        if include_optional:
            return ChecklistSchedule2(
                name = 'New Checklist Schedule',
                first_inspection_due_at = '2021-09-23T11:34:27Z',
                ends_at = '2023-10-23T11:34:27Z',
                frequency = 'monthly',
                location_id = 42,
                point_of_contact_id = 42,
                responsible_contractor_id = 76,
                specification_section_id = 178,
                assignee_ids = [
                    12
                    ],
                distribution_member_ids = [
                    93
                    ]
            )
        else:
            return ChecklistSchedule2(
        )
        """

    def testChecklistSchedule2(self):
        """Test ChecklistSchedule2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
