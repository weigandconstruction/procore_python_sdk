# DirectCostLineItem1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Line Item id | [optional] 
**amount** | **str** | Line Item amount | [optional] 
**company** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany.md) |  | [optional] 
**cost_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode.md) |  | [optional] 
**created_at** | **datetime** | Created at date and time | [optional] 
**currency_configuration** | [**DirectCostLineItem1CurrencyConfiguration**](DirectCostLineItem1CurrencyConfiguration.md) |  | [optional] 
**description** | **str** | Line Item description | [optional] 
**extended_type** | **str** | Line Item extended type | [optional] 
**line_item_type** | [**LineItemType**](LineItemType.md) |  | [optional] 
**origin_data** | **str** | Line Item third party data | [optional] 
**origin_id** | **str** | Line Item third party id | [optional] 
**position** | **int** | Line Item position | [optional] 
**quantity** | **float** | Line Item quantity | [optional] 
**tax_code_id** | **int** | Tax Code ID | [optional] 
**total_amount** | **float** | Line Item total amount | [optional] 
**extended_amount** | **float** | Line Item extended amount | [optional] 
**unit_cost** | **float** | Line Item unit cost | [optional] 
**uom** | **str** | Line Item units of measure | [optional] 
**updated_at** | **datetime** | Updated at date and time | [optional] 
**wbs_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode.md) |  | [optional] 
**ref** | **str** | The reference, if any, passed in upon item creation and is not persisted. | [optional] 

## Example

```python
from procore_sdk.models.direct_cost_line_item1 import DirectCostLineItem1

# TODO update the JSON string below
json = "{}"
# create an instance of DirectCostLineItem1 from a JSON string
direct_cost_line_item1_instance = DirectCostLineItem1.from_json(json)
# print the JSON string representation of the object
print(DirectCostLineItem1.to_json())

# convert the object into a dict
direct_cost_line_item1_dict = direct_cost_line_item1_instance.to_dict()
# create an instance of DirectCostLineItem1 from a dict
direct_cost_line_item1_from_dict = DirectCostLineItem1.from_dict(direct_cost_line_item1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


