# RestV10ChangeOrderPackagesPost201ResponseLineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**position** | **int** | Position | [optional] 
**description** | **str** | Description | [optional] 
**quantity** | **float** | Quantity | [optional] 
**uom** | **str** | Unit of measurement | [optional] 
**total_amount** | **float** | Total amount | [optional] 
**extended_amount** | **float** | Extended amount | [optional] 
**cost_code** | [**RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerCostCode**](RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerCostCode.md) |  | [optional] 
**wbs_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode.md) |  | [optional] 
**unit_cost** | **float** | Unit cost | [optional] 
**holder** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerHolder**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerHolder.md) |  | [optional] 
**line_item_type** | [**LineItemType3**](LineItemType3.md) |  | [optional] 
**markup_line_items** | [**List[RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerMarkupLineItemsInner]**](RestV10ChangeOrderPackagesPost201ResponseLineItemsInnerMarkupLineItemsInner.md) |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_change_order_packages_post201_response_line_items_inner import RestV10ChangeOrderPackagesPost201ResponseLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeOrderPackagesPost201ResponseLineItemsInner from a JSON string
rest_v10_change_order_packages_post201_response_line_items_inner_instance = RestV10ChangeOrderPackagesPost201ResponseLineItemsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeOrderPackagesPost201ResponseLineItemsInner.to_json())

# convert the object into a dict
rest_v10_change_order_packages_post201_response_line_items_inner_dict = rest_v10_change_order_packages_post201_response_line_items_inner_instance.to_dict()
# create an instance of RestV10ChangeOrderPackagesPost201ResponseLineItemsInner from a dict
rest_v10_change_order_packages_post201_response_line_items_inner_from_dict = RestV10ChangeOrderPackagesPost201ResponseLineItemsInner.from_dict(rest_v10_change_order_packages_post201_response_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


