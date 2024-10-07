# RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Detail Line Item ID | [optional] 
**amount** | **str** | Detail Line Item amount | [optional] 
**description** | **str** | Detail Line Item description | [optional] 
**position** | **int** | Detail Line Item position | [optional] 
**line_item_id** | **int** | Line Item ID | [optional] 
**billed_to_date** | **str** | Detail Line Item actual billed amount | [optional] 
**billed_against** | **bool** | Has this line item ever been billed for a non-zero amount on a previous invoice | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 
**created_at** | **datetime** | Created at date and time | [optional] 
**updated_at** | **datetime** | Updated at date and time | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_post201_response import RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response from a JSON string
rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_post201_response_instance = RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response.to_json())

# convert the object into a dict
rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_post201_response_dict = rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_post201_response_instance.to_dict()
# create an instance of RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response from a dict
rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_post201_response_from_dict = RestV10WorkOrderContractsWorkOrderContractIdLineItemContractDetailsPost201Response.from_dict(rest_v10_work_order_contracts_work_order_contract_id_line_item_contract_details_post201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


