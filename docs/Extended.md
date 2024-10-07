# Extended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**biller** | **str** | Biller | [optional] 
**biller_id** | **int** | Biller ID | [optional] 
**biller_type** | **str** | Biller type | [optional] 
**budgeted** | **bool** | Budgeted | [optional] 
**code** | **str** | Cost code, not including parent prefix | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**full_code** | **str** | Full Cost code, including parent prefixes | [optional] 
**name** | **str** | Name | [optional] 
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
from procore_sdk.models.extended import Extended

# TODO update the JSON string below
json = "{}"
# create an instance of Extended from a JSON string
extended_instance = Extended.from_json(json)
# print the JSON string representation of the object
print(Extended.to_json())

# convert the object into a dict
extended_dict = extended_instance.to_dict()
# create an instance of Extended from a dict
extended_from_dict = Extended.from_dict(extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


