# Extended1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**biller** | **str** | Biller | [optional] 
**biller_id** | **int** | Biller ID | [optional] 
**biller_type** | **str** | Biller type | [optional] 
**biller_origin_id** | **str** | Biller Origin Id | [optional] 
**budgeted** | **bool** | Budgeted | [optional] 
**code** | **str** | Cost code, not including parent prefix | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**full_code** | **str** | Full Cost code, including parent prefixes | [optional] 
**name** | **str** | Name | [optional] 
**origin_data** | **str** | Cost Code third party data | [optional] 
**origin_id** | **str** | Cost Code third party id | [optional] 
**parent** | [**Extended1Parent**](Extended1Parent.md) |  | [optional] 
**position** | **int** | Position | [optional] 
**sortable_code** | **str** | Sortable code (this property is deprecated - see full_code) | [optional] 
**standard_cost_code_id** | **int** | Standard Cost Code ID | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**line_item_types** | [**List[LineItemType]**](LineItemType.md) | Line Item Types | [optional] 

## Example

```python
from procore_sdk.models.extended1 import Extended1

# TODO update the JSON string below
json = "{}"
# create an instance of Extended1 from a JSON string
extended1_instance = Extended1.from_json(json)
# print the JSON string representation of the object
print(Extended1.to_json())

# convert the object into a dict
extended1_dict = extended1_instance.to_dict()
# create an instance of Extended1 from a dict
extended1_from_dict = Extended1.from_dict(extended1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


