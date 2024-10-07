# WorkClassification

Work Classification Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the classification | [optional] 
**abbreviation** | **str** | The shortened form of classification | [optional] 
**is_active** | **bool** | Is the classification active or not | [optional] 

## Example

```python
from procore_sdk.models.work_classification import WorkClassification

# TODO update the JSON string below
json = "{}"
# create an instance of WorkClassification from a JSON string
work_classification_instance = WorkClassification.from_json(json)
# print the JSON string representation of the object
print(WorkClassification.to_json())

# convert the object into a dict
work_classification_dict = work_classification_instance.to_dict()
# create an instance of WorkClassification from a dict
work_classification_from_dict = WorkClassification.from_dict(work_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


