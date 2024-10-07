# ActionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Incident Action Type ID | [optional] 
**name** | **str** | Incident Action Type Name | [optional] 
**active** | **bool** | Represents whether an Incident Action Type is available for use. | [optional] 
**var_global** | **bool** | Represents whether an Incident Action Type has been provided by Procore. | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.action_type import ActionType

# TODO update the JSON string below
json = "{}"
# create an instance of ActionType from a JSON string
action_type_instance = ActionType.from_json(json)
# print the JSON string representation of the object
print(ActionType.to_json())

# convert the object into a dict
action_type_dict = action_type_instance.to_dict()
# create an instance of ActionType from a dict
action_type_from_dict = ActionType.from_dict(action_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


