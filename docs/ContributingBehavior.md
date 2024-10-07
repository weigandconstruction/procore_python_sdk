# ContributingBehavior


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Contributing Behavior ID | [optional] 
**name** | **str** | Contributing Behavior Name | [optional] 
**active** | **bool** | Represents whether a Contributing Behavior is available for use. | [optional] 
**var_global** | **bool** | Represents whether a Contributing Behavior has been provided by Procore. | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.contributing_behavior import ContributingBehavior

# TODO update the JSON string below
json = "{}"
# create an instance of ContributingBehavior from a JSON string
contributing_behavior_instance = ContributingBehavior.from_json(json)
# print the JSON string representation of the object
print(ContributingBehavior.to_json())

# convert the object into a dict
contributing_behavior_dict = contributing_behavior_instance.to_dict()
# create an instance of ContributingBehavior from a dict
contributing_behavior_from_dict = ContributingBehavior.from_dict(contributing_behavior_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


