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

from procore_sdk.models.company_users_inner import CompanyUsersInner

class TestCompanyUsersInner(unittest.TestCase):
    """CompanyUsersInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompanyUsersInner:
        """Test CompanyUsersInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompanyUsersInner`
        """
        model = CompanyUsersInner()
        if include_optional:
            return CompanyUsersInner(
                id = 123,
                first_name = 'Jane',
                last_name = 'Doe',
                job_title = 'QA Manager',
                address = '6305 Carpinteria Ave',
                city = 'Carpinteria',
                zip = '12345',
                business_phone = '1-555-555-1234',
                business_phone_extension = 123,
                mobile_phone = '1-555-555-1234',
                fax_number = '1-555-555-1234',
                email_address = 'jane.doe@example.com',
                email_signature = '<p>Sent from Procore.</p>',
                is_active = True,
                is_employee = False,
                employee_id = '123456789',
                notes = 'notes',
                country_code = 'US',
                state_code = 'CA',
                initials = 'JD',
                origin_id = 'foobar',
                origin_data = 'OD-3483830-2',
                vendor_id = 161072,
                default_permission_template_id = 27,
                company_permission_template_id = 13,
                work_classification_id = 13,
                avatar = 'avatar.jpg'
            )
        else:
            return CompanyUsersInner(
        )
        """

    def testCompanyUsersInner(self):
        """Test CompanyUsersInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
