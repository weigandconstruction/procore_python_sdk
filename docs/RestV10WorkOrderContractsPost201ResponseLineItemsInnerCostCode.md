# RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**full_code** | **str** | Full Cost code, including parent prefixes | [optional] 
**name** | **str** | Name | [optional] 
**biller** | **str** | Biller | [optional] 
**biller_id** | **int** | Biller ID | [optional] 
**biller_type** | **str** | Biller type | [optional] 
**budgeted** | **bool** | Budgeted | [optional] 
**code** | **str** | Cost code, not including parent prefix | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**origin_data** | **str** | Cost Code third party data | [optional] 
**origin_id** | **str** | Cost Code third party id | [optional] 
**parent** | [**ExtendedParent**](ExtendedParent.md) |  | [optional] 
**position** | **int** | Position | [optional] 
**sortable_code** | **str** | Sortable code (this property is deprecated - see full_code) | [optional] 
**standard_cost_code_id** | **int** | Standard Cost Code ID | [optional] 
**standard_cost_code_list_id** | **int** | Standard Cost Code List ID | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**line_item_types** | [**List[LineItemType]**](LineItemType.md) | Line Item Types | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_line_items_inner_cost_code import RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode from a JSON string
rest_v10_work_order_contracts_post201_response_line_items_inner_cost_code_instance = RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode.to_json())

# convert the object into a dict
rest_v10_work_order_contracts_post201_response_line_items_inner_cost_code_dict = rest_v10_work_order_contracts_post201_response_line_items_inner_cost_code_instance.to_dict()
# create an instance of RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode from a dict
rest_v10_work_order_contracts_post201_response_line_items_inner_cost_code_from_dict = RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode.from_dict(rest_v10_work_order_contracts_post201_response_line_items_inner_cost_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


