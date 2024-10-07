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

from procore_sdk.models.billing_period1 import BillingPeriod1

class TestBillingPeriod1(unittest.TestCase):
    """BillingPeriod1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BillingPeriod1:
        """Test BillingPeriod1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BillingPeriod1`
        """
        model = BillingPeriod1()
        if include_optional:
            return BillingPeriod1(
                due_date = 'Thu Oct 25 00:00:00 UTC 2012',
                start_date = 'Mon Oct 01 00:00:00 UTC 2012',
                end_date = 'Wed Oct 31 00:00:00 UTC 2012',
                status = 'open'
            )
        else:
            return BillingPeriod1(
                due_date = 'Thu Oct 25 00:00:00 UTC 2012',
                start_date = 'Mon Oct 01 00:00:00 UTC 2012',
                end_date = 'Wed Oct 31 00:00:00 UTC 2012',
                status = 'open',
        )
        """

    def testBillingPeriod1(self):
        """Test BillingPeriod1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
