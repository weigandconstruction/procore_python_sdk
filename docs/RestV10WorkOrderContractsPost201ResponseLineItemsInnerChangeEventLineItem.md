# RestV10WorkOrderContractsPost201ResponseLineItemsInnerChangeEventLineItem

Change Event Line Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Change Event Line Item ID | [optional] 
**cost_rom** | **float** | Change Event Line Item Cost ROM | [optional] 
**revenue_rom** | **float** | Change Event Line Item Revenue ROM | [optional] 
**event_id** | **int** | Change Event ID | [optional] 
**cost_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode.md) |  | [optional] 
**line_item_type** | [**LineItemType**](LineItemType.md) |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_line_items_inner_change_event_line_item import RestV10WorkOrderContractsPost201ResponseLineItemsInnerChangeEventLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkOrderContractsPost201ResponseLineItemsInnerChangeEventLineItem from a JSON string
rest_v10_work_order_contracts_post201_response_line_items_inner_change_event_line_item_instance = RestV10WorkOrderContractsPost201ResponseLineItemsInnerChangeEventLineItem.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkOrderContractsPost201ResponseLineItemsInnerChangeEventLineItem.to_json())

# convert the object into a dict
rest_v10_work_order_contracts_post201_response_line_items_inner_change_event_line_item_dict = rest_v10_work_order_contracts_post201_response_line_items_inner_change_event_line_item_instance.to_dict()
# create an instance of RestV10WorkOrderContractsPost201ResponseLineItemsInnerChangeEventLineItem from a dict
rest_v10_work_order_contracts_post201_response_line_items_inner_change_event_line_item_from_dict = RestV10WorkOrderContractsPost201ResponseLineItemsInnerChangeEventLineItem.from_dict(rest_v10_work_order_contracts_post201_response_line_items_inner_change_event_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


