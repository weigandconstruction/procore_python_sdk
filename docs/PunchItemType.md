# PunchItemType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 

## Example

```python
from procore_sdk.models.punch_item_type import PunchItemType

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItemType from a JSON string
punch_item_type_instance = PunchItemType.from_json(json)
# print the JSON string representation of the object
print(PunchItemType.to_json())

# convert the object into a dict
punch_item_type_dict = punch_item_type_instance.to_dict()
# create an instance of PunchItemType from a dict
punch_item_type_from_dict = PunchItemType.from_dict(punch_item_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


