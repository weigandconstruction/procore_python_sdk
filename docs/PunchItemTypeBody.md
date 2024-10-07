# PunchItemTypeBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Punch Item Type belongs to | 
**punch_item_type** | [**PunchItemType2**](PunchItemType2.md) |  | 

## Example

```python
from procore_sdk.models.punch_item_type_body import PunchItemTypeBody

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItemTypeBody from a JSON string
punch_item_type_body_instance = PunchItemTypeBody.from_json(json)
# print the JSON string representation of the object
print(PunchItemTypeBody.to_json())

# convert the object into a dict
punch_item_type_body_dict = punch_item_type_body_instance.to_dict()
# create an instance of PunchItemTypeBody from a dict
punch_item_type_body_from_dict = PunchItemTypeBody.from_dict(punch_item_type_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


