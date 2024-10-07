# PunchItemBody4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Project ID to which the Punch Item belongs to | 
**punch_item** | [**PunchItem7**](PunchItem7.md) |  | 

## Example

```python
from procore_sdk.models.punch_item_body4 import PunchItemBody4

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItemBody4 from a JSON string
punch_item_body4_instance = PunchItemBody4.from_json(json)
# print the JSON string representation of the object
print(PunchItemBody4.to_json())

# convert the object into a dict
punch_item_body4_dict = punch_item_body4_instance.to_dict()
# create an instance of PunchItemBody4 from a dict
punch_item_body4_from_dict = PunchItemBody4.from_dict(punch_item_body4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


