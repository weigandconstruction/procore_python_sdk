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

from procore_sdk.models.rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get200_response_base_bid_inner_sub_sections_inner import RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerSubSectionsInner

class TestRestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerSubSectionsInner(unittest.TestCase):
    """RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerSubSectionsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerSubSectionsInner:
        """Test RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerSubSectionsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerSubSectionsInner`
        """
        model = RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerSubSectionsInner()
        if include_optional:
            return RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerSubSectionsInner(
                id = 1234,
                title = 'Floors 10-19',
                position = 1,
                bid_form_items = [
                    procore_sdk.models.rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get_200_response_base_bid_inner_bid_form_items_inner.RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet_200_response_base_bid_inner_bid_form_items_inner(
                        id = 18, 
                        cost_code = procore_sdk.models.rest_v10_companies_company_id_bid_bid_id_bid_forms_bid_form_id_get_200_response_base_bid_inner_bid_form_items_inner_cost_code.RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet_200_response_base_bid_inner_bid_form_items_inner_cost_code(
                            id = 2, 
                            name = 'Concrete', 
                            full_code = '2 - Concrete', ), 
                        description = 'Wood Doors', 
                        position = 1, 
                        subject = 'Is the insurance of tools included in the Bid?', 
                        item_type = 'cost_code', 
                        response_type = 'amount', )
                    ]
            )
        else:
            return RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerSubSectionsInner(
        )
        """

    def testRestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerSubSectionsInner(self):
        """Test RestV10CompaniesCompanyIdBidBidIdBidFormsBidFormIdGet200ResponseBaseBidInnerSubSectionsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
