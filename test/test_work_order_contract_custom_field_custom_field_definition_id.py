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

from procore_sdk.models.work_order_contract_custom_field_custom_field_definition_id import WorkOrderContractCustomFieldCustomFieldDefinitionId

class TestWorkOrderContractCustomFieldCustomFieldDefinitionId(unittest.TestCase):
    """WorkOrderContractCustomFieldCustomFieldDefinitionId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WorkOrderContractCustomFieldCustomFieldDefinitionId:
        """Test WorkOrderContractCustomFieldCustomFieldDefinitionId
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WorkOrderContractCustomFieldCustomFieldDefinitionId`
        """
        model = WorkOrderContractCustomFieldCustomFieldDefinitionId()
        if include_optional:
            return WorkOrderContractCustomFieldCustomFieldDefinitionId(
            )
        else:
            return WorkOrderContractCustomFieldCustomFieldDefinitionId(
        )
        """

    def testWorkOrderContractCustomFieldCustomFieldDefinitionId(self):
        """Test WorkOrderContractCustomFieldCustomFieldDefinitionId"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
