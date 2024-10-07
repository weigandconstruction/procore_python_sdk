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

from procore_sdk.models.insurance3 import Insurance3

class TestInsurance3(unittest.TestCase):
    """Insurance3 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Insurance3:
        """Test Insurance3
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Insurance3`
        """
        model = Insurance3()
        if include_optional:
            return Insurance3(
                effective_date = 'Tue Mar 03 00:00:00 UTC 2015',
                enable_expired_insurance_notifications = True,
                exempt = False,
                expiration_date = 'Wed Mar 02 00:00:00 UTC 2016',
                info_received = False,
                insurance_type = 'General Liability',
                limit = '1000000.00',
                name = 'GL Insurance Inc.',
                notes = 'Meets minimum requirements',
                policy_number = '12345GL',
                status = 'compliant',
                vendor_id = 2627684,
                additional_insured = 'John Doe',
                division_template = 'Template 1',
                insurance_sets = 'Set 1',
                origin_data = 'OD-2398273424',
                origin_id = 'ABC123'
            )
        else:
            return Insurance3(
                vendor_id = 2627684,
        )
        """

    def testInsurance3(self):
        """Test Insurance3"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
