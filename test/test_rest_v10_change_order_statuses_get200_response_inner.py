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

from procore_sdk.models.rest_v10_change_order_statuses_get200_response_inner import RestV10ChangeOrderStatusesGet200ResponseInner

class TestRestV10ChangeOrderStatusesGet200ResponseInner(unittest.TestCase):
    """RestV10ChangeOrderStatusesGet200ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ChangeOrderStatusesGet200ResponseInner:
        """Test RestV10ChangeOrderStatusesGet200ResponseInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ChangeOrderStatusesGet200ResponseInner`
        """
        model = RestV10ChangeOrderStatusesGet200ResponseInner()
        if include_optional:
            return RestV10ChangeOrderStatusesGet200ResponseInner(
                id = 324737,
                name = 'No Charge',
                mapped_to_status = 'approved',
                show_in_select = True
            )
        else:
            return RestV10ChangeOrderStatusesGet200ResponseInner(
        )
        """

    def testRestV10ChangeOrderStatusesGet200ResponseInner(self):
        """Test RestV10ChangeOrderStatusesGet200ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
