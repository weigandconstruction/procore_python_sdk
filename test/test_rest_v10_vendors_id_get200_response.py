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

from procore_sdk.models.rest_v10_vendors_id_get200_response import RestV10VendorsIdGet200Response

class TestRestV10VendorsIdGet200Response(unittest.TestCase):
    """RestV10VendorsIdGet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10VendorsIdGet200Response:
        """Test RestV10VendorsIdGet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10VendorsIdGet200Response`
        """
        model = RestV10VendorsIdGet200Response()
        if include_optional:
            return RestV10VendorsIdGet200Response(
                id = 161072,
                name = 'SID Architecture',
                abbreviated_name = 'PE',
                address = '846 Dogglesworth Drive',
                attachments = [
                    procore_sdk.models.normal_view_attachments_inner.normal_view_attachments_inner(
                        id = 5324, 
                        url = 'http://www.example.com/', 
                        name = 'january_receipt_copy.jpg', 
                        filename = 'january_receipt_copy.jpg', )
                    ],
                authorized_bidder = True,
                business_id = 12345,
                business_phone = '(812) 989-9810',
                business_register = {"id":321,"type":"abn","identifier":"51824753556","verified_at":"2018-06-11T15:56:25Z","verification_status":"active"},
                city = 'Jeffersonville',
                contact_count = 5,
                company = 'Stock Construction',
                country_code = 'US',
                created_at = '2016-10-23T21:39:40Z',
                email_address = 'jane.doe@example.com',
                fax_number = '(812) 989-9810',
                is_active = True,
                is_connected = False,
                labor_union = 'IWW 872',
                license_number = '1901XYZ',
                logo = 'https://s3.amazonaws.com/pro-core.com/prostore/20160718141208_development_528209843.jpeg?AWSAccessKeyId=AKIAJ5EH2SRCJA6V2DKA&Expires=2100028332&Signature=pjM0nzUOxNrtjM2F0oTG2dbkPa8%3D',
                mobile_phone = '(812) 989-9810',
                non_union_prevailing_wage = False,
                notes = 'owned by a dog',
                origin_code = 'foobar',
                origin_data = 'OD-2398273424',
                origin_id = 'foobar',
                prequalified = False,
                primary_contact = {"id":1306796,"first_name":"John","last_name":"Doe","business_phone":"5555555555","business_phone_extension":123,"fax_number":"5555555555","mobile_phone":"5555555555","email_address":"john.doe@example.com","created_at":"2016-10-23T21:39:40Z","updated_at":"2016-10-23T21:39:40Z"},
                state_code = 'IN',
                synced_to_erp = False,
                trade_name = 'Woofer Electric',
                union_member = False,
                updated_at = '2016-10-23T21:39:40Z',
                vendor_group = {"id":1,"name":"Otis Elevators"},
                website = 'http://poodleparade.com',
                zip = '47130',
                origin_custom_fields = [
                    ''
                    ],
                erp_custom_fields = [
                    ''
                    ],
                bidding = procore_sdk.models.rest_v10_vendors_id_get_200_response_one_of_1_all_of_bidding.RestV10VendorsIdGet_200_response_oneOf_1_allOf_bidding(
                    affirmative_action = False, 
                    african_american_business = False, 
                    asian_american_business = False, 
                    certified_business_enterprise = False, 
                    disadvantaged_business = False, 
                    eight_a_business = False, 
                    hispanic_business = False, 
                    historically_underutilized_business = False, 
                    minority_business_enterprise = False, 
                    native_american_business = False, 
                    sdvo_business = False, 
                    small_business = False, 
                    womens_business = False, ),
                bidding_distribution = [
                    null
                    ],
                children_count = 0,
                company_vendor = False,
                legal_name = '1st Choice Glass Inc.',
                parent = {"id":634512,"name":"Poodle Electric Inc."},
                project_ids = [
                    56
                    ],
                standard_cost_codes = [
                    null
                    ],
                trades = [
                    procore_sdk.models.trade.Trade(
                        id = 999, 
                        name = '09 - acoustical panels', 
                        active = True, 
                        updated_at = '2016-08-01T23:33:54Z', )
                    ],
                business = procore_sdk.models.rest_v10_vendors_id_get_200_response_one_of_1_all_of_business.RestV10VendorsIdGet_200_response_oneOf_1_allOf_business(
                    id = '245acd0d-a3e1-4b8d-8891-7fdc364910ec', 
                    name = 'Test Company, Inc.', 
                    dba = 'Test Company', 
                    logo_url = 'https://s3.amazonaws.com/pro-core.com/prostore/20160718141208_development_528209843.jpeg?AWSAccessKeyId=AKIAJ5EH2SRCJA6V2DKA&Expires=2100028332&Signature=pjM0nzUOxNrtjM2F0oTG2dbkPa8%3D', 
                    primary_slug = 'test-company-carpinteria', 
                    construction_sectors = [
                        'industrial_and_energy'
                        ], 
                    business_types = [
                        'general_contractor'
                        ], 
                    provided_services = [
                        procore_sdk.models.business__normal_view__provided_services_inner.Business__Normal_View__provided_services_inner(
                            id = '245acd0d-a3e1-4b8d-8891-7fdc364910ec', 
                            key = 'existing_material_assessment', 
                            path = 'professional_and_business_services#assessments_and_studies#existing_material_assessment', 
                            level = 'specialty', )
                        ], 
                    avg_contract_size = procore_sdk.models.rest_v10_vendors_id_get_200_response_one_of_1_all_of_business_avg_contract_size.RestV10VendorsIdGet_200_response_oneOf_1_allOf_business_avg_contract_size(
                        start = 100000, 
                        end = 500000, ), 
                    company_size = procore_sdk.models.rest_v10_vendors_id_get_200_response_one_of_1_all_of_business_company_size.RestV10VendorsIdGet_200_response_oneOf_1_allOf_business_company_size(
                        start = 100000, 
                        end = 500000, ), ),
                contract_signer = procore_sdk.models.rest_v10_vendors_id_get_200_response_one_of_1_all_of_contract_signer.RestV10VendorsIdGet_200_response_oneOf_1_allOf_contract_signer(
                    id = 161024, 
                    company_name = '1st Choice Glass', 
                    contact_id = 334268, 
                    is_active = True, 
                    login = 'jon.doe@example.com', 
                    name = 'Jon Doe', ),
                country_name = 'United States of America',
                state_name = 'Berat',
                invoice_contacts = [
                    procore_sdk.models.rest_v10_vendors_id_get_200_response_one_of_1_all_of_invoice_contacts_inner.RestV10VendorsIdGet_200_response_oneOf_1_allOf_invoice_contacts_inner(
                        id = 1128828, 
                        name = 'A-1 Electric Company', )
                    ],
                active_users_count = 12345,
                bids_count = 12345,
                open_bids_count = 12345,
                projects_count = 12345
            )
        else:
            return RestV10VendorsIdGet200Response(
        )
        """

    def testRestV10VendorsIdGet200Response(self):
        """Test RestV10VendorsIdGet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
