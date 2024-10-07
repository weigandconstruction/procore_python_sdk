# PunchItemBody6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Project ID to which the Punch Item belongs to | 
**punch_item** | [**PunchItem9**](PunchItem9.md) |  | 

## Example

```python
from procore_sdk.models.punch_item_body6 import PunchItemBody6

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItemBody6 from a JSON string
punch_item_body6_instance = PunchItemBody6.from_json(json)
# print the JSON string representation of the object
print(PunchItemBody6.to_json())

# convert the object into a dict
punch_item_body6_dict = punch_item_body6_instance.to_dict()
# create an instance of PunchItemBody6 from a dict
punch_item_body6_from_dict = PunchItemBody6.from_dict(punch_item_body6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


