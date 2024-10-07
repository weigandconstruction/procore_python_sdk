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

from procore_sdk.models.rest_v10_companies_company_id_vendors_inactive_get200_response_inner import RestV10CompaniesCompanyIdVendorsInactiveGet200ResponseInner

class TestRestV10CompaniesCompanyIdVendorsInactiveGet200ResponseInner(unittest.TestCase):
    """RestV10CompaniesCompanyIdVendorsInactiveGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdVendorsInactiveGet200ResponseInner:
        """Test RestV10CompaniesCompanyIdVendorsInactiveGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdVendorsInactiveGet200ResponseInner`
        """
        model = RestV10CompaniesCompanyIdVendorsInactiveGet200ResponseInner()
        if include_optional:
            return RestV10CompaniesCompanyIdVendorsInactiveGet200ResponseInner(
                id = 161072,
                name = 'SID Architecture',
                abbreviated_name = 'PE',
                address = '846 Dogglesworth Drive',
                authorized_bidder = True,
                business_id = '89cac92d-fbd8-40ec-a1fc-24bbbd035a78',
                business_phone = '(800) 555-1234',
                city = 'Jeffersonville',
                contact_count = 5,
                company = 'Stock Construction',
                company_vendor = False,
                country_code = 'US',
                created_at = '2016-10-23T21:39:40Z',
                email_address = 'joe-vendor@example.com',
                fax_number = '(800) 555-5678',
                is_active = True,
                is_connected = True,
                labor_union = 'IWW 872',
                license_number = '1901XYZ',
                logo = 'https://s3.amazonaws.com/pro-core.com/prostore/20160718141208_development_528209843.jpeg?AWSAccessKeyId=AKIAJ5JUTRRCJA6V2DKA&Expires=2100028332&Signature=pjM0nzUOxNrtjM2F0oTG2dbkPa8%3D',
                mobile_phone = '(800) 555-1234',
                non_union_prevailing_wage = False,
                notes = 'owned by a dog',
                origin_data = 'OD-2398273424',
                origin_id = 'foobar',
                origin_code = 'foobar',
                prequalified = False,
                state_code = 'IN',
                synced_to_erp = False,
                trade_name = 'Woofer Electric',
                union_member = False,
                updated_at = '2016-10-23T21:39:40Z',
                website = 'http://example-vendor.com',
                zip = '47130',
                business_register = {"id":321,"type":"abn","identifier":"51824753556","verified_at":"2018-06-11T15:56:25Z","verification_status":"active"},
                vendor_group = {"id":1,"name":"Otis Elevators"},
                primary_contact = {"id":1306796,"first_name":"John","last_name":"Doe","business_phone":"5555555555","business_phone_extension":123,"fax_number":"5555555555","mobile_phone":"5555555555","email_address":"john.doe@example.com","created_at":"2016-10-23T21:39:40Z","updated_at":"2016-10-23T21:39:40Z"},
                attachments = [
                    procore_sdk.models.rest_v10_work_order_contracts_post_201_response_attachments_inner.RestV10WorkOrderContractsPost_201_response_attachments_inner(
                        id = 5324, 
                        url = 'http://www.example.com/', 
                        filename = 'january_receipt_copy.jpg', )
                    ],
                children_count = 0,
                legal_name = 'Stock Construction',
                parent = {"id":634512,"name":"Poodle Electric Inc."},
                trades = [
                    procore_sdk.models.trade.Trade(
                        id = 999, 
                        name = '09 - acoustical panels', 
                        active = True, 
                        updated_at = '2016-08-01T23:33:54Z', )
                    ],
                bidding_distribution = [
                    null
                    ],
                bidding = {"affirmative_action":false,"small_business":false,"african_american_business":true,"hispanic_business":false,"womens_business":false,"historically_underutilized_business":false,"sdvo_business":false,"certified_business_enterprise":true,"asian_american_business":false,"native_american_business":true,"disadvantaged_business":false,"minority_business_enterprise":false,"eight_a_business":true},
                project_ids = [
                    56
                    ],
                standard_cost_codes = [
                    procore_sdk.models.standard_cost_code.Standard Cost Code(
                        id = 12345, 
                        standard_cost_code_list_id = 12345, 
                        parent_id = 12345, 
                        code = '300', 
                        full_code = '02-300', 
                        name = 'Site Work', 
                        origin_data = 'OD-2398273424', 
                        origin_id = 'ABC123', )
                    ],
                links = procore_sdk.models.rest_v10_projects_project_id_vendors_inactive_get_200_response_inner_all_of__links.RestV10ProjectsProjectIdVendorsInactiveGet_200_response_inner_allOf__links(
                    reactivate = 'https://api.procore.com/rest/v1.0/companies/1/vendors/inactive/1', )
            )
        else:
            return RestV10CompaniesCompanyIdVendorsInactiveGet200ResponseInner(
        )
        """

    def testRestV10CompaniesCompanyIdVendorsInactiveGet200ResponseInner(self):
        """Test RestV10CompaniesCompanyIdVendorsInactiveGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
