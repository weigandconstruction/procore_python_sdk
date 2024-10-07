# RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique integer ID | [optional] 
**max_retainage** | **str** | The maximum amount of retainage held before this rule no longer applies | [optional] 
**position** | **int** | The ordinal of this Rule within the containing Rule Set | [optional] 
**retainage_percentage** | **str** | The percentage of retaiange to withold on work completed while this Rule is active | [optional] 
**rule_type** | **str** | The property type used to calculate the max retainage for this Rule | [optional] 
**rule_type_upper_limit** | **str** | The amount used in conjunction with the Rule Type to detertmine the max retainage for this Rule | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response_retainage_rule_set_retainage_rules_inner import RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner from a JSON string
rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response_retainage_rule_set_retainage_rules_inner_instance = RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response_retainage_rule_set_retainage_rules_inner_dict = rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response_retainage_rule_set_retainage_rules_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner from a dict
rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response_retainage_rule_set_retainage_rules_inner_from_dict = RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSetRetainageRulesInner.from_dict(rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response_retainage_rule_set_retainage_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


