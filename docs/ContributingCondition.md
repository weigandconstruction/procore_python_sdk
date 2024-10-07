# ContributingCondition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Contributing Condition ID | [optional] 
**name** | **str** | Contributing Condition Name | [optional] 
**active** | **bool** | Represents whether a Contributing Condition is available for use. | [optional] 
**var_global** | **bool** | Represents whether a Contributing Condition has been provided by Procore. | [optional] 
**created_at** | **datetime** | Timestamp of creation | [optional] 
**updated_at** | **datetime** | Timestamp of last update | [optional] 

## Example

```python
from procore_sdk.models.contributing_condition import ContributingCondition

# TODO update the JSON string below
json = "{}"
# create an instance of ContributingCondition from a JSON string
contributing_condition_instance = ContributingCondition.from_json(json)
# print the JSON string representation of the object
print(ContributingCondition.to_json())

# convert the object into a dict
contributing_condition_dict = contributing_condition_instance.to_dict()
# create an instance of ContributingCondition from a dict
contributing_condition_from_dict = ContributingCondition.from_dict(contributing_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


