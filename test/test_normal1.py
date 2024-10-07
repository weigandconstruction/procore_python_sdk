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

from procore_sdk.models.normal1 import Normal1

class TestNormal1(unittest.TestCase):
    """Normal1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Normal1:
        """Test Normal1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Normal1`
        """
        model = Normal1()
        if include_optional:
            return Normal1(
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
                contact_count = 5,
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
            return Normal1(
        )
        """

    def testNormal1(self):
        """Test Normal1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
