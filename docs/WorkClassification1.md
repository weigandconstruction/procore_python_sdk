# WorkClassification1

Work Classification Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** | Is the classifications active or not | [optional] 

## Example

```python
from procore_sdk.models.work_classification1 import WorkClassification1

# TODO update the JSON string below
json = "{}"
# create an instance of WorkClassification1 from a JSON string
work_classification1_instance = WorkClassification1.from_json(json)
# print the JSON string representation of the object
print(WorkClassification1.to_json())

# convert the object into a dict
work_classification1_dict = work_classification1_instance.to_dict()
# create an instance of WorkClassification1 from a dict
work_classification1_from_dict = WorkClassification1.from_dict(work_classification1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


