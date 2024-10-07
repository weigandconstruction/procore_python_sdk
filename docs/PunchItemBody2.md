# PunchItemBody2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Project ID to which the Punch Item belongs to | 
**punch_item** | [**PunchItem4**](PunchItem4.md) |  | 

## Example

```python
from procore_sdk.models.punch_item_body2 import PunchItemBody2

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItemBody2 from a JSON string
punch_item_body2_instance = PunchItemBody2.from_json(json)
# print the JSON string representation of the object
print(PunchItemBody2.to_json())

# convert the object into a dict
punch_item_body2_dict = punch_item_body2_instance.to_dict()
# create an instance of PunchItemBody2 from a dict
punch_item_body2_from_dict = PunchItemBody2.from_dict(punch_item_body2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


