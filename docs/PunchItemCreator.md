# PunchItemCreator

User that created the Punch Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID | [optional] 
**name** | **str** | User Name | [optional] 
**login** | **str** | User Email | [optional] 

## Example

```python
from procore_sdk.models.punch_item_creator import PunchItemCreator

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItemCreator from a JSON string
punch_item_creator_instance = PunchItemCreator.from_json(json)
# print the JSON string representation of the object
print(PunchItemCreator.to_json())

# convert the object into a dict
punch_item_creator_dict = punch_item_creator_instance.to_dict()
# create an instance of PunchItemCreator from a dict
punch_item_creator_from_dict = PunchItemCreator.from_dict(punch_item_creator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


