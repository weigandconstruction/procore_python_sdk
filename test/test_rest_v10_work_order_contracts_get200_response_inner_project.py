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

from procore_sdk.models.rest_v10_work_order_contracts_get200_response_inner_project import RestV10WorkOrderContractsGet200ResponseInnerProject

class TestRestV10WorkOrderContractsGet200ResponseInnerProject(unittest.TestCase):
    """RestV10WorkOrderContractsGet200ResponseInnerProject unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10WorkOrderContractsGet200ResponseInnerProject:
        """Test RestV10WorkOrderContractsGet200ResponseInnerProject
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10WorkOrderContractsGet200ResponseInnerProject`
        """
        model = RestV10WorkOrderContractsGet200ResponseInnerProject()
        if include_optional:
            return RestV10WorkOrderContractsGet200ResponseInnerProject(
                id = 123456,
                name = 'Children's Hospital'
            )
        else:
            return RestV10WorkOrderContractsGet200ResponseInnerProject(
        )
        """

    def testRestV10WorkOrderContractsGet200ResponseInnerProject(self):
        """Test RestV10WorkOrderContractsGet200ResponseInnerProject"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
