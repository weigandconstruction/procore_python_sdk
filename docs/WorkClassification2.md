# WorkClassification2

Work Classification Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the classification | [optional] 
**abbreviation** | **str** | The shortened form of classification | [optional] 

## Example

```python
from procore_sdk.models.work_classification2 import WorkClassification2

# TODO update the JSON string below
json = "{}"
# create an instance of WorkClassification2 from a JSON string
work_classification2_instance = WorkClassification2.from_json(json)
# print the JSON string representation of the object
print(WorkClassification2.to_json())

# convert the object into a dict
work_classification2_dict = work_classification2_instance.to_dict()
# create an instance of WorkClassification2 from a dict
work_classification2_from_dict = WorkClassification2.from_dict(work_classification2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


