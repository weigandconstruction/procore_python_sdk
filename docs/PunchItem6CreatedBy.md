# PunchItem6CreatedBy

Login Information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Login Information ID | [optional] 
**name** | **str** | User name | [optional] 
**login** | **str** | User email | [optional] 

## Example

```python
from procore_sdk.models.punch_item6_created_by import PunchItem6CreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of PunchItem6CreatedBy from a JSON string
punch_item6_created_by_instance = PunchItem6CreatedBy.from_json(json)
# print the JSON string representation of the object
print(PunchItem6CreatedBy.to_json())

# convert the object into a dict
punch_item6_created_by_dict = punch_item6_created_by_instance.to_dict()
# create an instance of PunchItem6CreatedBy from a dict
punch_item6_created_by_from_dict = PunchItem6CreatedBy.from_dict(punch_item6_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


