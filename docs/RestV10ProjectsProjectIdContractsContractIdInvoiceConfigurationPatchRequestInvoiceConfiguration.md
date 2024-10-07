# RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationPatchRequestInvoiceConfiguration

Invoice Configuration for the Contract

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**separate_billing_for_stored_materials** | **bool** | Whether billing for materials separately from the work complete is allowed | [optional] 
**stored_materials_billing_method** | **str** | Billing method for stored materials | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_patch_request_invoice_configuration import RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationPatchRequestInvoiceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationPatchRequestInvoiceConfiguration from a JSON string
rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_patch_request_invoice_configuration_instance = RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationPatchRequestInvoiceConfiguration.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationPatchRequestInvoiceConfiguration.to_json())

# convert the object into a dict
rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_patch_request_invoice_configuration_dict = rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_patch_request_invoice_configuration_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationPatchRequestInvoiceConfiguration from a dict
rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_patch_request_invoice_configuration_from_dict = RestV10ProjectsProjectIdContractsContractIdInvoiceConfigurationPatchRequestInvoiceConfiguration.from_dict(rest_v10_projects_project_id_contracts_contract_id_invoice_configuration_patch_request_invoice_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


