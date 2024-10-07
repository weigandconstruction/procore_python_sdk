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

from procore_sdk.models.company_user5 import CompanyUser5

class TestCompanyUser5(unittest.TestCase):
    """CompanyUser5 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompanyUser5:
        """Test CompanyUser5
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompanyUser5`
        """
        model = CompanyUser5()
        if include_optional:
            return CompanyUser5(
                first_name = '',
                last_name = '',
                job_title = '',
                address = '',
                city = '',
                zip = '',
                business_phone = '',
                business_phone_extension = 56,
                mobile_phone = '',
                fax_number = '',
                email_address = '',
                email_signature = '',
                is_active = True,
                is_employee = True,
                employee_id = '',
                notes = '',
                country_code = '',
                state_code = '',
                initials = '',
                origin_id = '',
                origin_data = 'OD-3483830-2',
                vendor_id = 56,
                default_permission_template_id = 56,
                company_permission_template_id = 56,
                work_classification_id = 56,
                avatar = ''
            )
        else:
            return CompanyUser5(
                last_name = '',
                email_address = '',
        )
        """

    def testCompanyUser5(self):
        """Test CompanyUser5"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
