# RestV10WorkOrderContractsPost201ResponseInvoiceContactsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**business_phone** | **str** |  | [optional] 
**business_phone_extension** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**fax_number** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**login_information_id** | **int** |  | [optional] 
**mobile_phone** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**vendor_name** | **str** |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_invoice_contacts_inner import RestV10WorkOrderContractsPost201ResponseInvoiceContactsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkOrderContractsPost201ResponseInvoiceContactsInner from a JSON string
rest_v10_work_order_contracts_post201_response_invoice_contacts_inner_instance = RestV10WorkOrderContractsPost201ResponseInvoiceContactsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkOrderContractsPost201ResponseInvoiceContactsInner.to_json())

# convert the object into a dict
rest_v10_work_order_contracts_post201_response_invoice_contacts_inner_dict = rest_v10_work_order_contracts_post201_response_invoice_contacts_inner_instance.to_dict()
# create an instance of RestV10WorkOrderContractsPost201ResponseInvoiceContactsInner from a dict
rest_v10_work_order_contracts_post201_response_invoice_contacts_inner_from_dict = RestV10WorkOrderContractsPost201ResponseInvoiceContactsInner.from_dict(rest_v10_work_order_contracts_post201_response_invoice_contacts_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


