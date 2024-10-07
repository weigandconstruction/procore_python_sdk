# PunchItemType1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Punch Item Type ID | [optional] 
**name** | **str** | Punch Item Type name | [optional] 
**created_at** | **datetime** | Punch Item Type created at | [optional] 
**updated_at** | **datetime** | Punch Item Type last updated at | [optional] 

## Example

```python
from procore_sdk.models.punch_item_type1 import PunchItemType1

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItemType1 from a JSON string
punch_item_type1_instance = PunchItemType1.from_json(json)
# print the JSON string representation of the object
print(PunchItemType1.to_json())

# convert the object into a dict
punch_item_type1_dict = punch_item_type1_instance.to_dict()
# create an instance of PunchItemType1 from a dict
punch_item_type1_from_dict = PunchItemType1.from_dict(punch_item_type1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


