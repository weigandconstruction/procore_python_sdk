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

from procore_sdk.models.company_vendor_sync_body_updates_inner import CompanyVendorSyncBodyUpdatesInner

class TestCompanyVendorSyncBodyUpdatesInner(unittest.TestCase):
    """CompanyVendorSyncBodyUpdatesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompanyVendorSyncBodyUpdatesInner:
        """Test CompanyVendorSyncBodyUpdatesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompanyVendorSyncBodyUpdatesInner`
        """
        model = CompanyVendorSyncBodyUpdatesInner()
        if include_optional:
            return CompanyVendorSyncBodyUpdatesInner(
                id = 13513,
                name = 'Poodle Electric',
                address = '846 Dogglesworth Drive',
                city = 'Jeffersonville',
                zip = '47130',
                business_phone = '(812) 284-8506',
                mobile_phone = '(812) 556-3397',
                fax_number = '(812) 989-9810',
                email_address = 'jane.doe@example.com',
                is_active = True,
                state_code = 'IN',
                authorized_bidder = True,
                prequalified = False,
                country_code = 'US',
                labor_union = 'IWW 872',
                license_number = '1901XYZ',
                website = 'http://poodleparade.com',
                union_member = True,
                non_union_prevailing_wage = False,
                abbreviated_name = 'PE',
                notes = 'Owned by a cat',
                vendor_group_id = 1843218,
                parent_id = 1306797,
                primary_contact_id = 1306796,
                origin_id = 'ref-12345',
                origin_data = '{"data_field":{"is_important":true}}',
                origin_code = 'PE-12345',
                trade_ids = [123,456],
                bidding_distribution_ids = [123,456],
                standard_cost_code_ids = [123,456],
                trade_name = 'Woofer Electric',
                bidding = procore_sdk.models.company_vendor_sync_body_updates_inner_bidding.Company_Vendor_Sync_Body_updates_inner_bidding(
                    affirmative_action = True, 
                    small_business = True, 
                    african_american_business = True, 
                    hispanic_business = False, 
                    womens_business = False, 
                    historically_underutilized_business = True, 
                    sdvo_business = False, 
                    certified_business_enterprise = True, 
                    asian_american_business = True, 
                    native_american_business = True, 
                    disadvantaged_business = False, 
                    minority_business_enterprise = True, 
                    eight_a_business = True, )
            )
        else:
            return CompanyVendorSyncBodyUpdatesInner(
        )
        """

    def testCompanyVendorSyncBodyUpdatesInner(self):
        """Test CompanyVendorSyncBodyUpdatesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
