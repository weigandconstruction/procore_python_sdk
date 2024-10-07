# PunchItemManager

User that manages the Punch Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID | [optional] 
**name** | **str** | User Name | [optional] 
**login** | **str** | User Email | [optional] 

## Example

```python
from procore_sdk.models.punch_item_manager import PunchItemManager

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItemManager from a JSON string
punch_item_manager_instance = PunchItemManager.from_json(json)
# print the JSON string representation of the object
print(PunchItemManager.to_json())

# convert the object into a dict
punch_item_manager_dict = punch_item_manager_instance.to_dict()
# create an instance of PunchItemManager from a dict
punch_item_manager_from_dict = PunchItemManager.from_dict(punch_item_manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


