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

from procore_sdk.models.rest_v11_projects_project_id_vendors_get200_response_inner_one_of import RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf

class TestRestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf(unittest.TestCase):
    """RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf:
        """Test RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf`
        """
        model = RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf()
        if include_optional:
            return RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf(
                bidding = {"affirmative_action":false,"small_business":false,"african_american_business":true,"hispanic_business":false,"womens_business":false,"historically_underutilized_business":false,"sdvo_business":false,"certified_business_enterprise":true,"asian_american_business":false,"native_american_business":true,"disadvantaged_business":false,"minority_business_enterprise":false,"eight_a_business":true},
                bidding_distribution = [
                    null
                    ],
                business = procore_sdk.models.business_(normal_view).Business (Normal View)(
                    id = '2975a9c3-f28b-4eb6-a29a-2332e73b3ad7', 
                    name = 'Test Company, Inc.', 
                    dba = 'Test Company', 
                    website = 'www.testcompanyinc.com', 
                    about = 'The best test company around.', 
                    published = True, 
                    primary_slug = 'test-company-carpinteria', 
                    logo_url = 'www.storage.com/company_logo.png', 
                    source = procore_sdk.models.business__normal_view__source.Business__Normal_View__source(
                        id = 'm7pn7civb73iwijcm7wxxpaxniejvyo2', 
                        type = 'SNOWFLAKE', 
                        record_type = 'Typeform', ), 
                    addresses = [
                        procore_sdk.models.business__normal_view__addresses_inner.Business__Normal_View__addresses_inner(
                            id = '2975a9c3-f28b-4eb6-a29a-2332e73b3ad7', 
                            name = 'Main Office', 
                            address1 = '6309 Carpinteria Ave', 
                            address2 = 'Suite 100', 
                            city = 'Carpinteria', 
                            latitude = 42.39996, 
                            longitude = -84.35104, 
                            province = 'CA', 
                            postal_code1 = '93013', 
                            country_code = 'US', 
                            phone_number = '+1-517-936-7923', 
                            fax_number = '+1-517-936-7923', 
                            primary = True, 
                            address_types = [
                                'office'
                                ], )
                        ], 
                    provided_services = [
                        procore_sdk.models.business__normal_view__provided_services_inner.Business__Normal_View__provided_services_inner(
                            id = '245acd0d-a3e1-4b8d-8891-7fdc364910ec', 
                            key = 'existing_material_assessment', 
                            path = 'professional_and_business_services#assessments_and_studies#existing_material_assessment', 
                            level = 'specialty', )
                        ], 
                    construction_sectors = [
                        'industrial_and_energy'
                        ], 
                    business_types = [
                        'general_contractor'
                        ], 
                    project_types = [
                        'seaport'
                        ], 
                    classifications = [
                        procore_sdk.models.business__normal_view__classifications_inner.Business__Normal_View__classifications_inner(
                            abbreviation = 'SBE', 
                            key = 'SBE', 
                            name = 'Small Business', )
                        ], 
                    coverage_areas = [
                        procore_sdk.models.business__normal_view__coverage_areas_inner.Business__Normal_View__coverage_areas_inner(
                            country_code = 'US', 
                            google_place_id = 'ChIJL4iEQEoS6YAR04viVA12TNw', 
                            admin1 = 'CA', 
                            admin2 = 'Orange County', 
                            admin3 = '', 
                            admin4 = '', 
                            locality = 'Anaheim Hills', 
                            selected_level = 'locality', )
                        ], 
                    claimed = True, 
                    tags = procore_sdk.models.business__normal_view__tags.Business__Normal_View__Tags(
                        claim_status = 'PENDING', 
                        approval_status = 'PENDING', 
                        publishable = 'true', ), 
                    start_of_operations = 'Tue Oct 24 00:00:00 UTC 2023', ),
                children_count = 0,
                legal_name = 'Stock Construction',
                company_vendor = False,
                parent = {"id":634512,"name":"Poodle Electric Inc."},
                trades = [
                    procore_sdk.models.trade.Trade(
                        id = 999, 
                        name = '09 - acoustical panels', 
                        active = True, 
                        updated_at = '2016-08-01T23:33:54Z', )
                    ],
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
                business_id = '89cac92d-fbd8-40ec-a1fc-24bbbd035a78',
                business_phone = '(812) 989-9810',
                business_register = {"id":321,"type":"abn","identifier":"51824753556","verified_at":"2018-06-11T15:56:25Z","verification_status":"active"},
                city = 'Jeffersonville',
                company = 'Stock Construction',
                country_code = 'US',
                created_at = '2016-10-23T21:39:40Z',
                email_address = 'jane.doe@example.com',
                fax_number = '(812) 989-9810',
                is_active = True,
                is_connected = True,
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
                project_ids = [
                    12
                    ],
                state_code = 'IN',
                synced_to_erp = False,
                trade_name = 'Woofer Electric',
                union_member = False,
                updated_at = '2016-10-23T21:39:40Z',
                vendor_group = {"id":1,"name":"Otis Elevators"},
                website = 'http://poodleparade.com',
                zip = '47130'
            )
        else:
            return RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf(
        )
        """

    def testRestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf(self):
        """Test RestV11ProjectsProjectIdVendorsGet200ResponseInnerOneOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
