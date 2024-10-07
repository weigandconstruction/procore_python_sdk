# RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the Invoice Configuration | [optional] 
**separate_billing_for_stored_materials** | **bool** | Whether billing for materials separately from the work complete is allowed | [optional] 
**stored_materials_billing_method** | **str** | Billing method for stored materials | [optional] 
**contract_id** | **int** | Contract ID | [optional] 
**project_id** | **int** | Project ID | [optional] 
**company_id** | **int** | Company ID | [optional] 
**ssr_enabled** | **bool** | Sliding Scale Retainage Enabled | [optional] 
**move_materials_to_previous_work_completed** | **bool** | True if the Project Invoice Configuration is set to move materials to previous work completed | [optional] 
**retainage_rule_set** | [**RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSet**](RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200ResponseRetainageRuleSet.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response import RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200Response from a JSON string
rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response_instance = RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response_dict = rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200Response from a dict
rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response_from_dict = RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationGet200Response.from_dict(rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


