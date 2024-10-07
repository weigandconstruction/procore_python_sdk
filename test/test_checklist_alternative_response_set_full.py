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

from procore_sdk.models.checklist_alternative_response_set_full import ChecklistAlternativeResponseSetFull

class TestChecklistAlternativeResponseSetFull(unittest.TestCase):
    """ChecklistAlternativeResponseSetFull unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChecklistAlternativeResponseSetFull:
        """Test ChecklistAlternativeResponseSetFull
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChecklistAlternativeResponseSetFull`
        """
        model = ChecklistAlternativeResponseSetFull()
        if include_optional:
            return ChecklistAlternativeResponseSetFull(
                id = 1,
                conforming_response = 'Safe',
                deficient_response = 'At Risk',
                var_global = True
            )
        else:
            return ChecklistAlternativeResponseSetFull(
        )
        """

    def testChecklistAlternativeResponseSetFull(self):
        """Test ChecklistAlternativeResponseSetFull"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
