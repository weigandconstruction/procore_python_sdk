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

from procore_sdk.models.extended_view2 import ExtendedView2

class TestExtendedView2(unittest.TestCase):
    """ExtendedView2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExtendedView2:
        """Test ExtendedView2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExtendedView2`
        """
        model = ExtendedView2()
        if include_optional:
            return ExtendedView2(
                contact = procore_sdk.models.normal_contact.Normal_contact(
                    is_active = True, 
                    email = 'paul@example.com', ),
                employee_id = '123456789',
                first_name = 'Leah',
                id = 381006,
                is_employee = False,
                last_name = 'Russell',
                user_id = 700215,
                user_uuid = 56,
                work_classification_id = 398438,
                origin_id = 398438,
                work_classification = procore_sdk.models.extended_view_work_classification.extended_view_work_classification(
                    id = 57869, 
                    name = 'Driver', ),
                vendor = procore_sdk.models.compact.Compact(
                    id = 161072, 
                    name = 'SID Architecture', )
            )
        else:
            return ExtendedView2(
        )
        """

    def testExtendedView2(self):
        """Test ExtendedView2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
