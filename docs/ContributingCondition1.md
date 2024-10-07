# ContributingCondition1


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
from procore_sdk.models.contributing_condition1 import ContributingCondition1

# TODO update the JSON string below
json = "{}"
# create an instance of ContributingCondition1 from a JSON string
contributing_condition1_instance = ContributingCondition1.from_json(json)
# print the JSON string representation of the object
print(ContributingCondition1.to_json())

# convert the object into a dict
contributing_condition1_dict = contributing_condition1_instance.to_dict()
# create an instance of ContributingCondition1 from a dict
contributing_condition1_from_dict = ContributingCondition1.from_dict(contributing_condition1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


