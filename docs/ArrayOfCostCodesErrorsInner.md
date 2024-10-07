# ArrayOfCostCodesErrorsInner


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
**errors** | [**RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseErrorsInnerAllOfErrors.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_cost_codes_errors_inner import ArrayOfCostCodesErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfCostCodesErrorsInner from a JSON string
array_of_cost_codes_errors_inner_instance = ArrayOfCostCodesErrorsInner.from_json(json)
# print the JSON string representation of the object
print(ArrayOfCostCodesErrorsInner.to_json())

# convert the object into a dict
array_of_cost_codes_errors_inner_dict = array_of_cost_codes_errors_inner_instance.to_dict()
# create an instance of ArrayOfCostCodesErrorsInner from a dict
array_of_cost_codes_errors_inner_from_dict = ArrayOfCostCodesErrorsInner.from_dict(array_of_cost_codes_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


