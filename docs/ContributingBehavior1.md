# ContributingBehavior1


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
from procore_sdk.models.contributing_behavior1 import ContributingBehavior1

# TODO update the JSON string below
json = "{}"
# create an instance of ContributingBehavior1 from a JSON string
contributing_behavior1_instance = ContributingBehavior1.from_json(json)
# print the JSON string representation of the object
print(ContributingBehavior1.to_json())

# convert the object into a dict
contributing_behavior1_dict = contributing_behavior1_instance.to_dict()
# create an instance of ContributingBehavior1 from a dict
contributing_behavior1_from_dict = ContributingBehavior1.from_dict(contributing_behavior1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


