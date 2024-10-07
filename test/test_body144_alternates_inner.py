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

from procore_sdk.models.body144_alternates_inner import Body144AlternatesInner

class TestBody144AlternatesInner(unittest.TestCase):
    """Body144AlternatesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Body144AlternatesInner:
        """Test Body144AlternatesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Body144AlternatesInner`
        """
        model = Body144AlternatesInner()
        if include_optional:
            return Body144AlternatesInner(
                title = 'Flooring',
                position = 1,
                header = True,
                bid_form_items = [
                    procore_sdk.models.body_144_base_bid_inner_bid_form_items_inner.Body_144_base_bid_inner_bid_form_items_inner(
                        id = 1235, 
                        cost_code_id = 1, 
                        description = 'Concrete', 
                        position = 1, 
                        subject = 'Is the insurance of tools included in the Bid?', 
                        item_type = 'cost_code', 
                        response_type = 'amount', )
                    ],
                sub_sections = [
                    procore_sdk.models.body_144_base_bid_inner_sub_sections_inner.Body_144_base_bid_inner_sub_sections_inner(
                        id = 1235, 
                        title = 'Floors 10-19', 
                        position = 1, 
                        bid_form_items = [
                            procore_sdk.models.body_143_base_bid_inner_bid_form_items_inner.Body_143_base_bid_inner_bid_form_items_inner(
                                cost_code_id = 1, 
                                description = 'Concrete', 
                                position = 1, 
                                subject = 'Is the insurance of tools included in the Bid?', 
                                item_type = 'cost_code', 
                                response_type = 'amount', )
                            ], )
                    ]
            )
        else:
            return Body144AlternatesInner(
        )
        """

    def testBody144AlternatesInner(self):
        """Test Body144AlternatesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
