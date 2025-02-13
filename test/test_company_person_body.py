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

from procore_sdk.models.company_person_body import CompanyPersonBody

class TestCompanyPersonBody(unittest.TestCase):
    """CompanyPersonBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompanyPersonBody:
        """Test CompanyPersonBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompanyPersonBody`
        """
        model = CompanyPersonBody()
        if include_optional:
            return CompanyPersonBody(
                person = procore_sdk.models.company_person.Company Person(
                    first_name = '', 
                    last_name = '', 
                    is_employee = True, 
                    employee_id = '', 
                    active = True, 
                    origin_id = 'OD-3483830-2', )
            )
        else:
            return CompanyPersonBody(
                person = procore_sdk.models.company_person.Company Person(
                    first_name = '', 
                    last_name = '', 
                    is_employee = True, 
                    employee_id = '', 
                    active = True, 
                    origin_id = 'OD-3483830-2', ),
        )
        """

    def testCompanyPersonBody(self):
        """Test CompanyPersonBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
