# PunchItemBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Project ID to which the Punch Item belongs to | 
**punch_item** | [**PunchItem1**](PunchItem1.md) |  | 

## Example

```python
from procore_sdk.models.punch_item_body import PunchItemBody

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItemBody from a JSON string
punch_item_body_instance = PunchItemBody.from_json(json)
# print the JSON string representation of the object
print(PunchItemBody.to_json())

# convert the object into a dict
punch_item_body_dict = punch_item_body_instance.to_dict()
# create an instance of PunchItemBody from a dict
punch_item_body_from_dict = PunchItemBody.from_dict(punch_item_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


