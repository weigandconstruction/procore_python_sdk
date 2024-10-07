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

from procore_sdk.models.rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response_retainage_rule_set_retainage_rules_inner import RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner

class TestRestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner(unittest.TestCase):
    """RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner:
        """Test RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner`
        """
        model = RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner()
        if include_optional:
            return RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner(
                id = 12345,
                max_retainage = '1000.0',
                position = 1,
                retainage_percentage = '10.0',
                rule_type = '%_original_contract_value',
                rule_type_upper_limit = '5.0'
            )
        else:
            return RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner(
        )
        """

    def testRestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner(self):
        """Test RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
