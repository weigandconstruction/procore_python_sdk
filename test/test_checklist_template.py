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

from procore_sdk.models.checklist_template import ChecklistTemplate

class TestChecklistTemplate(unittest.TestCase):
    """ChecklistTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChecklistTemplate:
        """Test ChecklistTemplate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChecklistTemplate`
        """
        model = ChecklistTemplate()
        if include_optional:
            return ChecklistTemplate(
                description = '',
                inspection_type_id = 56,
                alternative_response_set_id = 1,
                name = '',
                trade_id = 56
            )
        else:
            return ChecklistTemplate(
        )
        """

    def testChecklistTemplate(self):
        """Test ChecklistTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
