# RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSet

A set of rules to control how retainage is applied to invoices of a contract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique integer ID | [optional] 
**contract_id** | **int** | Integer ID for the associated Contract | [optional] 
**name** | **str** | The Name of the Retainage Rule Set | [optional] 
**retainage_rules** | [**List[RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner]**](RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response_retainage_rule_set import RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSet

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSet from a JSON string
rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response_retainage_rule_set_instance = RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSet.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSet.to_json())

# convert the object into a dict
rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response_retainage_rule_set_dict = rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response_retainage_rule_set_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSet from a dict
rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response_retainage_rule_set_from_dict = RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSet.from_dict(rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response_retainage_rule_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


